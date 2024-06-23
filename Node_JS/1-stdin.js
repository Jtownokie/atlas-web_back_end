// Task 1 Script

console.log("Welcome to Holberton School, what is your name?");

process.stdin.setEncoding('utf8')

process.stdin.on('readable', function() {
  let input = process.stdin.read();
  if (input !== null) {
    process.stdout.write('Your name is: ' + input);
  }
});

process.stdin.on('end', function() {
  process.stdout.write('This important software is now closing' + '\n')
});
