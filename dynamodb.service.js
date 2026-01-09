const dynamodb = require('../config/dynamodb');

exports.putItem = async (params) => {
  return dynamodb.put(params).promise();
};
