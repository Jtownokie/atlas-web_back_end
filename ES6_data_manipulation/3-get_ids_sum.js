// Using Reduce

export default function getStudentIdsSum(array) {
  const sumWithInitial = array.reduce((accumulator, item) => accumulator + item.id, 0);

  return sumWithInitial;
}
