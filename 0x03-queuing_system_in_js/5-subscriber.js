import { createClient } from 'redis';

const client = createClient();

client.on('connect', () => console.log('Redis client connected to the server'));
client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));

client.subscribe('holberton school channel');

client.on('message', (_, messg) => {
  console.log(messg);
  if (messg === 'KILL_SERVER') {
    client.unsubscribe();
    client.quit();
  }
});
