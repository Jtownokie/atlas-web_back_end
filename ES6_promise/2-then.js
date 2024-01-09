// Resolving/Rejecting Promises

export default function handleResponseFromAPI(promise) {
  return promise.then(() => { return { body: 'success', status: 200 } }, () => new Error()).finally(console.log('Got a response from the API'));
}
