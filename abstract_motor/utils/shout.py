def shout_error(error):
    msg = f"| ERROR: {error} |"
    print(f'\n{"="*len(msg)}\n{msg}\n{"="*len(msg)}')


def shout_disabled(motor):
    msg = f"DISABLED MOTOR: {motor}"
    print(f'{"-"*len(msg)}\n{msg}\n{"-"*len(msg)}')
