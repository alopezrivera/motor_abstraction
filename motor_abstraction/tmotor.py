"""
T-Motor Motor Classes
=====================
"""

from motor_driver.canmotorlib import CanMotorController

from motor_abstraction.abstract_motor import AbstractMotor

from motor_abstraction.utils.fallback import fallback_disable


class ak80_6(AbstractMotor):

    def __init__(self, can_port, motor_id, **kwargs):
        """
        **T-Motor ak80-6**
        """

        self.motor_id = motor_id
        
        # Driver
        self.motor = CanMotorController(can_port, motor_id, **kwargs)

    def enable(self):
        self.motor.enable_motor()
    
    @fallback_disable("setting rest position")
    def rest(self):
        return self.motor.send_deg_command(self.x_r)
    
    @fallback_disable("sending command")
    def command(self, u):
        return self.motor.send_rad_command(u)

    def disable(self):
        self.motor.disable_motor()

# # Initialize
# motor_1 = ak80_6(can_port="can0", motor_id=0x00)
# # Rest state
# motor_1.rest_state([0, 0, 0, 0, 0])
# # Enable
# motor_1.enable()
# # Rest
# motor_1.rest()