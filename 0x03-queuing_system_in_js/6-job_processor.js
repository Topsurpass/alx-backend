import { createQueue } from 'kue';

// Create new queue that gives us access to redis
const queue = createQueue();

// Function that determines what to do with created jobs
// and its payload / data
const sendNotification = (phoneNumber, message) => {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
};

// Job processor
queue.process('push_notification_code', (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message);
  done();
});
