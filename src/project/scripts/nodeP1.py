#!/usr/bin/env python
import rospy 
import time
import math

from sensor_msgs.msg import PointCloud
from geometry_msgs.msg import Twist, Vector3

flag = 0

x_dist = 0
y_dist = 0

def callback(data):
	
	global flag
	global x_dist
	global y_dist

	sonar0_x = data.points[0].x

	sonar1_x = data.points[1].x

	sonar2_x = data.points[2].x

	sonar3_x = data.points[3].x
	
	sonar4_x = data.points[4].x

	sonar5_x = data.points[5].x

	sonar6_x = data.points[6].x

	sonar7_x = data.points[7].x

	sonar8_x = data.points[8].x

	sonar9_x = data.points[9].x

	sonar10_x = data.points[10].x

	sonar11_x = data.points[11].x

	sonar12_x = data.points[12].x

	sonar13_x = data.points[13].x

	sonar14_x = data.points[14].x

	sonar15_x = data.points[15].x


	sonar0_y = data.points[0].y

	sonar1_y = data.points[1].y

	sonar2_y = data.points[2].y

	sonar3_y = data.points[3].y
	
	sonar4_y = data.points[4].y

	sonar5_y = data.points[5].y

	sonar6_y = data.points[6].y

	sonar7_y = data.points[7].y

	sonar8_y = data.points[8].y

	sonar9_y = data.points[9].y

	sonar10_y = data.points[10].y

	sonar11_y = data.points[11].y

	sonar12_y = data.points[12].y

	sonar13_y = data.points[13].y

	sonar14_y = data.points[14].y

	sonar15_y = data.points[15].y


	print ('Sonar 0')
	print ('x: %s' %sonar0_x); print ('y: %s' %sonar0_y)
	print
	print ('Sonar 1')
	print ('x: %s' %sonar1_x); print ('y: %s' %sonar1_y)
	print
	print ('Sonar 2')
	print ('x: %s' %sonar2_x); print ('y: %s' %sonar2_y)
	print
	print ('Sonar 3')
	print ('x: %s' %sonar3_x); print ('y: %s' %sonar3_y)
	print
	print ('Sonar 4')
	print ('x: %s' %sonar4_x); print ('y: %s' %sonar4_y)
	print
	print ('Sonar 5')
	print ('x: %s' %sonar5_x); print ('y: %s' %sonar5_y)
	print
	print ('Sonar 6')
	print ('x: %s' %sonar6_x); print ('y: %s' %sonar6_y)
	print
	print ('Sonar 7')
	print ('x: %s' %sonar7_x); print ('y: %s' %sonar7_y)
	print
	print ('Sonar 8')
	print ('x: %s' %sonar8_x); print ('y: %s' %sonar8_y)
	print
	print ('Sonar 9')
	print ('x: %s' %sonar9_x); print ('y: %s' %sonar9_y)
	print
	print ('Sonar 10')
	print ('x: %s' %sonar10_x); print ('y: %s' %sonar10_y)
	print
	print ('Sonar 11')
	print ('x: %s' %sonar11_x); print ('y: %s' %sonar11_y)
	print
	print ('Sonar 12')
	print ('x: %s' %sonar12_x); print ('y: %s' %sonar12_y)
	print
	print ('Sonar 13')
	print ('x: %s' %sonar13_x); print ('y: %s' %sonar13_y)
	print
	print ('Sonar 14')
	print ('x: %s' %sonar14_x); print ('y: %s' %sonar14_y)
	print
	print ('Sonar 15')
	print ('x: %s' %sonar15_x); print ('y: %s' %sonar15_y)
	print ('-----------------')




# #__________________________________________________________________

# Become parallel to a wall

	if flag == 0:

		if (((abs(sonar7_y) - abs(sonar8_y)) <= 0.01) and ((abs(sonar0_y) - abs(sonar15_y)) <= 0.01)) and (((abs(sonar3_x) - abs(sonar4_x)) <= 0.01) and (abs(sonar11_x) - abs(sonar12_x) <= 0.01)) :
			msg.linear.x = 0
			msg.angular.z = 0
			print 'Parallel to wall'
			time.sleep(2)
			flag += 1

		else:
			msg.linear.x = 0
			msg.angular.z = 0.2 

#____________________________________________________________________

# #Measure Distance

	if flag == 1:
		x_dist = round(abs(sonar3_x) + abs(sonar12_x),2)
		y_dist = round(abs(sonar0_y) + abs(sonar7_y),2)
		#x_dist = (((abs(sonar3_x) + abs(sonar4_x))/2) + ((abs(sonar11_x) + abs(sonar12_x))/2))
		#y_dist = (((abs(sonar0_y) + abs(sonar15_y))/2) + ((abs(sonar7_y) + abs(sonar8_y))/2))
		print 'Measured Distance'
		print 'X Dist =', x_dist
		print 'Y Dist = ', y_dist
		time.sleep(2)
		flag += 1

# #____________________________________________________________________

# ##Find Center
	

	if flag == 2:


		if abs(x_dist) > 3:

			if abs(sonar3_x) <= (x_dist/2) and abs(sonar4_y) <= (x_dist/2):
				msg.linear.x = 0
				msg.angular.z = 0.25
				print '1'

			elif abs(sonar0_y) <= (y_dist/2) and abs(sonar15_y) <= (y_dist/2):
				msg.linear.x = 0
				msg.angular.z = 0.25
				print '2'

			elif abs(sonar2_x) <= (x_dist/2) and abs(sonar5_y) <= (x_dist/2):
				msg.linear.x = 0
				msg.angular.z = 0.25
				print '3'

			elif ((abs(sonar2_x) >= 5) or (abs(sonar3_x) >= 5)) or (abs(sonar4_x) >= 5):
				msg.linear.x = 0
				msg.angular.z = 0.5
				print '4'


			elif (abs(sonar3_x) - abs(sonar11_x)) <= 0.1 and (abs(sonar0_y) - abs(sonar7_y)) <= 0.1:
				msg.linear.x = 0
				msg.angular.z = 0
				print 'found center'
				time.sleep(5)
				flag += 1
			
			else:
				msg.linear.x = 0.2
				msg.angular.z = 0

		else:

			if abs(sonar3_x) <= (y_dist/2) and abs(sonar4_y) <= (y_dist/2):
				msg.linear.x = 0
				msg.angular.z = 0.25
				print '1'

			elif abs(sonar0_y) <= (x_dist/2) and abs(sonar15_y) <= (x_dist/2):
				msg.linear.x = 0
				msg.angular.z = 0.25
				print '2'

			elif abs(sonar2_x) <= (y_dist/2) and abs(sonar5_y) <= (y_dist/2):
				msg.linear.x = 0
				msg.angular.z = 0.25
				print '3'

			elif ((abs(sonar2_x) >= 5) or (abs(sonar3_x) >= 5)) or (abs(sonar4_x) >= 5):
				msg.linear.x = 0
				msg.angular.z = 0.5
				print '4'

			elif (abs(sonar3_x) - abs(sonar11_x)) <= 0.1 and (abs(sonar0_y) - abs(sonar7_y)) <= 0.1:
				msg.linear.x = 0
				msg.angular.z = 0
				print 'found center'
				time.sleep(5)
				flag += 1
			
			else:
				msg.linear.x = 0.2
				msg.angular.z = 0

		# if sonar3_x <= (x_dist/2) or sonar4_x <= (x_dist/2):
		# 	msg.linear.x = 0
		# 	msg.angular.z = 0.1
		# 	print '1'

		# elif sonar0_y <= (y_dist/2) or sonar15_y <= (y_dist/2):
		# 	msg.linear.x = 0
		# 	msg.angular.z = 0.1
		# 	print '2'

		# if sonar2_x <= (x_dist/2) or sonar5_x <= (x_dist/2):
		# 	msg.linear.x = 0
		# 	msg.angular.z = 0.1
		# 	print '3'

		# elif (((abs(sonar3_x) - abs(sonar11_x) <= 0.1) and (abs(sonar4_x) - abs(sonar12_x)))) <= 0.1 and ((abs(sonar0_y) - abs(sonar7_y))) <= 0.1:
		# 	msg.linear.x = 0
		# 	msg.angular.z = 0
		# 	print 'found center'
		# 	time.sleep(5)
		# 	flag += 1

		# else:
		# 	msg.linear.x = 0.2
		# 	msg.angular.z = 0
		# 	print '4'


# # #__________________________________________________________________

# # #Find exit


	if flag == 3:

		if (abs(sonar3_x) and abs(sonar4_x)) <= 5:
			msg.angular.x = 0
			msg.angular.z = 0.25
		elif (abs(sonar3_x) or  abs(sonar4_x)) <= 0.3:
			msg.angular.x = 0
			msg.angular.z = 0.25
		elif (abs(sonar5_x) or abs(sonar6_x)) <= 0.4:
			msg.linear.x = 0
			msg.angular.z = 0.4
		elif (abs(sonar1_x) or abs(sonar2_x)) <= 0.4:
			msg.linear.x = 0
			msg.angular.z = -0.4

		else:
			msg.linear.x = 0.3
			msg.angular.z = 0
			print 'exiting'

#__________________________________________________________________


#Works for specific scenario -- 2x2 square
#-------------------------------------------------------------------------
#	Find Center

# 	if flag == 0:

# 		if sonar3_x <= 1 or sonar4_x <= 1:
# 			msg.linear.x = 0
# 			msg.angular.z = 0.25

# 		elif sonar0_y <= 1 or sonar15_y <= 1:
# 			msg.linear.x = 0
# 			msg.angular.z = 0.25

# 		if sonar2_x <= 1 or sonar5_x <= 1:
# 			msg.linear.x = 0
# 			msg.angular.z = 0.25

# 		elif (abs(sonar3_x) - abs(sonar11_x)) <= 0.1 and (abs(sonar0_y) - abs(sonar7_y)) <= 0.1:
# 			msg.linear.x = 0
# 			msg.angular.z = 0
# 			print 'found center'
# 			time.sleep(5)
# 			flag += 1

# 		else:
# 			msg.linear.x = 0.2
# 			msg.angular.z = 0

# #-----------------------------------------------------------------------
# #	Find Exit

# 	if flag == 1:

# 		if abs(sonar3_x) and abs(sonar4_x) <= 4:
# 			msg.angular.x = 0
# 			msg.angular.z = 0.25

# 		else:
# 			msg.linear.x = 0.2
# 			msg.angular.z = 0			

#-----------------------------------------------------------------------


	pub.publish(msg)
	r.sleep()

if __name__ == '__main__':
	try:
		rospy.init_node('nodeProject1')
		r = rospy.Rate(20)
		pub = rospy.Publisher('/RosAria/cmd_vel', Twist, queue_size=1)
		msg = Twist()

		while not rospy.is_shutdown():
			rospy.Subscriber('/RosAria/sonar', PointCloud, callback)
			rospy.spin()

	except rospy.ROSInterruptException:
		pass