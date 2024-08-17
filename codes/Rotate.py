#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

names = [f"turtle{i+1}" for i in range(27)]

def rotate_turtle():
    rospy.init_node('rotating_node', anonymous=True)

    publishers = {}
    for turtle in names:
        topic_name = f'/{turtle}/cmd_vel'
        try:
            pub = rospy.Publisher(topic_name, Twist, queue_size=10)
            publishers[turtle] = pub
            rospy.loginfo(f'Publisher created for {turtle}')
        except Exception as e:
            rospy.logwarn(f'Failed to create publisher for {turtle}: {e}')

    rospy.sleep(1)

    rate = rospy.Rate(10)

    vel_msg = Twist()

    vel_msg.angular.z = -1

 
    duration = 50
    start_time = rospy.Time.now().to_sec()

    while rospy.Time.now().to_sec() - start_time < duration:
        for turtle, pub in publishers.items():
            pub.publish(vel_msg)
            rospy.loginfo(f'Published rotate command to {turtle}')
        rate.sleep()

    vel_msg.angular.z = 0.0
    for turtle, pub in publishers.items():
        pub.publish(vel_msg)
        rospy.loginfo(f'Stopped {turtle}')

if __name__ == '__main__':
    try:
        rotate_turtle()
    except rospy.ROSInterruptException:
        pass