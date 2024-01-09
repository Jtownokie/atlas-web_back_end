// Clean Set function
/* eslint-disable no-unused-vars */

export default function cleanSet(set, startString) {
  let resultString = '';

  if (!startString || typeof startString !== 'string') {
    return '';
  }

  for (let element of set) {
    if (element.startsWith(startString)) {
      resultString += startString === '' ? element : element.slice(startString.length) + '-';
    }
  }

  resultString = resultString.slice(0, -1);

  return resultString;
}
