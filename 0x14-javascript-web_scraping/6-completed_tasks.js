#!/usr/bin/node
const request = require('request');

request(
  `${process.argv[2]}?completed=true`,
  function (error, response, body) {
    if (!error) {
      const tasks = JSON.parse(body);
      const completedTasks = {};

      tasks.forEach(task => {
        if (completedTasks[task.userId] === undefined) {
          completedTasks[task.userId] = 1;
        } else {
          completedTasks[task.userId] += 1;
        }
      });

      console.log(completedTasks);
    }
  }
);
