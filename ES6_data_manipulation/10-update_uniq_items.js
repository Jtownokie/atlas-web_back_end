// Updating Map Values

export default function updateUniqueItems(map) {
  try {
    const updatedMap = map.forEach((value, key, map) => {
      if (value === 1) {
        map.set(key, 100);
      }
    });

    return updatedMap;
  } catch (error) {
    throw new Error('Cannot process');
  }
}
