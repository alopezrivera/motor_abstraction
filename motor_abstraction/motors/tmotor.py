"""
T-Motor Motor Classes
=====================
"""

from motor_driver.canmotorlib import CanMotorController

from motor_abstraction.abstract_motor import AbstractMotor

from motor_abstraction.utils.fallback import fallback_disable


class ak80_6(AbstractMotor):

    # Motor characteristics
    torque_max = 12

    def __init__(self,
                 protocol,
                 can_port, motor_id,
                 kp, kd,
                 **kwargs):
        """
        **tmotor ak80-6**
        """

        self.motor_id = motor_id

        # Communication protocol
        self.protocol = protocol

        # Configuration
        self.kp = kp
        self.kd = kd
        self.torque_limit = max(kwargs.pop('torque_limit'), ak80_6.torque_max) if 'torque_limit' in kwargs.keys() else ak80_6.torque_max

        # Rest state
        if 'rest_state' in kwargs.keys():
            self.rest_state(kwargs.pop('rest_state'))

        # Driver
        self.motor = CanMotorController(can_port, motor_id)

    def enable(self):
        self.motor.enable_motor()
    
    @fallback_disable("zeroing motor")
    def zero(self):
        """
        Zero at current motor position
        """
        pass
    
    @fallback_disable("sending command")
    def command(self, u):
        return self.motor.send_rad_command(u[0], u[1], self.kp, self.kd, u[2])

    @fallback_disable("setting rest position")
    def rest(self):
        return self.motor.send_rad_command(self.x_r)

    def disable(self):
        self.motor.disable_motor()
