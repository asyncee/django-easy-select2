const { editDistance, fuzzySearch, isEditDistanceNoGreaterThan } =
  require('./levenshtein-search')

module.exports = {
  editDistance,
  fuzzySearch,
  isEditDistanceNoGreaterThan
}
