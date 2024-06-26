// Task 3 Testing
const { expect } = require('chai');
const sinon = require('sinon');
const sendPaymentRequestToApi = require('./3-payment');
const Utils = require('./utils')

describe('sendPaymentRequestToApi', () => {
  it('Should use same math for both functions', () => {
    const calculateNumSpy = sinon.spy(Utils, 'calculateNumber');

    sendPaymentRequestToApi(100, 20);

    sinon.assert.calledWith(calculateNumSpy, 'SUM', 100, 20);

    calculateNumSpy.restore();
  });
});
