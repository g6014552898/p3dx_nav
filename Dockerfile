FROM ros:kinetic-robot
# install ros  packages
RUN mkdir -p ~/catkin_ws/src && cd ~/catkin_ws/src && \
    /bin/bash -c "source /opt/ros/kinetic/setup.bash && catkin_init_workspace && \
    cd ~/catkin_ws && catkin_make" && ls && \
    cd ~/catkin_ws/src && \
    git clone https://github.com/amor-ros-pkg/rosaria.git && \
    apt-get update && apt-get install -y \
    ros-kinetic-openni2-launch ros-kinetic-navigation ros-kinetic-lms1xx libaria-dev && \
    cd ~/catkin_ws/ && ls && /bin/bash -c "source devel/setup.bash && catkin_make install" && \
    apt-get autoremove -y &&  rm -rf /var/lib/apt/lists/

