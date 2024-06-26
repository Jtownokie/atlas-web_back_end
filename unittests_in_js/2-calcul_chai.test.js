// Task 1 Tests
const { expect } = require('chai')
const calculateNumber = require('./1-calcul')

describe('test_group_sum', () => {
  it('returns the calculation type result (sum) of its rounded arguments', () => {
    expect(calculateNumber('SUM', 1, 3)).to.equal(4);
    expect(calculateNumber('SUM', 1, 3.7)).to.equal(5);
    expect(calculateNumber('SUM', 1, 3.4)).to.equal(4);
    expect(calculateNumber('SUM', 1.2, 3)).to.equal(4);
    expect(calculateNumber('SUM', 1.6, 3)).to.equal(5);
    expect(calculateNumber('SUM', 1.5, 3.7)).to.equal(6);
  });
});

describe('test_group_subtract', () => {
  it('returns the calculation type result (difference) of its rounded arguments', () => {
    expect(calculateNumber('SUBTRACT', 1, 3)).to.equal(-2);
    expect(calculateNumber('SUBTRACT', 1, 3.7)).to.equal(-3);
    expect(calculateNumber('SUBTRACT', 1, 3.4)).to.equal(-2);
    expect(calculateNumber('SUBTRACT', 1.2, 3)).to.equal(-2);
    expect(calculateNumber('SUBTRACT', 1.6, 3)).to.equal(-1);
    expect(calculateNumber('SUBTRACT', 1.5, 3.7)).to.equal(-2);
  });
});

describe('test_group_divide', () => {
  it('returns the calculation type result (quotient) of its rounded arguments', () => {
    expect(calculateNumber('DIVIDE', 3, 1)).to.equal(3);
    expect(calculateNumber('DIVIDE', 3.7, 2)).to.equal(2);
    expect(calculateNumber('DIVIDE', 6, 3.4)).to.equal(2);
    expect(calculateNumber('DIVIDE', 8.2, 4)).to.equal(2);
    expect(calculateNumber('DIVIDE', 3.6, 2)).to.equal(2);
    expect(calculateNumber('DIVIDE', 3.5, 2.4)).to.equal(2);
    expect(calculateNumber('DIVIDE', 3, 0)).to.equal('Error');
  });
});
