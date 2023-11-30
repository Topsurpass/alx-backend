import { createClient, print } from 'redis';

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));

const createHash = (hashName, hashObj) => {
  for (const [field, value] of Object.entries(hashObj)) {
    client.HSET(hashName, field, value, print);
  }
};

const printHash = (hashName) => {
  client.HGETALL(hashName, (_, hashData) => console.log(hashData));
};

const myObj = {
  Portland: 50,
  Seattle: 80,
  'New York': 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2,
};

(() => {
  createHash('HolbertonSchools', myObj);
  printHash('HolbertonSchools');
})();
