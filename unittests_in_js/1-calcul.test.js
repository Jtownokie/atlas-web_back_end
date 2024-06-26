// Task 1 Tests
const assert = require('assert')
const calculateNumber = require('./1-calcul')

describe('test_group_sum', () => {
  it('returns the calculation type result (sum) of its rounded arguments', () => {
    assert.ok(calculateNumber('SUM', 1, 3) === 4);
    assert.ok(calculateNumber('SUM', 1, 3.7) === 5);
    assert.ok(calculateNumber('SUM', 1, 3.4) === 4);
    assert.ok(calculateNumber('SUM', 1.2, 3) === 4);
    assert.ok(calculateNumber('SUM', 1.6, 3) === 5);
    assert.ok(calculateNumber('SUM', 1.5, 3.7) === 6);
  });
});

describe('test_group_subtract', () => {
  it('returns the calculation type result (difference) of its rounded arguments', () => {
    assert.ok(calculateNumber('SUBTRACT', 1, 3) === -2);
    assert.ok(calculateNumber('SUBTRACT', 1, 3.7) === -3);
    assert.ok(calculateNumber('SUBTRACT', 1, 3.4) === -2);
    assert.ok(calculateNumber('SUBTRACT', 1.2, 3) === -2);
    assert.ok(calculateNumber('SUBTRACT', 1.6, 3) === -1);
    assert.ok(calculateNumber('SUBTRACT', 1.5, 3.7) === -2);
  });
});

describe('test_group_divide', () => {
  it('returns the calculation type result (quotient) of its rounded arguments', () => {
    assert.ok(calculateNumber('DIVIDE', 3, 1) === 3);
    assert.ok(calculateNumber('DIVIDE', 3.7, 2) === 2);
    assert.ok(calculateNumber('DIVIDE', 6, 3.4) === 2);
    assert.ok(calculateNumber('DIVIDE', 8.2, 4) === 2);
    assert.ok(calculateNumber('DIVIDE', 3.6, 2) === 2);
    assert.ok(calculateNumber('DIVIDE', 3.5, 2.4) === 2);
    assert.ok(calculateNumber('DIVIDE', 3, 0) === 'Error');
  });
});
