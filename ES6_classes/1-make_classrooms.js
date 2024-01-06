import ClassRoom from './0-classroom';

export default function initializeRooms() {
  const objOne = new ClassRoom(19);
  const objTwo = new ClassRoom(20);
  const objThree = new ClassRoom(34);

  return [objOne, objTwo, objThree];
}
