# TIAGo programming and simulation with ROS2 and Webots
## 1. Get acquainted with the environment
1. File > New > New Project Directory (and tick the add arena checkbox)
2. Select Rectangle Arena then floorSize and make it bigger
3. CTRL + Shift + A > PROTO Nodes (Webots Projects) > robots > pal_robotics > tiago > Tiago (robot) > Add

![First controller](https://github.com/dan-crdll/tiago_simulation_webots_ros2/blob/main/gifs/first_controller.gif?raw=true)

The added robot will already have a controller written in `C` that allows you to move the base if pressing arrow keys.

## 2. Building a first simple controller in Python
* File > New > New Robot Controller (and select Python)
A new Python script will be created under the `controllers` directory, I called it `simple_controller.py`.
Install `webots` python package with:
```bash
pip install webots
```
Then I can write the simple controller to move the robot base, the torso and the arm with keyboard.

![Simple controller](https://github.com/dan-crdll/tiago_simulation_webots_ros2/blob/main/gifs/simple_controller.gif?raw=true)
