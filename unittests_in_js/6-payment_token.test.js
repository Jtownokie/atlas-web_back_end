// Task 6 Testing
const { expect } = require('chai');
const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI', () => {
  it('Tests function with Promise return', (done) => {
    const tokenPromise = getPaymentTokenFromAPI(true);

    tokenPromise
      .then((token) => {
        expect(token).to.deep.equal({ data: 'Successful response from the API' });
        done();
      })
      .catch(done);
  });
});
