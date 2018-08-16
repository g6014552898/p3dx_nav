#!/usr/bin/env python

import movetest

# goal position on map [px, py, oz, ow]
goal_pos = [
            [0.0, 3.5, 0.0, 1.0],     # start point
            [-0.7, 0.7, -0.7, 0.7],    # door area
            # [-3.4, -0.65, 0.0, 1.0],   # lab door
            [-0.7, 7.0, 0.7, 0.7],    # walk way A
            [-0.7, 11.0, 0.7, 0.7],    # walk way B
            # [-5.0, 12.7, 1.0, -0.1],   # lift hall 
            # [-9.5, 9.3, -0.7, 0.7],   # table A 
            # [-9.5, 13.3, -0.7, 0.7],  # table B
            # [-5.3, 12.0, -0.1, 1.0],   # lift hall
            # [-0.7, 11.0, -0.7, 0.7],   # walk way B
            [-0.7, 7.0, -0.7, 0.7],   # walk way A
            [-0.7, 3.0, -0.7, 0.7],   # walk way C
            [-0.7, 0.7, -0.7, 0.7],    # door area
            [0.0, 3.5, 0.0, 1.0]       # start point
            ]
if __name__ == '__main__':
    
    movetest.main(goal_pos)