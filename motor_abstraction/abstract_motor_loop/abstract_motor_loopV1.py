"""
Abstract Motor Control Loop
===========================
"""

def _control():
    pass

def motor_control_loop(motors, controller, controller_params):

    # Zero

    # Indicate initialization

    # Runtime variables
    i            = 0
    meas_dt      = 0.0
    meas_time    = 0.0
    vel_filtered = 0
    t_start = time.time()

    # Control loop
    while i < n:
        _t         = time.time()
        t_elapsed += t_iter

        # _control() -----------------------------------------
        des_pos, des_vel, des_tau = control_method.get_control_output(meas_pos, 
                                                                      vel_filtered, 
                                                                      meas_tau,
                                                                      meas_time)
        # Placeholder values
        if des_pos is None:
            des_pos = 0
            kp = 0
        if des_vel is None:
            des_vel = 0
            kd = 0
        # Clip torque
        if des_tau > control_tau_max:
            des_tau = control_tau_max
        if des_tau < -control_tau_max:
            des_tau = -control_tau_max
        # Control
        meas_pos, meas_vel, meas_tau = motor_01.send_rad_command(des_pos, 
                                                                 des_vel, 
                                                                 kp, 
                                                                 kd, 
                                                                 des_tau)
        # Filter velocity
        if i > 0:
            vel_filtered = np.mean(data_dict["meas_vel_list"][max(0,
                                                                  i-10):i])
        else:
            vel_filtered = 0
        # Record data
        record = {}

        # _control() -----------------------------------------
        
        i += 1
        t_iter = time.time() - _t
        
        # Enforce control frequency
        if t_iter > dt:
            print("Control loop is too slow!")
            print("Control frequency:", 1/exec_time, "Hz")
            print("Desired frequency:", 1/dt, "Hz")
            print()
        while time.time() - _t < dt:
            pass

    t_end = time.time()

    # Disable motors
    
    return record, t_start, t_end, t_iter