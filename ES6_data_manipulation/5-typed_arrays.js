// Practicing Typed Arrays

export default function createInt8TypedArray(length, position, value) {
  const buffer = new ArrayBuffer(length);
  const view = new DataView(buffer);

  try {
    view.setInt8(position, value);
  } catch {
    throw 'Position outside range'
  }

  return view;
}
