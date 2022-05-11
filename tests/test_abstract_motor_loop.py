import asyncio

from motor_abstraction.abstract_motor_loop.abstract_motor_loop import motor_control_loop


def test_abstract_control_loop():

    class _motor:

        def __init__(self, motor_id):
            self.motor_id = motor_id

        async def zero(self):
            print(f"{self.motor_id} :: zeroed")

        async def listen(self):
            print(f"{self.motor_id} :: listened")
            return 1, 2, 3
        
        async def command(self):
            print(f"{self.motor_id} :: command executed")
            return 1.1, 2.1, 3.1

    motors = [_motor(id) for id in ['hip', 'knee', 'ankle']]

    record, t_start, t_end, t_iter = asyncio.run(motor_control_loop(motors, 10, 5))

    print(record)

test_abstract_control_loop()