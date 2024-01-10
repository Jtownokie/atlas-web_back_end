// Handling multiple promises
import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.all([signUpUser(firstName, lastName), uploadPhoto(fileName)]).then(([signUpResult, uploadResult]) => {
    return [{ status: signUpResult.status, value: signUpResult.value }, { status: uploadResult.status, value: uploadResult.value }];
  })
}
