#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
import math
from turtlesim.msg import Pose

#angular_speed = math.radians(abs(angular_speed_degreehu))
def turtle_square():

	rospy.init_node("straight", anonymous = True)
	pub = rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)

	vel = Twist()
	
	vel.linear.x = 0.2
	rate = rospy.Rate(1)
	while not rospy.is_shutdown():
	#for i in range(4):
		vel.linear.x = 0.2
		t0 = rospy.Time.now().to_sec()
		current_dist = 0

		while current_dist <= 2:
			pub.publish(vel)
			t1=rospy.Time.now().to_sec()
			current_dist = round(((vel.linear.x)*(t1-t0)),5)
		print("Side of the square is: ", round((current_dist),2))
			
		vel.linear.x = 0
		pub.publish(vel)
		t2 = rospy.Time.now().to_sec()
		while True:
			vel.angular.z = 0.2
			pub.publish(vel)
			t3 = rospy.Time.now().to_sec()
			current_angle = (t3-t2)*(vel.angular.z)

			if current_angle > 1.5708:
				break
		vel.angular.z = 0
		pub.publish(vel)
			
	rate.sleep()
		



if __name__ == '__main__':
	try:
		turtle_square()
	except rospy.ROSInterruptException: 
		pass
