#!/usr/bin/env python
import rospy
from sensor_msgs.msg import PointCloud2
import sensor_msgs.point_cloud2 as pc2
import numpy as np
import ros_numpy

def init_subscribers():
    rospy.Subscriber('/camera/depth_registered/points', PointCloud2, on_new_point_cloud)

def on_new_point_cloud(data):
    pc = ros_numpy.numpify(data)
    points=np.zeros((pc.shape[0],3))
    points[:,0]=pc['x']
    points[:,1]=pc['y']
    points[:,2]=pc['z']
    
    print(points)
    
def listener():
    rospy.init_node('pcl_test_1', anonymous=True)
    init_subscribers()
    rospy.spin()
    

if __name__ == "__main__":
    listener()