"""
Abstract Motor Control Loop
===========================
"""

import time
import asyncio
import itertools
import numpy as np

from hopping_leg.utils.init import arrinit, varget


async def motor_control_loop(motors, freq, T):

    # Zero
    for motor in motors:
        await motor.zero()

    # Indicate initialization
    print("initialization complete")

    # Runtime variables
    i            = 0
    meas_dt      = 0.0
    meas_time    = 0.0
    vel_filtered = 0
    n            = int(T*freq)
    t_iter       = 0
    t_elapsed    = 0
    t_start = time.time()

    # Record variables
    motor_ids   = [motor.motor_id for motor in motors]
    state_vars  = ['pos', 'vel', 'tau']
    record_src  = ['des', 'msr']
    record      = arrinit(np.empty(n), motor_ids, state_vars, record_src)    

    # Control loop
    while i < n:
        _t         = time.time()
        t_elapsed += t_iter

        # control and record state -------------------------
        # listen
        for motor in motors:
            _des = await motor.listen()
            record.update(dict(zip(varget(record, motor.motor_id, 'des'), _des)))
        # command
        for motor in motors:
            _msr = await motor.command()
            record.update(dict(zip(varget(record, motor.motor_id, 'msr'), _msr)))
        # -----
        # command
        # for motor in motors:
        #     _des, _msr = await motor.command()
        #     record.update(dict(zip(varget(record, motor.motor_id, 'des'), _msr)))
        #     record.update(dict(zip(varget(record, motor.motor_id, 'msr'), _msr)))
        # control -----------------------------------------

        i += 1
        t_iter = time.time() - _t

    t_end = time.time()

    # Disable motors
    
    return record, t_start, t_end, t_iter
