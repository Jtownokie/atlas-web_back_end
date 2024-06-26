// Task 0 Testing
const assert = require('assert')
const calculateNumber = require('./0-calcul')

describe('test_group', () => {
  it('returns the sum of its rounded arguments', () => {
    assert.ok(calculateNumber(1, 3) === 4);
  });
});
