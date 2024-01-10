// Handling multiple promises
import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.all([
    signUpUser(firstName, lastName),
    uploadPhoto(fileName).catch((error) => ({ status: 'rejected', value: `Error: ${error.message}` }))
  ]).then(([signUpResult, uploadResult]) => {
    return [
      { status: 'fulfilled', value: { firstName: signUpResult.firstName, lastName: signUpResult.lastName } },
      { status: uploadResult.status, value: uploadResult.value }
    ];
  });
}
