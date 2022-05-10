import math
import asyncio
from synced_object.synced_object import LCMSyncedObject

import moteus

from abc import ABC, abstractmethod

from motor_abstraction.utils.shout import shout_disabled
from motor_abstraction.utils.fallback import fallback_disable
from motor_abstraction.utils.exceptions import SafetyException, ConfigurationError


class AbstractMotor(ABC):

    def __getattribute__(self, name):
        """
        **Override attribute retrieval.**

        Conduct motor configuration validation at attribute
        retrieval time, and apply boilerplate to communicate
        the motor's state after all commands and provide the
        user with logs.

        1. Motor configuration validation
            - Ensure motor instance has all required attributes
            - Ensure motor instance has a declared ``rest_state`` 
              before calling any function other than ``__init__`` 
              or ``rest_state``
        2. Function boilerplate
            - Push motor state via provided communication protocol after all motor commands
            - Log motor disabling
        """

        get = lambda obj, attr: super(ABC, obj).__getattribute__(attr)
            
        # Attempt to retrieve attribute from instance
        attribute = get(self, name)

        if callable(attribute):
            
            print(attribute)

            return attribute

    def __getattr__(self, name):
        """
        Handle requests for unknown attributes by diverting the request
        to the ``motor`` attribute of the class.
        """
        print("=======================")
        print(name)
        print("=======================")
        try:
            return self.__dict__['_retrieve'](name)
        except AttributeError:
            raise AttributeError(f"{self.__class__.__name__} has no attribute \"{name}\"")

    def _retrieve(self, name):
        """
        Retrieve attribute from the class' ``motor`` object.
        """
        return getattr(self.motor, name) 

    def _disable(self, fn_disable, *args, **kwargs):
        output = fn_disable(*args, **kwargs)
        shout_disabled(f'0x0{self.motor_id}')
        return output

    def _command(self, fn_command, *args, **kwargs):
        state = fn_command(*args, **kwargs)
        self.protocol.push(state)
        return state

    @abstractmethod
    def disable(self):
        """
        Disable motor
        """
        pass


class qdd100(LCMSyncedObject,AbstractMotor, moteus.Controller):

    def __init__(self, *args, **kwargs):
        self.kp = 1
        LCMSyncedObject.__init__(self)
        self.motor = moteus.Controller(*args, **kwargs)

        self.pull()
    def disable(self):
        pass


a = qdd100()
a.pull()