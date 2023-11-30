// Track progress and errors with Kue: Create the Job creator

import { createQueue } from 'kue';

const queue = createQueue({ name: 'push_notification_code_2' });

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account',
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account',
  },
];

const newJob = (name, payLoad) => {
  const job = queue.create(name, payLoad);
  job.on('enqueue', () => console.log(`Notification job created: ${job.id}`))
    .on('complete', () => console.log(`Notification job ${job.id} completed`))
    .on('failed attempt', (err) => console.log(`Notification job ${job.id} failed: ${err}`))
    // eslint-disable-next-line no-unused-vars
    .on('progress', (progress, _) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });
  job.save();
};

for (const jobPayLoad of jobs) {
  newJob('push_notification_code_2', jobPayLoad);
}
