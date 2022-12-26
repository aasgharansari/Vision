import rclpy
from rclpy.node import Node
import keyboard
from std_msgs.msg import String


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('pubKey')
        self.publisher_ = self.create_publisher(String, 'move', 1)
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()         
        msg.data=self.get_key() 
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1

    def get_key(self):
        msg=String()
        if keyboard.is_pressed ('left'):
            return 'left'
        elif keyboard.is_pressed ('right'):
            return 'right'
        elif keyboard.is_pressed ('up'):
            return 'forward'
        elif keyboard.is_pressed ('down'):
            return 'reverse'
        else:
            return 'stop'
            



def main(args=None):
    rclpy.init(args=args)

    pubKey = MinimalPublisher()

    rclpy.spin(pubKey)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    pubKey.drdestroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()