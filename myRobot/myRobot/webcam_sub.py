import rclpy # Python library for ROS 2
from rclpy.node import Node # Handles the creation of nodes
from sensor_msgs.msg import Image # Image is the message type
import cv2 # OpenCV library
from cv_bridge import CvBridge # Package to convert between ROS and OpenCV Images

 
class ImageSubscriber(Node):
    def __init__(self):
        super().__init__('webcam_sub')
        self.subscription = self.create_subscription(
            Image, 
            'video_frames', 
            self.listener_callback, 
            10)
        self.subscription # prevent unused variable warning
        self.br = CvBridge()
   
    def listener_callback(self, data):
        self.get_logger().info('Receiving video frame')
        current_frame = self.br.imgmsg_to_cv2(data)
        cv2.imshow("camera", current_frame)
    
        cv2.waitKey(1)
  
def main(args=None):
    rclpy.init(args=args)
    webcam_sub = ImageSubscriber()
    rclpy.spin(webcam_sub)
    webcam_sub.destroy_node()
    rclpy.shutdown()
  
if __name__ == '__main__':
  main()