import { createQueue } from 'kue';

// A data structure that manages the order in which jobs
// are executed
const queue = createQueue({ name: 'push_notification_code' });

// Create new job
// A job is a unit of work or a task that needs to be executed.
// It can be any background task e.g sending email, processing images
// e.t.c
const job = queue.create('push_notification_code', {
  phoneNumber: '+2348123456789',
  message: 'This is the code to verify your account',
});

job.on('enqueue', () => console.log(`Notification job created: ${job.id}`));
job.on('complete', () => console.log('Notification job completed'));
job.on('failed attempt', () => console.log('Notification job failed'));

// Add or save the job to the in-memory queue i.e enqueue the job
// and also persist in storage backend(redis) to process
job.save();
