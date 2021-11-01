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

import rclpy, sys, os, re
from rclpy.node import Node

from std_msgs.msg import String
from interfaces.msg import PubSub

class MinimalSubscriber(Node):

    def __init__(self, topic):
        super().__init__('minimal_subscriber')
        self.topic = topic
        # self.nmr = nmr

        # create a subscription for each publisher
        # for i in range(nmr):
          # self.init_subscription(self.timer_n, topics_info[i+1])
        self.init_subscription(topic)

    def init_subscription(self, topic):

      self.subscription = self.create_subscription(
            PubSub,
            topic,
            self.callback, 10)

      self.subscription

      # The subscriber node’s code is nearly identical to the publisher’s. The constructor creates a subscriber with the same arguments as the publisher. Recall from the topics tutorial that the topic name and message type used by the publisher and subscriber must match to allow them to communicate.
      # The subscriber’s constructor and callback don’t include any timer definition, because it doesn’t need one. Its callback gets called as soon as it receives a message.

    # subscription callback
    def callback(self, msg):
      self.get_logger().info('I heard from [%s - %d]: "%s"' % (msg.pub_name, msg.pub_id, msg.data))

    def timer_callback(self):
      pass
      # if self.priority == self.nmr_pubs:
      # self.priority = 1
      # else:
      # self.priority += 1


def main(args=None):
    rclpy.init(args=args)

    topic = 'main_topic'

    '''
    other version

      topic = 'topic'
      # check how many publishers there are related to the topic
      cmd_topic_info = f'ros2 topic info /{topic}'
      topic_info = os.popen(cmd_topic_info).readlines()
      nmr_pub = int(re.split(':', topic_info[1])[1].strip())

      # check who are the nodes related to the topic
      publishers = []
      cmd_node_list = f'ros2 node list'
      node_list = os.popen(cmd_node_list).readlines()
      for node in node_list:
        node = node.strip()
        cmd_node_info = f'ros2 node info {node}'
        node_info = os.popen(cmd_node_info).read()
        publisher_info = re.search(r'Publishers:\n(.|\n)*(?=Service Servers)', node_info).group(0)

        # if topic in the info of the publisher
        if f'/{topic}:' in publisher_info:
          publishers.append(node[1:])

      # print(publishers) - Debug

      # Priority will at maximum the same as the nmr of pubs
      # Timers should be treated in a different way since you may want to assign different timers
      minimal_subscriber = MinimalSubscriber(topic, nmr_pub, publishers)
    '''

    minimal_subscriber = MinimalSubscriber(topic)
    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
