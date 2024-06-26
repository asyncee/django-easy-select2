function * searchExact (needle, haystack, startIndex = 0, endIndex = null) {
  const needleLen = needle.length
  if (needleLen === 0) return

  if (endIndex === null) {
    endIndex = haystack.length
  }
  let index

  while ((index = haystack.indexOf(needle, startIndex)) > -1) {
    if (index + needle.length > endIndex) break
    yield index
    startIndex = index + 1
  }
}

function reverse (string) {
  return string
    .split('')
    .reverse()
    .join('')
}

module.exports = {
  searchExact,
  reverse
}
