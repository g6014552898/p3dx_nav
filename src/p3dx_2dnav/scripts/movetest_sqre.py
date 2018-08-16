#!/usr/bin/env python

import movetest
# goal position on map [px, py, oz, ow]
goal_pos = [
            [1.0, 0.0, 0.7, 0.7], 
            [1.0, 1.0, 1.0, 0.01], 
            [0.0, 1.0, -0.7, 0.7], 
            [0.0, 0.0, 0.0, 1.0]
            ]

if __name__ == '__main__':
    
    movetest.main(goal_pos)
