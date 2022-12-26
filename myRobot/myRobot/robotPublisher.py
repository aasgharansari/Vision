import rclpy
from rclpy.node import Node
import getch as gh
from std_msgs.msg import String


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('robotPublisher')
        self.publisher_ = self.create_publisher(String, 'move', 1)
        timer_period = 0.05  # seconds
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
        msg.data = 'stop'        
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        first_char = gh.getch()
        if first_char == '\x1b':
            return {'[A': 'forward', '[B': 'reverse', '[C': 'right', '[D': 'left'}[gh.getch() + gh.getch()]
        else:
            return first_char



def main(args=None):
    rclpy.init(args=args)

    robotPublisher = MinimalPublisher()

    rclpy.spin(robotPublisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    robotPublisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()