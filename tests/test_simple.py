import asyncio
import moteus_pi3hat

import sys
sys.path.append('../motor_abstraction')

from motor_abstraction.simple import qdd100

bus_number = 2
motor_id = 5
transport = moteus_pi3hat.Pi3HatRouter(servo_bus_map={
                                            bus_number: [motor_id],
                                        })

motor_1 = qdd100(id=motor_id, transport=transport)

async def main():
    await motor_1.set_stop()
    await motor_1.set_position(position=math.nan, query=True)

print("ASYNCIO")

asyncio.run(main())

print("DONE")
