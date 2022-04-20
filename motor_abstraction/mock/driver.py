class TestDriver:

    """
    Test Motor Driver
    """

    def __init__(self, can_port, motor_id):
        pass

    def enable_motor(self, raise_error=False):
        if raise_error:
            raise Exception("Test exception")

    def send_deg_command(self, u, raise_error=False):

        print(u)

        if raise_error:
            raise Exception("Test exception")

    def send_rad_command(self, u, raise_error=False):

        print(u)

        if raise_error:
            raise Exception("Test exception")

    def disable_motor(self, raise_error=False):
        if raise_error:
            raise Exception("Test exception")