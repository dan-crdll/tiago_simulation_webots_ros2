from controller import Robot, Keyboard, Motor

robot = Robot()

timestep = int(robot.getBasicTimeStep())
keyboard = Keyboard()

# Get the motors for left and right wheels (differential drive base)
left_motor = robot.getDevice("wheel_left_joint")
right_motor = robot.getDevice("wheel_right_joint")

# Get motor of the torso lift
torso_motor = robot.getDevice("torso_lift_joint")
torso_V = torso_motor.getMaxVelocity()

# Get motor of the arm base
arm_motor_base = robot.getDevice("arm_1_joint")
arm_base_V = arm_motor_base.getMaxVelocity()

# Provide the initial state
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)
torso_motor.setVelocity(torso_V)
arm_motor_base.setVelocity(arm_base_V)

# Constant velocity
V = left_motor.getMaxVelocity()

keyboard.enable(timestep)
torso_v = 0
arm_base_v = (arm_motor_base.getMaxPosition() - arm_motor_base.getMinPosition())
while robot.step(timestep) != -1:
    key = keyboard.getKey()
    w_l = 0
    w_r = 0
    
    if key >= 0:
        if key == Keyboard.UP:
            w_l = V
            w_r = V
        elif key == Keyboard.LEFT:
            w_l = -V 
            w_r = V
        elif key == Keyboard.RIGHT:
            w_l = V 
            w_r = -V 
        elif key == Keyboard.DOWN:
            w_l = -V
            w_r = -V
        elif key == ord('W'):
            torso_v = torso_v + 0.001 if torso_v + 0.001 < torso_motor.getMaxPosition() else torso_motor.getMaxPosition()
        elif key == ord('S'):
            torso_v = torso_v - 0.001 if torso_v - 0.001 > torso_motor.getMinPosition() else torso_motor.getMinPosition() 
        elif key == ord('A'):
            arm_base_v = arm_base_v - 0.01 if arm_base_v - 0.01 > arm_motor_base.getMinPosition() else arm_motor_base.getMinPosition()
        elif key == ord('D'):
            arm_base_v = arm_base_v + 0.01 if arm_base_v + 0.01 < arm_motor_base.getMaxPosition() else arm_motor_base.getMaxPosition()

    left_motor.setVelocity(w_l)
    right_motor.setVelocity(w_r)
    torso_motor.setPosition(torso_v)
    arm_motor_base.setPosition(arm_base_v)
    
