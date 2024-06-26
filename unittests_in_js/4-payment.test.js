// Task 4 Testing
const { expect } = require('chai');
const sinon = require('sinon');
const sendPaymentRequestToApi = require('./4-payment');
const Utils = require('./utils')

describe('sendPaymentRequestToApi', () => {
  it('Stub function to reduce performance cost', () => {
    calculateStub = sinon.stub(Utils, 'calculateNumber').returns(10);
    consoleSpy = sinon.spy(console, 'log');

    sendPaymentRequestToApi(100, 20);

    sinon.assert.calledWith(calculateStub, 'SUM', 100, 20);
    sinon.assert.calledWith(consoleSpy, 'The total is: 10');

    calculateStub.restore();
    consoleSpy.restore();
  });
});
