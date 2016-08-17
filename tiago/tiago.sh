#!/bin/bash

#rosclean purge
rm ~/catkin_ws/stats.txt
rm ~/catkin_ws/assertion1.txt
rm ~/catkin_ws/assertion2.txt
rm ~/catkin_ws/assertion3.txt
rm /tmp/a1o*
rm /tmp/a2o*
rm /tmp/a3o*
rm /tmp/a4o*
rm /tmp/robot*
rm /tmp/human*
rm /tmp/sensor*
rm /tmp/dog*
#rm ~/catkin_ws/assertion*
rm /tmp/mainpids
rm /tmp/rospids

cd ~/catkin_ws

COUNTER=1
while [ $COUNTER -lt 51 ]; do
	
	rm /tmp/mainpids
	(roslaunch tiago_gazebo tiago_gazebo.launch & echo $! >> /tmp/mainpids) &

	sleep 15
	rm -f /tmp/rospids

	(rosrun tiago_gazebo sensors.py >> /tmp/sensors$COUNTER & echo $! >> /tmp/rospids) &
	(rosrun tiago_gazebo dog.py $COUNTER >> /tmp/dog$COUNTER & echo $! >> /tmp/rospids) &
	(rosrun tiago_gazebo assertion1.py $COUNTER >> /tmp/a1o$COUNTER & echo $! >> /tmp/rospids) &
	(rosrun tiago_gazebo assertion2.py $COUNTER >> /tmp/a2o$COUNTER & echo $! >> /tmp/rospids) &
	(rosrun tiago_gazebo assertion3.py $COUNTER >> /tmp/a3o$COUNTER & echo $! >> /tmp/rospids) &
	(rosrun tiago_gazebo assertion4.py $COUNTER >> /tmp/a4o$COUNTER & echo $! >> /tmp/rospids) &
	(coverage run src/tiago_simulation/tiago_gazebo/scripts/robot.py >> /tmp/robot$COUNTER & echo $! >> /tmp/rospids) &
	(sleep 5; rosrun tiago_gazebo human.py abstract_test$COUNTER $COUNTER >> /tmp/human$COUNTER & echo $! >> /tmp/rospids) &
#	(sleep 5; rosrun tiago_gazebo human.py stimulus_$COUNTER $COUNTER >> /tmp/human$COUNTER & echo $! >> /tmp/rospids) &
	(sleep 700; cat /tmp/rospids | xargs kill -INT)
	sleep 10
	coverage html -d covhtml
	python src/tiago_simulation/tiago_gazebo/scripts/check_code_coverage.py
	cat /tmp/mainpids | xargs kill
	sleep 30
        let COUNTER=COUNTER+1 
done


