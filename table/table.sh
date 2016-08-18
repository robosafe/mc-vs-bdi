#!/bin/bash

rm ~/catkin_ws/stats.txt
rm /tmp/a1out*
rm /tmp/a2out*
rm /tmp/a3out*
rm /tmp/a4out*
rm /tmp/a5out*
rm /tmp/a6out*
rm /tmp/robot*
rm /tmp/human*
rm /tmp/sensors*
rm ~/catkin_ws/assertion*

cd ~/catkin_ws
(roscore & echo $! >> /tmp/mainpids) &
(sleep 5; roslaunch table_simulator bert2_gazebo.launch & echo $! >> /tmp/mainpids) &
(sleep 10; roslaunch bert2_moveit move_group.launch & echo $! >> /tmp/mainpids) &


COUNTER=1
while [ $COUNTER -lt 161 ]; do
	sleep 15
	rm -f /tmp/rospids

	(rosrun table_simulator object.py & echo $! >> /tmp/rospids) &
	(rosrun table_simulator pressure.py & echo $! >> /tmp/rospids) &
	(rosrun table_simulator sensors.py $COUNTER>> /tmp/sensors$COUNTER & echo $! >> /tmp/rospids) &
	(rosrun table_simulator voice_commands.py & echo $! >> /tmp/rospids) &
	(rosrun table_simulator human_g.py & echo $! >> /tmp/rospids) &
	(rosrun table_simulator assertion1.py $COUNTER>> /tmp/a1out$COUNTER & echo $! >> /tmp/rospids) &
	(rosrun table_simulator assertion2.py $COUNTER>> /tmp/a2out$COUNTER & echo $! >> /tmp/rospids) &
	(rosrun table_simulator assertion3.py $COUNTER>> /tmp/a3out$COUNTER & echo $! >> /tmp/rospids) &
	(rosrun table_simulator assertion4.py $COUNTER>> /tmp/a4out$COUNTER & echo $! >> /tmp/rospids) &
	(rosrun table_simulator assertion5.py $COUNTER>> /tmp/a5out$COUNTER & echo $! >> /tmp/rospids) &
	(rosrun table_simulator assertion6.py $COUNTER>> /tmp/a6out$COUNTER & echo $! >> /tmp/rospids) &
	(coverage run src/table_simulator/scripts/robot.py $COUNTER>> /tmp/robotout$COUNTER & echo $! >> /tmp/rospids) &
	(rosrun table_simulator human.py stimulus_$COUNTER $COUNTER >> /tmp/humanout$COUNTER) &
#	(rosrun table_simulator human.py abstract_test$COUNTER $COUNTER >> /tmp/humanout$COUNTER) &
	(sleep 300; cat /tmp/rospids | xargs kill -INT)
	sleep 10
	coverage html -d covhtml
	python src/table_simulator/scripts/check_code_coverage.py
	
        let COUNTER=COUNTER+1 
done

cat /tmp/mainpids | xargs kill 
