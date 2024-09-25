import { createClient, print } from 'redis';
import { promisify } from 'util';

async function main() {
    const redisClient =  await createClient();
    
    redisClient.on('error', (error) => {
        console.log(`Redis client not connected to server: ${error.message}`);
        redisClient.quit();
    });
    
    redisClient.on('connect', async () => {
        console.log('Redis client connected to the server');
        await displaySchoolValue('Holberton');
        await setNewSchool('HolbertonSanFrancisco', '100');
        await displaySchoolValue('HolbertonSanFrancisco');
    });

    const setAsync = promisify(redisClient.set).bind(redisClient);
    const getAsync = promisify(redisClient.get).bind(redisClient);
    
    async function setNewSchool (schoolName, value) {
        await setAsync(schoolName, value);
        console.log(`Reply: OK`);
    }
    
    async function displaySchoolValue (schoolName) {
        const getted = await getAsync(schoolName);
        console.log(getted);

    }
}

main();