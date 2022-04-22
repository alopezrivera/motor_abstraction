"""
Abstract Motor Class
====================
"""

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

        try:
            
            # Attempt to retrieve attribute from instance
            attribute = get(self, name)

            # if callable(attribute):
                
            #     # Ensure motor instance has all required attributes when
            #     # calling non-configuration and non-safety-critical methods.
            #     config_methods = ['__init__', 'rest_state']
            #     safety_methods = ['disable']
            #     allowed_methods = config_methods + safety_methods
                
            #     if name not in allowed_methods:
                    
            #         # Ensure motor instance has all required attributes
            #         req_attrs = ['motor', 'motor_id', 'protocol', 'kp', 'kd', 'torque_max']
            #         ins_attrs = {**get(self, '__dict__'), **get(self, '__class__').__dict__}.keys()
            #         for req_attr in req_attrs:
            #             try:
            #                 assert req_attr in ins_attrs
            #             except AssertionError:
            #                 msg = f"\"{name}\" has not been declared as a class or instance attribute for class {get(self, '__class__').__name__}."
            #                 add = "The following attributes must be set for AbstractMotor heiresses:"
            #                 lst = [f'{ra}' for ra in req_attrs]
            #                 raise ConfigurationError(msg, add, lst)

            #         # Ensure motor instance has a declared ``rest_state``
            #         if 'x_r' not in ins_attrs:
            #             msg = f"rest state has not been set for {get(self, '__class__').__name__} with motor ID \"0x0{self.motor_id}\"."
            #             add = f"The rest state must be set with \"{get(self, '__class__').__name__}.rest_state\" before calling any motor control method."
            #             raise SafetyException(msg, add)

            #     # Declare motor disabling
            #     if name == 'disable':
            #         return lambda *args, **kwargs: get(self, '_disable')(attribute, *args, **kwargs)

            #     # Push state 
            #     if name == 'command':
            #         return lambda *args, **kwargs: get(self, '_command')(attribute, *args, **kwargs)
                
            return attribute

        except AttributeError:
            # Picked up by __getattr__
            pass

    def __getattr__(self, name):
        """
        Retrieve unknown attributes from motor controller.
        """
        try:
            return getattr(self.__dict__['motor'], name)
        except AttributeError:
            raise AttributeError(f"{self.__class__.__name__} has no attribute \"{name}\"")

    def _command(self, fn_command, *args, **kwargs):
        state = fn_command(*args, **kwargs)
        self.protocol.push(state)
        return state

    def _disable(self, fn_disable, *args, **kwargs):
        output = fn_disable(*args, **kwargs)
        shout_disabled(f'0x0{self.motor_id}')
        return output

    def rest_state(self, x_r):
        """
        Set rest state
        """
        self.x_r = x_r

    @abstractmethod
    def __init__(self, motor_id, **kwargs):
        """
        **Abstract Motor Class**

        Required attributes:

        - ``motor_id``
          Motor ID (hexadecimal or otherwise). This is used both for
          low level communication and to refer to individual motors
          in communication with the user.

        Recommended attributes:

        - ``motor``
          Motor object containing methods for low-level motor control.
          It may be provided by the user or by a library. For further
          reference consider the T-Motor AK80-6 and AK80-9 interfaces 
          provided by `mini-cheetah-tmotor-python-can <https://github.com/dfki-ric-underactuated-lab/mini-cheetah-tmotor-python-can>`_ 
          (`pip <https://pypi.org/project/mini-cheetah-motor-driver-socketcan/>`_).
    
        """

        self.motor_id = motor_id

        self.motor = None

    @abstractmethod
    @fallback_disable("enabling motor")
    def enable(self):
        """
        Enable motor
        """
        pass

    @abstractmethod
    @fallback_disable("zeroing motor")
    def zero(self):
        """
        Zero at current motor position
        """
        pass

    @abstractmethod
    @fallback_disable("setting rest state")
    def rest(self):
        """
        Rest position command
        """
        pass

    @abstractmethod
    @fallback_disable("sending motor command")
    def command(self, u):
        """
        Motor command
        """
        pass

    @abstractmethod
    def disable(self):
        """
        Disable motor
        """
        pass