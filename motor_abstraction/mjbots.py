import math
import asyncio

import moteus

from motor_abstraction.abstract_motor import AbstractMotor
from motor_abstraction.utils.fallback import fallback_disable


class qdd100(AbstractMotor):

    # Motor characteristics
    torque_max = 12

    def __init__(self,
                 protocol,
                 transport,
                 kp, kd,
                 **kwargs):
        """
        **mjbots qdd100**
        """

        self.motor_id = motor_id

        # Communication protocol
        self.protocol = protocol

        # Driver        
        self.motor = moteus.Controller(id=motor_id, transport=transport)

        # Configuration
        self.kp_scale = kp/self.kp_default
        self.kd_scale = kd/self.kd_default
        self.torque_limit = max(kwargs.pop('torque_limit'), TestMotor.torque_max) if 'torque_limit' in kwargs.keys() else TestMotor.torque_max

        # Rest state
        if 'rest_state' in kwargs.keys():
            self.rest_state(kwargs['rest_state'])

        # Lock motor in place
        self.disable()

    @fallback_disable("enabling motor")
    async def enable(self):
        self.motor.enable_motor()

    @fallback_disable("zeroing motor")
    def zero(self):
        """
        Zero at current motor position
        """
        pass

    @fallback_disable("reading motor state")
    async def state():
        return await self.motor.set_position(position=math.nan,
                                             query=True)
    
    @fallback_disable("sending command")
    async def command(self, u):
        return await self.motor.set_position(position=u[0], 
                                             velocity=u[1], 
                                             feedforward_torque=u[2],
                                             stop_position=self.x_r,
                                             kp_scale=self.kp_scale, 
                                             kd_scale=self.kd_scale,
                                             maximum_torque=self.torque_limit, 
                                             watchdog_timeout=None, 
                                             query=True)

    @fallback_disable("setting rest position")
    async def rest(self):
        return self.command([None, None, 0])

    async def disable(self):
        return await self.motor.set_stop()
