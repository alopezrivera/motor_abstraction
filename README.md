# Motor Abstraction

## TODO

- `communicator`
  - replace by LCM communication object
- `abstract_motor`
  - inherit from communicator
  - async communication methods
    - wrap *tmotor* methods in async communication routine -> unified async API for tmotor, mjbots
- `abstract-motor_loop`
  - complete integration with `abstract_motor`
  - tests
- Hardware tests