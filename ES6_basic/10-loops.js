// for of loop

export default function appendToEachArrayValue(array, appendString) {
  for (let [index, item] of array.entries()) {
    array[index] = appendString + item;
  }

  return array;
}
