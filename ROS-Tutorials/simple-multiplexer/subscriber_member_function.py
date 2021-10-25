# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.timer_period = 9 # Default value - multiple of 3 (preferably) -> 3 messages per publisher
        self.priority = 1
        self.topic = ''

        if self.priority == 1:
          self.topic = 'topic_1'
          # self.timer_period = 15 -> 5 messages
        else:
          self.topic = 'topic_2'
          # self.timer_period = 9 -> 3 messages

        self.subscription = self.create_subscription(
            String,
            self.topic,
            self.listener_callback,
          10)

        self.subscription
        self.timer = self.create_timer(self.timer_period, self.timer_callback)

        # The subscriber node’s code is nearly identical to the publisher’s. The constructor creates a subscriber with the same arguments as the publisher. Recall from the topics tutorial that the topic name and message type used by the publisher and subscriber must match to allow them to communicate.
        # The subscriber’s constructor and callback don’t include any timer definition, because it doesn’t need one. Its callback gets called as soon as it receives a message.


    def listener_callback(self, msg):
      if self.priority == 1:
        self.get_logger().info('Listening to Publisher 1 - I heard: "%s"' % msg.data)
      else:
        self.get_logger().info('Listening to Publisher 2 - I heard: "%s"' % msg.data)


    def timer_callback(self):
      self.change_priority()

    def change_priority(self):
      self.priority = 1 if self.priority == 0 else 0

def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
