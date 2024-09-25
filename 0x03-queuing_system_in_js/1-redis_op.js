import { createClient, print } from 'redis';

const redisClient = createClient();

redisClient.on('error', (error) => {
  console.log(`Redis client not connected to server: ${error.message}`);
  redisClient.quit();
});
redisClient.on('connect', () => {
  console.log('Redis client connected to the server');
  displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  displaySchoolValue('HolbertonSanFrancisco');
});

function setNewSchool (schoolName, value) {
  redisClient.set(schoolName, value, print);
}

function displaySchoolValue (schoolName) {
  redisClient.get(schoolName, (err, res) => {
    if (err) {
      console.log('pabhaizika');
    } else {
      console.log(res);
    }
  });
}
