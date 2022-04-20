from abstract_motor import AbstractMotor
from utils.fallback import fallback_disable

from TEST_driver import TestDriver


class TestMotor(AbstractMotor):

    """
    Test motor class
    """

    # Motor characteristics
    torque_max = 12

    def __init__(self,
                 protocol,
                 can_port, motor_id, 
                 kp, kd,
                 **kwargs):

        self.motor_id = motor_id

        # Driver
        self.motor = TestDriver(can_port, motor_id)
        
        # Communication protocol
        self.protocol = protocol

        # Configuration
        self.kp = kp
        self.kd = kd
        self.torque_limit = max(kwargs.pop('torque_limit'), TestMotor.torque_max) if 'torque_limit' in kwargs.keys() else TestMotor.torque_max

        # Rest state
        if 'rest_state' in kwargs.keys():
            self.rest_state(kwargs['rest_state'])

    @fallback_disable("enabling motor")
    def enable(self):
        self.motor.enable_motor()
    
    @fallback_disable("zeroing motor")
    def zero(self):
        """
        Zero at current motor position
        """
        pass
    
    @fallback_disable("setting rest state")
    def rest(self):
        return self.motor.send_deg_command(self.x_r)
    
    @fallback_disable("sending command")
    def command(self, u, raise_error=False):
        return self.motor.send_rad_command(u, raise_error=raise_error)

    def disable(self):
        self.motor.disable_motor()
