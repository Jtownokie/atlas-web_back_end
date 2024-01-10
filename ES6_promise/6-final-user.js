// Handling multiple promises
import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.all([signUpUser(firstName, lastName), uploadPhoto(fileName)]).then(([signUpResult, uploadResult]) => {
    return [
      { status: 'fulfilled', value: { firstName: signUpResult.firstName, lastName: signUpResult.lastName } },
      { status: 'rejected', value: `Error: ${uploadResult.message}` }
    ];
  })
}
