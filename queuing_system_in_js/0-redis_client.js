// Task 1 Script
import { createClient } from 'redis';

async function initializeRedis() {
  try {
    const client = await createClient()

    client.on('error', (err) => {console.log('Redis client not connected to the server: ', err)});
    client.on('connect', () => {console.log('Redis client connected to the server')});
  } catch (err) {
    console.error(err);
  }
  
}

initializeRedis();

