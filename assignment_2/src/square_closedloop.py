#!/usr/bin/env python3
import rospy
import math
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

def position(pose):
    global a,b,c
    a = pose.x
    b = pose.y
    c = pose.theta

def gotogoal():
    vel = Twist()
    pose = Pose()
    rospy.init_node("square_closedloop", anonymous = True)
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size = 10)
    rate = rospy.Rate(1)
    rospy.Subscriber("/turtle1/pose", Pose , position)
    g1 = float(input("Goal X co-ordinate: "))
    g2 = float(input("Goal Y co-ordinate: "))
    

    while not rospy.is_shutdown():
        distance = math.sqrt( (g1-a)**2 + (g2-b)**2 )
        vel.linear.x = 0.3 * distance
        vel.angular.z = (math.atan2((g2-b),(g1-a) ) - c)
        pub.publish(vel)
        rate.sleep()
        if distance < 0.01:
            break

if __name__ == "__main__":
    try:
        gotogoal() 
    except rospy.ROSInterruptException:
        pass



#(5,5) ->(8,5) -> (8,8) -> (5,8) -> (5,5)