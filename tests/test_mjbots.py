import asyncio

import sys
sys.path.append('../motor_abstraction')

from motor_abstraction.config import load

motor_1 = load('tests/robot_mjbots.yml')

async def main():
    await motor_1.stop()
    await motor_1.state()

print("ASYNCIO")

asyncio.run(main())

print("DONE")
