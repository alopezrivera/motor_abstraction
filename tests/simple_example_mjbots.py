import asyncio
import moteus
import moteus_pi3hat
import time


async def main():
    print("Motor Enabled.")
    # motor id and bus number mapping
    transport = moteus_pi3hat.Pi3HatRouter(
        servo_bus_map={
            bus_number: [motor_id],
        },
    )
    controller = moteus.Controller(id=motor_id, transport=transport)
    print(f'controller: id={controller.id}')
    # ,, kd={controller.pid_dq.kd}, ki={controller.pid_dq.ki} ')
    # print(f'kp={controller.pid_position.kp}')
    print(controller.__dict__.keys())

    if input('continue?') == 'y':
        while True:
            # To send a raw CAN, you must manually instantiate a
            # 'moteus.Command' and fill in its fields, along with which
            # bus to send it on.
            raw_message = moteus.Command()
            raw_message.raw = True
            raw_message.arbitration_id = 0x0405
            raw_message.bus = 1
            raw_message.data = b'1234'
            raw_message.reply_required = False

            # A single 'transport.cycle' call's message list can contain a
            # mix of "raw" frames and those generated from
            # 'moteus.Controller'.
            #
            # If you want to listen on a CAN bus without having sent a
            # command with 'reply_required' set, you can use the
            # 'force_can_check' optional parameter.  It is a 1-indexed
            # bitfield listing which additional CAN buses should be
            # listened to.

            results = await transport.cycle([
                raw_message,
                controller.make_query(),
            ], force_can_check = (1 << 5))

            # If any raw CAN frames are present, the result list will be a
            # mix of moteus.Result elements and can.Message elements.
            # They each have the 'bus', 'arbitration_id', and 'data'
            # fields.
            #
            # moteus.Result elements additionally have an 'id' field which
            # is the moteus servo ID and a 'values' field which reports
            # the decoded response.
            for result in results:
                if hasattr(result, 'id'):
                    # This is a moteus structure.
                    print(f"{time.time():.3f} MOTEUS {result}")
                else:
                    # This is a raw structure.
                    print(f"{time.time():.3f} BUS {result.bus}  " +
                        f"ID {result.arbitration_id:x}  DATA {result.data.hex()}")

            await asyncio.sleep(1.0)


if __name__ == '__main__':
    bus_number = 2
    motor_id = 5     
    asyncio.run(main())