#!/bin/bash
docker run -it --rm \
-h p3dx \
--device /dev/ttyUSB0 \
--privileged -v /dev/bus/usb:/dev/bus/usb \
--net host \
-v $(pwd)/src/p3dx_2dnav:/root/catkin_ws/src/p3dx_2dnav \
--env ROS_IP=$(ifconfig wlp2s0 | sed -En -e 's/.*inet addr:([0-9.]+).*/\1/p') \
--env ROS_MASTER_URI=http://$(ifconfig wlp2s0 | sed -En -e 's/.*inet addr:([0-9.]+).*/\1/p'):11311/ \
p3dx:navigation
