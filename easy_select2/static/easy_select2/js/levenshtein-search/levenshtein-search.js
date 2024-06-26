const { searchExact, reverse } = require('./utils')

function isEditDistanceNoGreaterThan (a, b, maxDist) {
  if (a.length > b.length) {
    [a, b] = [b, a]
  }
  const lenDelta = b.length - a.length
  if (lenDelta > maxDist) {
    return false
  }

  if (maxDist === 0) {
    return a === b
  }

  let firstDiffIdx
  for (firstDiffIdx = 0; firstDiffIdx < a.length; firstDiffIdx++) {
    if (a[firstDiffIdx] !== b[firstDiffIdx]) break
  }
  if (firstDiffIdx === a.length) {
    return lenDelta <= maxDist
  }

  let lastDiffIdx
  for (lastDiffIdx = a.length - 1; lastDiffIdx >= 0; lastDiffIdx--) {
    if (a[lastDiffIdx] !== b[lastDiffIdx + lenDelta]) break
  }

  a = a.slice(firstDiffIdx, lastDiffIdx + 1)
  b = b.slice(firstDiffIdx, lastDiffIdx + 1 + lenDelta)

  const [dist, length] = _expand(a, b, maxDist)
  return dist + (b.length - length) <= maxDist
}

function editDistance (a, b) {
  if (a.length > b.length) {
    [a, b] = [b, a]
  }
  const scores = new Array(a.length + 1)
  for (let i = 0; i <= a.length; i++) {
    scores[i] = i
  }

  let _prevScore
  let prevScore
  for (let i = 0; i < b.length; i++) {
    scores[0] = i + 1
    prevScore = i
    for (let k = 0; k < a.length; k++) {
      _prevScore = scores[k + 1]
      scores[k + 1] = Math.min(
        prevScore + +(a[k] !== b[i]),
        scores[k] + 1,
        scores[k + 1] + 1
      )
      prevScore = _prevScore
    }
  }

  return scores[a.length]
}

function makeChar2needleIdx (needle, maxDist) {
  const res = {}
  for (let i = Math.min(needle.length - 1, maxDist); i >= 0; i--) {
    res[needle[i]] = i
  }
  return res
}

function * fuzzySearch (needle, haystack, maxDist) {
  if (needle.length > haystack.length + maxDist) return

  const ngramLen = Math.floor(needle.length / (maxDist + 1))

  if (maxDist === 0) {
    for (const index of searchExact(needle, haystack)) {
      yield {
        start: index,
        end: index + needle.length,
        dist: 0
      }
    }
  } else if (ngramLen >= 10) {
    yield * fuzzySearchNgrams(needle, haystack, maxDist)
  } else {
    yield * fuzzySearchCandidates(needle, haystack, maxDist)
  }
}

function _expand (needle, haystack, maxDist) {
  maxDist = +maxDist

  let firstDiff
  for (firstDiff = 0; firstDiff < Math.min(needle.length, haystack.length); firstDiff++) {
    if (needle.charCodeAt(firstDiff) !== haystack.charCodeAt(firstDiff)) break
  }
  if (firstDiff) {
    needle = needle.slice(firstDiff)
    haystack = haystack.slice(firstDiff)
  }

  if (!needle) {
    return [0, firstDiff]
  } else if (!haystack) {
    if (needle.length <= maxDist) {
      return [needle.length, firstDiff]
    } else {
      return [null, null]
    }
  }

  if (maxDist === 0) return [null, null]

  let scores = new Array(needle.length + 1)
  for (let i = 0; i <= maxDist; i++) {
    scores[i] = i
  }
  let newScores = new Array(needle.length + 1)

  let minScore = null
  let minScoreIdx = null
  let maxGoodScore = maxDist
  let firstGoodScoreIdx = 0
  let lastGoodScoreIdx = needle.length - 1

  for (let haystackIdx = 0; haystackIdx < haystack.length; haystackIdx++) {
    const char = haystack.charCodeAt(haystackIdx)

    const needleIdxStart = Math.max(0, firstGoodScoreIdx - 1)
    const needleIdxLimit = Math.min(
      haystackIdx + maxDist,
      needle.length - 1,
      lastGoodScoreIdx
    )

    newScores[0] = scores[0] + 1
    firstGoodScoreIdx = newScores[0] <= maxGoodScore ? 0 : null
    lastGoodScoreIdx = newScores[0] <= maxGoodScore ? 0 : -1

    let needleIdx
    for (needleIdx = needleIdxStart; needleIdx < needleIdxLimit; needleIdx++) {
      const score = newScores[needleIdx + 1] = Math.min(
        scores[needleIdx] + +(char !== needle.charCodeAt(needleIdx)),
        scores[needleIdx + 1] + 1,
        newScores[needleIdx] + 1
      )
      if (score <= maxGoodScore) {
        if (firstGoodScoreIdx === null) firstGoodScoreIdx = needleIdx + 1
        lastGoodScoreIdx = Math.max(
          lastGoodScoreIdx,
          needleIdx + 1 + (maxGoodScore - score)
        )
      }
    }

    const lastScore = newScores[needleIdx + 1] = Math.min(
      scores[needleIdx] + +(char !== needle.charCodeAt(needleIdx)),
      newScores[needleIdx] + 1
    )
    if (lastScore <= maxGoodScore) {
      if (firstGoodScoreIdx === null) firstGoodScoreIdx = needleIdx + 1
      lastGoodScoreIdx = needleIdx + 1
    }

    if (
      needleIdx === needle.length - 1 &&
      (minScore === null || lastScore <= minScore)
    ) {
      minScore = lastScore
      minScoreIdx = haystackIdx
      if (minScore < maxGoodScore) maxGoodScore = minScore
    }

    [scores, newScores] = [newScores, scores]

    if (firstGoodScoreIdx === null) break
  }

  if (minScore !== null && minScore <= maxDist) {
    return [minScore, minScoreIdx + 1 + firstDiff]
  } else {
    return [null, null]
  }
}

function * fuzzySearchNgrams (needle, haystack, maxDist) {
  // use n-gram search
  const ngramLen = Math.floor(needle.length / (maxDist + 1))
  const needleLen = needle.length
  const haystackLen = haystack.length
  for (let ngramStartIdx = 0;
    ngramStartIdx <= needle.length - ngramLen;
    ngramStartIdx += ngramLen
  ) {
    const ngram = needle.slice(ngramStartIdx, ngramStartIdx + ngramLen)

    const ngramEnd = ngramStartIdx + ngramLen
    const needleBeforeReversed = reverse(needle.slice(0, ngramStartIdx))
    const needleAfter = needle.slice(ngramEnd)
    const startIdx = Math.max(0, ngramStartIdx - maxDist)
    const endIdx = Math.min(haystackLen, haystackLen - needleLen + ngramEnd + maxDist)

    for (const haystackMatchIdx of searchExact(ngram, haystack, startIdx, endIdx)) {
      // try to expand left
      const [distRight, rightExpandSize] = _expand(
        needleAfter,
        haystack.slice(
          haystackMatchIdx + ngramLen,
          haystackMatchIdx - ngramStartIdx + needleLen + maxDist
        ),
        maxDist
      )
      if (distRight === null) continue

      const [distLeft, leftExpandSize] = _expand(
        needleBeforeReversed,
        reverse(haystack.slice(
          Math.max(0, haystackMatchIdx - ngramStartIdx - (maxDist - distRight)),
          haystackMatchIdx
        )),
        maxDist - distRight
      )
      if (distLeft === null) continue

      yield {
        start: haystackMatchIdx - leftExpandSize,
        end: haystackMatchIdx + ngramLen + rightExpandSize,
        dist: distLeft + distRight
      }
    }
  }
}

function * fuzzySearchCandidates (needle, haystack, maxDist) {
  const debugFlag = false
  if (debugFlag) console.log(`fuzzySearchCandidates(${needle}, ${haystack}, ${maxDist})`)

  // prepare some often used things in advance
  const needleLen = needle.length
  const haystackLen = haystack.length
  if (needleLen > haystackLen + maxDist) return
  const char2needleIdx = makeChar2needleIdx(needle, maxDist)

  let prevCandidates = [] // candidates from the last iteration
  let candidates = [] // new candidates from the current iteration

  // iterate over the chars in the haystack, updating the candidates for each
  for (let i = 0; i < haystack.length; i++) {
    const haystackChar = haystack[i]

    prevCandidates = candidates
    candidates = []

    const needleIdx = char2needleIdx[haystackChar]
    if (needleIdx !== undefined) {
      if (needleIdx + 1 === needleLen) {
        if (debugFlag) {
          console.log(`yield ${{
            start: i,
            end: i + 1,
            dist: needleIdx
          }}`)
        }
        yield {
          start: i,
          end: i + 1,
          dist: needleIdx
        }
      } else {
        candidates.push({
          startIdx: i,
          needleIdx: needleIdx + 1,
          dist: needleIdx
        })
      }
    }

    for (const candidate of prevCandidates) {
      // if this sequence char is the candidate's next expected char
      if (needle[candidate.needleIdx] === haystackChar) {
        // if reached the end of the needle, return a match
        if (candidate.needleIdx + 1 === needleLen) {
          if (debugFlag) {
            console.log(`yield ${{
              start: candidate.startIdx,
              end: i + 1,
              dist: candidate.dist
            }}`)
          }
          yield {
            start: candidate.startIdx,
            end: i + 1,
            dist: candidate.dist
          }
        } else {
          // otherwise, update the candidate's needleIdx and keep it
          candidates.push({
            startIdx: candidate.startIdx,
            needleIdx: candidate.needleIdx + 1,
            dist: candidate.dist
          })
        }
      } else {
        if (candidate.dist === maxDist) continue

        candidates.push({
          startIdx: candidate.startIdx,
          needleIdx: candidate.needleIdx,
          dist: candidate.dist + 1
        })

        for (let nSkipped = 1; nSkipped <= maxDist - candidate.dist; nSkipped++) {
          if (candidate.needleIdx + nSkipped === needleLen) {
            if (debugFlag) {
              console.log(`yield ${{
                start: candidate.startIdx,
                end: i + 1,
                dist: candidate.dist + nSkipped
              }}`)
            }
            yield {
              start: candidate.startIdx,
              end: i + 1,
              dist: candidate.dist + nSkipped
            }
            break
          } else if (needle[candidate.needleIdx + nSkipped] === haystackChar) {
            if (candidate.needleIdx + nSkipped + 1 === needleLen) {
              if (debugFlag) {
                console.log(`yield ${{
                  start: candidate.startIdx,
                  end: i + 1,
                  dist: candidate.dist + nSkipped
                }}`)
              }
              yield {
                start: candidate.startIdx,
                end: i + 1,
                dist: candidate.dist + nSkipped
              }
            } else {
              candidates.push({
                startIdx: candidate.startIdx,
                needleIdx: candidate.needleIdx + 1 + nSkipped,
                dist: candidate.dist + nSkipped
              })
            }
            break
          }
        }

        if (i + 1 < haystackLen && candidate.needleIdx + 1 < needleLen) {
          candidates.push({
            startIdx: candidate.startIdx,
            needleIdx: candidate.needleIdx + 1,
            dist: candidate.dist + 1
          })
        }
      }
    }

    if (debugFlag) console.log(candidates)
  }

  for (const candidate of candidates) {
    candidate.dist += needle.length - candidate.needleIdx
    if (candidate.dist <= maxDist) {
      yield {
        start: candidate.startIdx,
        end: haystack.length,
        dist: candidate.dist
      }
    }
  }
}

module.exports = {
  _expand,
  editDistance,
  fuzzySearch,
  fuzzySearchNgrams,
  fuzzySearchCandidates,
  isEditDistanceNoGreaterThan
}
