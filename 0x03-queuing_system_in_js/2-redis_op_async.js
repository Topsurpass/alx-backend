import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();

// Take function that accept callback (err, data) as its last argument and
// return a version of the function that return promise
const asyncPromise = promisify(client.GET).bind(client);

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));

const setNewSchool = (schoolName, value) => {
  client.SET(schoolName, value, print);
};

// Using promise API for the new promise
const displaySchoolValue = (schoolName) => {
  asyncPromise(schoolName).then((val) => console.log(val));
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

/* Using async/wait for the promise
 *
 * const displaySchoolValue = async (schoolName) => {
    const result = await asyncPromise(schoolName);
    console.log(result);
};

(async ()=> {
 await displaySchoolValue('Holberton');
 setNewSchool('HolbertonSanFrancisco', '100');
 await displaySchoolValue('HolbertonSanFrancisco');
})();
*/
