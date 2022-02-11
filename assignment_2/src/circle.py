#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist


def turtle_circle():
   
   #Create Publisher Object
   circle_pub = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size=10)
   
   #Initialize the node   
   rospy.init_node('circle', anonymous=True)
   
   #Frequency
   rate = rospy.Rate(1)
   
   cir = Twist()


   while not rospy.is_shutdown():

      #Input desired radius and angular speed
      cir.linear.x = 1.0      #Radius
      cir.angular.z = 1.0     #Speed

      circle_pub.publish(cir)
      rate.sleep()
      
if __name__ == '__main__':
   try:
      turtle_circle()
   except rospy.ROSInterruptException:
      pass
