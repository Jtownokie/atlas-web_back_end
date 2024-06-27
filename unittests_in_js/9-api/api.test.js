// Task 8 Testing
const { expect } = require('chai');
const request = require('request');

describe('GET / API Integration Testing', () => {
  const url = "http://localhost:7865";

  it('Returns correct status code', () => {
    request(url, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
    });
  });

  it('Returns the correct data', () => {
    request(url, (error, response, body) => {
      expect(body).to.deep.equal('Welcome to the payment system')
    });
  });
});

describe('GET /cart/:id Integration Testing', () => {
  it('Returns correct status code', () => {
    request("http://localhost:7865/cart/12", (error, response, body) => {
      expect(response.statusCode).to.equal(200);
    });
  });

  it('Returns correct data', () => {
    request("http://localhost:7865/cart/12", (error, response, body) => {
      expect(body).to.deep.equal('Payment methods for cart 12');
    });
  });

  it('Returns correct error code', () => {
    request("http://localhost:7865/cart/hello", (error, response, body) => {
      expect(response.statusCode).to.equal(404);
    });
  })
});
