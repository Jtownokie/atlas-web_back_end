// Task 8 Testing
const { expect } = require('chai');
const request = require('request');

describe('Basic API Integration Testing', () => {
  const url = "http://localhost:7865";

  it('Returns correct status code', () => {
    request(url, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
    });
  });
  it('Returns the correct data', () => {
    request(url, (error, response, body) => {
      expect(body).to.equal('Welcome to the payment system')
    });
  });
});
