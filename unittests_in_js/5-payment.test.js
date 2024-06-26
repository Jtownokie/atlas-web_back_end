// Task 5 Testing
const { expect } = require('chai');
const sinon = require('sinon');
const sendPaymentRequestToApi = require('./4-payment');
const Utils = require('./utils')

describe('sendPaymentRequestToApi', () => {
  beforeEach(() => {
    consoleSpy = sinon.spy(console, 'log');
  });
  afterEach(() => {
    consoleSpy.restore();
  });
  it('Calls function with 100 and 20 to test output', () => {
    sendPaymentRequestToApi(100, 20);
    sinon.assert.calledOnce(consoleSpy);
    sinon.assert.calledWith(consoleSpy, 'The total is: 120');
  });
  it('Calls function with 10 and 10 to test output', () => {
    sendPaymentRequestToApi(10, 10);
    sinon.assert.calledOnce(consoleSpy);
    sinon.assert.calledWith(consoleSpy, 'The total is: 20');
  });
});
