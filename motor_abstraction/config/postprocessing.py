import sys
import logging
import traceback

from copy import deepcopy as dc
from importlib import import_module

from motor_abstraction.utils.shout import shout_error


def mjbots(robot):
    """
    mjbots motor configuration

    1. Create transport with all 
    """

    if any(['mjbots' in config['class'].__module__ for config in robot.values()]):

        # Retrieve motor parameters of all mjbots motors
        get_mjbots = lambda param: [config[param] for config in robot.values() if 'mjbots' in config['class'].__module__]

        # Transport configuration
        assert isinstance(get_mjbots('bus_id')[0], int)
        servo_bus_map = {get_mjbots('bus_id')[0]: get_mjbots('motor_id')}

        # Create transport
        try:
            raspy_router = import_module('moteus_pi3hat')
        except ModuleNotFoundError:
            shout_error('missing moteus_pi3hat')
            logging.error(traceback.format_exc())
            sys.exit()
        transport  = raspy_router.Pi3HatRouter(
            servo_bus_map=servo_bus_map,
        )

        # Initialize motors
        mjbots = [robot.pop(name).pop('class')(**{**config, **{'transport': transport}}) for name, config in dc(robot).items() if 'mjbots' in robot[name]['class'].__module__]

        return mjbots

    return []
