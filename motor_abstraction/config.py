import yaml
import moteus
from copy import deepcopy as dc
from importlib import import_module


def load(robot):

    # Load configuration
    with open(robot, "r") as stream:
        robot = yaml.safe_load(stream)

    # Process motor configs
    getmod = lambda module: import_module(f"motor_abstraction.{module}")
    
    for config in robot.values():
        
        # Communication protocol
        _protocol_confg        = {k: config.pop(k) for k in config.keys() & {'topic', 'freq', 'generate_bindings'}}
        _protocol_class        = getattr(getmod('communicator'), f"{config.pop('protocol')}")
        config['protocol'] = _protocol_class(**_protocol_confg)
        # Motor class
        config['class']    = getattr(getmod(config.pop('manufacturer')), config.pop('model'))

    ##################################
    # Motor-specific post-processing #
    ##################################

    # mjbots
    # ----------------------- test
    # mjbots = [robot.pop(name).pop('class') for name, config in dc(robot).items() if 'mjbots' in robot[name]['class'].__module__]
    # print(mjbots)
    # print(robot)
    # ----------------------- test
    get_mjbots = lambda param: [config[param] for config in robot.values() if 'mjbots' in config['class'].__module__]
    transport  = moteus_pi3hat.Pi3HatRouter(
        servo_bus_map={
            get_mjbots('bus_id'): get_mjbots('motor_id'),
        },
    )
    mjbots = [robot.pop(name).pop('class')(**config) for name, config in dc(robot).items() if 'mjbots' in robot[name]['class'].__module__]

    

    # for conf in motor_configs:
    #     print('mjbots' in conf['class'].__module__)

    ##################################
    #        Initialize motors       #
    ##################################
    # motors = [conf.pop('class')(**conf) for conf in motor_configs]

    return motors
