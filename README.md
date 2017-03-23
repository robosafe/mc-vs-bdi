# mc-vs-bdi
Comparison BDI agents vs PTA model checking for test generation

Assumptions:
- ROS Indigo
- Gazebo v. 2.2.5
- MoveIt!
- Compatibility packages for ROS-Gazebo

Contents:
- Table assembly (cooperative manufacture) simulator (new version)
- Tiago (home care) simulator components (to be used in combination with the installation from: http://wiki.ros.org/Robots/TIAGo)
- Models: BDI, and PTA (with properties)
- Tests: BDI, MC (model checking), and PR (pseudorandom)
- Data: 
	- Assertion logs in the format: assertion<number>_<seed>.txt
	- X product logs in the format: x_product_<test generation type>.txt
	- Code coverage logs in the format: stats_<seed>.txt
	- Scripts used to plot and get the data out from log files
