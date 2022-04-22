import yaml
from copy import deepcopy as dc
from importlib import import_module

from motor_abstraction.config.postprocessing import mjbots


def load(robot):

    # Load configuration
    with open(robot, "r") as stream:
        robot = yaml.safe_load(stream)

    # Process motor configs
    getmod = lambda module: import_module(f"motor_abstraction.{module}")
    for config in robot.values():
        # Communication protocol
        _protocol_confg    = {k: config.pop(k) for k in config.keys() & {'topic', 'freq', 'generate_bindings'}}
        _protocol_class    = getattr(getmod('communicator'), f"{config.pop('protocol')}")
        config['protocol'] = _protocol_class(**_protocol_confg)
        # Motor class
        config['class']    = getattr(getmod(config.pop('manufacturer')), config.pop('model'))

    ##################################
    # Motor-specific post-processing #
    ##################################
    # mjbots
    _mjbots = mjbots(robot)

    #################################
    #       Initialize motors       #
    #################################
    motors = [conf.pop('class')(**conf) for conf in robot.values()]

    return motors
