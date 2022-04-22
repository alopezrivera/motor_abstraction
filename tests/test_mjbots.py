import asyncio
import sys
sys.path.append('../motor_abstraction')

from motor_abstraction.config import load

# import moteus
# import moteus_pi3hat

# async def main():
#     servo_bus_map = {2: [5]}
#     transport  = moteus_pi3hat.Pi3HatRouter(
#             servo_bus_map=servo_bus_map,
#         )
#     servo = moteus.Controller(id=5, transport=transport)
#     await servo.set_stop()

# print("ASYNCIO")

# asyncio.run(main())

motor_1 = load('tests/robot_mjbots.yml')

async def main():
    print("MAIN")
    print(motor_1.motor)
    print(motor_1.motor.__dict__.keys())
    print(motor_1.motor.id)
    await motor_1.motor.set_stop()

print("ASYNCIO")

asyncio.run(main())

print("DONE")

# Enable
# asyncio.run(motor_1.enable())
# print("TROIJAISDOAIS")
# Rest
# motor_1.rest()
# # Command
# motor_1.command([1, 1, 1, 1, 1])
# # Disable
# asyncio.run(motor_1.disable())


# motor_1.listen()