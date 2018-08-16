#!/bin/bash
docker run -it --rm \
-h ros \
--device /dev/ttyUSB0 \
--privileged -v /dev/bus/usb:/dev/bus/usb \
--net host \
-v $(pwd)/src/teleop_twist_keyboard:/root/catkin_ws/src/teleop_twist_keyboard \
--env ROS_IP=$(ifconfig wlp2s0 | sed -En -e 's/.*inet addr:([0-9.]+).*/\1/p') \
--env ROS_MASTER_URI=http://$(ifconfig wlp2s0 | sed -En -e 's/.*inet addr:([0-9.]+).*/\1/p'):11311/ \
p3dx:navigation \
/bin/bash -c "source ~/catkin_ws/devel/setup.bash && rosrun teleop_twist_keyboard teleop_twist_keyboard.py"
