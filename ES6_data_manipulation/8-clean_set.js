// Clean Set function
/* eslint-disable no-unused-vars */
/* eslint-disable no-useless-concat */

export default function cleanSet(set, startString) {
  let resultString = '';

  if (!startString || typeof startString !== 'string') {
    return '';
  }

  for (const element of set) {
    if (element.startsWith(startString)) {
      resultString += element.slice(startString.length) + '-';
    }
  }

  resultString = resultString.slice(0, -1);

  return resultString;
}
