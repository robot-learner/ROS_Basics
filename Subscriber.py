import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    
def subscriber_node():
    rospy.init_node('subscriber_node', anonymous=True)
    rospy.Subscriber("/topic_name", String, callback)
    rospy.spin()

if __name__ == '__main__':
    subscriber_node()
