#!/usr/bin/env python
from nav_msgs.msg import OccupancyGrid
from nav_msgs.msg import Odometry
import rospy
import numpy as np
from matplotlib import pyplot as plt


def compute_cells(msg):
    if not msg:
        return 0

    num_unknown_cells = 0.0
    # print(msg.info)
    costmap = np.empty((msg.info.height, msg.info.width), dtype=np.int8)
    costmap.fill(-1)
    
    for row_h in range(msg.info.height):
        costmap[row_h] = msg.data[(row_h*msg.info.width):((row_h + 1)*msg.info.width)]
    # print(costmap)
    return costmap

def init_subscribers():
    # rospy.Subscriber('/move_base/global_costmap/costmap', OccupancyGrid, handle_occupancy_grid)
    rospy.Subscriber('/map', OccupancyGrid, handle_occupancy_grid)
    rospy.Subscriber('/odom', Odometry, handle_odometry)

def handle_occupancy_grid(msg):
    global map
    map = compute_cells(msg)

def handle_odometry(msg):

    print(msg.pose.pose)
    
    
def listener():
    rospy.init_node('map_test_1')
    init_subscribers()
    rospy.spin()
    

if __name__ == "__main__":
    listener()

    