// Resolving/Rejecting Promises

export default function handleResponseFromAPI(promise) {
  return promise.then(function() { return { body: 'success', status: 200 } }, function() { new Error() }).finally(console.log('Got a response from the API'));
}
