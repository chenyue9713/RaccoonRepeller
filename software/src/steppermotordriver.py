from periphery import GPIO
from time import sleep





base_motor_direction = GPIO("/dev/gpiochip0", 7, "out")
base_motor_step = GPIO("/dev/gpiochip0", 8, "out")
base_motor_cw = True # Clockwise Rotation
base_motor_ccw = False # Counterclockwise Rotation
base_motor_spr = 200 # Steps per Revolution (360 / 7.5)

base_motor_direction.write(base_motor_ccw)

base_motor_step_count = base_motor_spr

arm_motor_direction = GPIO("/dev/gpiochip2", 9, "out")
arm_motor_step = GPIO("/dev/gpiochip4", 10, "out")
arm_motor_cw = True # Clockwise Rotation
arm_motor_ccw = False # Counterclockwise Rotation
arm_motor_spr = 200 # Steps per Revolution (360 / 7.5)

arm_motor_direction.write(arm_motor_cw)

arm_motor_step_count = arm_motor_spr

delay = .0005

for x in range(base_motor_step_count):
    base_motor_step.write(True)
    sleep(delay)
    base_motor_step.write(False)
    sleep(delay)

for x in range(arm_motor_step_count):
    arm_motor_step.write(True)
    sleep(delay)
    arm_motor_step.write(False)
    sleep(delay)

sleep(.5)

base_motor_direction.write(base_motor_cw)
arm_motor_direction.write(arm_motor_ccw)

for x in range(base_motor_step_count):
    base_motor_step.write(True)
    sleep(delay)
    base_motor_step.write(False)
    sleep(delay)

for x in range(arm_motor_step_count):
    arm_motor_step.write(True)
    sleep(delay)
    arm_motor_step.write(False)
    sleep(delay)

sleep(.5)




base_motor_direction.close()
base_motor_step.close()
arm_motor_direction.close()
arm_motor_step.close()