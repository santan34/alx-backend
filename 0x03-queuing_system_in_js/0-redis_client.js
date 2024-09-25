import { createClient } from 'redis';
async function main () {
  const redisClient = await createClient();

  redisClient.on('error', (error) => {
    console.log(`Redis client not connected to server: ${error.message}`);
    redisClient.quit();
  });
  redisClient.on('connect', () => console.log('Redis client connected to the server'));
}

main();
