from copy import deepcopy as dc


def mjbots(robot):
    # ----------------------- test
    # mjbots = [robot.pop(name).pop('class') for name, config in dc(robot).items() if 'mjbots' in robot[name]['class'].__module__]
    # print(mjbots)
    # print(robot)
    # # ----------------------- test
    get_mjbots = lambda param: [config[param] for config in robot.values() if 'mjbots' in config['class'].__module__]
    transport  = moteus_pi3hat.Pi3HatRouter(
        servo_bus_map={
            get_mjbots('bus_id'): get_mjbots('motor_id'),
        },
    )
    mjbots = [robot.pop(name).pop('class')(**config) for name, config in dc(robot).items() if 'mjbots' in robot[name]['class'].__module__]

    return mjbots
