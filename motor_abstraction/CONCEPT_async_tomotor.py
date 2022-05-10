timer = now


while True:

    time = time()

    if time is freq_comm:

        await read_command()
        await send_command()

    if time is freq_state:

        await communicate_state()
