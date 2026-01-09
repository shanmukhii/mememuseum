const sns = require('../config/sns');

exports.sendNotification = async (topicArn, message) => {
  await sns.publish({
    TopicArn: topicArn,
    Message: message
  }).promise();
};
