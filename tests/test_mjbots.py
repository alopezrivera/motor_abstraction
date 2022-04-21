import sys
sys.path.append('../motor_abstraction')

from motor_abstraction.config import load

motor_1, motor_2 = load('tests/robot_mjbots.yml')

# Enable
motor_1.enable()
# Rest
motor_1.rest()
# Command
motor_1.command([1, 1, 1, 1, 1])
# Disable
motor_1.disable()


# motor_1.listen()