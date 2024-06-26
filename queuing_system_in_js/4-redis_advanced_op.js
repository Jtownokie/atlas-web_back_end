// Task 4 Script
import { createClient, print } from 'redis';

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err);
});

const schoolName = 'HolbertonSchools';
const details = {
  Portland: 50,
  Seattle: 80,
  'New York': 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2
};

const fields = Object.entries(details);

fields.forEach(([field, value]) => {
  client.hset(schoolName, field, value, print);
})

client.hgetall(schoolName, (err, reply) => {
  console.log(reply);
});
