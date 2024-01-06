// Overwrite casting

export default class Airport {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  toString() {
    return this._location;
  }

  valueOf() {
    return this._size;
  }
}
