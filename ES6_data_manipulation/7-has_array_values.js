// Checking Set for Values
/* eslint-disable no-unused-vars */

export default function hasValuesFromArray(set, array) {
  return array.every((element, index, array) => {
    return set.has(element);
  });
}
