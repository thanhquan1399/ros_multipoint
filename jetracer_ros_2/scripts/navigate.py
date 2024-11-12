#!/usr/bin/env python
# encoding: utf-8

import rospy
from move_base_msgs.msg import *
from actionlib_msgs.msg import GoalID
from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray
from geometry_msgs.msg import PointStamped, PoseStamped, PoseWithCovarianceStamped, Point



def navigate_to_table_cb(msg):
    point1 = Point()
    point2 = Point()
    my_msg = msg
    
    point1.x = my_msg.markers[0].pose.position.x
    rospy.loginfo(my_msg)
    

if __name__ == '__main__':
    rospy.init_node('navigate_to_table')
    my_msg = MarkerArray()
    pub = rospy.Publisher("/test", MarkerArray,  queue_size=100 )
    sub = rospy.Subscriber("/path_point", MarkerArray, callback = navigate_to_table_cb)
    
    rospy.loginfo("Node has been started.")
    
    rospy.spin()

