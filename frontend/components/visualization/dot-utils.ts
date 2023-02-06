/**
 * Adds quotation marks to label with more than two words.
 *
 * @param {string} label - label-name
 * @return {string} - label with quotation
 */
export const getInQuotationMarks = (label: String | String[]): String => {
  return label.indexOf(' ') != -1 ? '"' + label + '"' : label.toString();
};

/**
 * Converts places of transitions of a petrinet into DOT language.
 *
 * @param {Array<String> | String} t - places
 * @return {string} - place of petrinet
 */
export const getPlacesAsDOT = (t: Array<String> | String) => {
  return typeof t == 'string'
    ? getInQuotationMarks(t)
    : '"(' +
        getInQuotationMarks(t[0]) +
        '->' +
        getInQuotationMarks(t[1]) +
        ')"';
};

/**
 * Converts flow of petrinet (edges of graph) into DOT language.
 *
 * @param {Array<Array<String>> | String} f - flow
 * @return {string} - edges of petrinet
 */
export const getFlowAsDOT = (f: Array<Array<String>> | String) => {
  return typeof f[0] == 'string' && typeof f[1] != 'string'
    ? getInQuotationMarks(f[0]) +
        '->' +
        '"(' +
        getInQuotationMarks(f[1][0]) +
        '->' +
        getInQuotationMarks(f[1][1]) +
        ')"'
    : typeof f[0] != 'string' && typeof f[1] == 'string'
    ? '"(' +
      getInQuotationMarks(f[0][0]) +
      '->' +
      getInQuotationMarks(f[0][1]) +
      ')"->' +
      getInQuotationMarks(f[1])
    : getInQuotationMarks(f[0]) + '->' + getInQuotationMarks(f[1]);
};

/**
 * Converts flow of dependency-net (edges of graph) into DOT language.
 *
 * @param {[string, string, number, number]} e - flow of dependency-net
 * @return {string} - label of edge
 */
export const getEdgesAsDOT = (e: [string, string, number, number]) => {
  return (
    getInQuotationMarks(e[0]) +
    ' -> ' +
    getInQuotationMarks(e[1]) +
    ` [ label="${e[2]}(${e[3]})" ];`
  );
};

/**
 * Converts row of relation-enums to relation-symbol.
 *
 * @param {Array<String>} e - row of footprint-matrix
 * @return {Array<String>} - row with relation-symbols (->, <-, ||, #)
 */
export const convertToRelations = (row: Array<String>) => {
  return row.map((cell) => {
    switch (cell) {
      case 'causality_right':
        return '→';
      case 'causality_left':
        return '←';
      case 'parallel':
        return '||';
      case 'unrelated':
        return '#';
      default:
        'none';
    }
  });
};
