#!/usr/bin/node
exports.logMe = function (item) {
  if (typeof nb === 'undefined') {
    nb = 0;
  }

  console.log(`${nb++}: ${item}`);
};
