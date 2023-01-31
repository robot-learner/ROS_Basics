import rospy
from std_msgs.msg import String

def publisher_node():
    pub = rospy.Publisher('/topic_name', String, queue_size=10)
    rospy.init_node('publisher_node', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        message = "Hello ROS!"
        rospy.loginfo(message)
        pub.publish(message)
        rate.sleep()

if __name__ == '__main__':
    publisher_node()
