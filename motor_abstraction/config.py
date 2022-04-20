import yaml
from importlib import import_module


def load(robot):

    # Load configuration
    with open(robot, "r") as stream:
        robot = yaml.safe_load(stream)

    # Initialize motors
    motors = []
    getmod = lambda module: import_module(f"motor_abstraction.{module}")
    for motor_config in robot.values():
        
        # Communication protocol
        _protocol_confg = {k: motor_config.pop(k) for k in motor_config.keys() & {'topic', 'freq', 'generate_bindings'}}
        _protocol_class = getattr(getmod('communicator'), f"{motor_config.pop('protocol')}")
        # Motor class
        _motor_class    = getattr(getmod(motor_config.pop('manufacturer')), motor_config.pop('model'))
        # Initialize
        _protocol       = _protocol_class(**_protocol_confg)
        _motor          = _motor_class(protocol=_protocol, **motor_config)

        motors.append(_motor)

    return motors
