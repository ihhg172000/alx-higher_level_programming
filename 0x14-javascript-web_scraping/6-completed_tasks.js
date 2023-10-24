#!/usr/bin/node
const request = require('request');

request(
  process.argv[2],
  function (error, response, body) {
    if (!error && response.statusCode === 200) {
      const tasks = JSON.parse(body);
      const completedTasks = tasks.filter(task => {
        return task.completed;
      }
      );

      const usersTasks = {};

      completedTasks.forEach(task => {
        if (usersTasks[task.userId] === undefined) {
          usersTasks[task.userId] = 1;
        } else {
          usersTasks[task.userId] += 1;
        }
      });

      console.log(usersTasks);
    }
  }
);
