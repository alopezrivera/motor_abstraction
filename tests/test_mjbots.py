import asyncio
import sys
sys.path.append('../motor_abstraction')

from motor_abstraction.config import load

motor_1 = load('tests/robot_mjbots.yml')

async def main():
    print("MAIN")
    print(motor_1.motor)
    print(motor_1.motor.__dict__.keys())
    print(motor_1.motor.id)
    # await motor_1.motor.set_stop()
    motor_1.disable()

print("ASYNCIO")

asyncio.run(main())

print("DONE")
