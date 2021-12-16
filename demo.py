from simple_pid import PID
import time

pid = PID(5, 0, 0, setpoint=60)
pid.sample_time = 0.1
pid.output_limits = (0, 100)


class water:
    def __init__(self) -> None:
        self.val = 0

    def update(self, delta, dt):
        if delta > 0:
            self.val += delta * dt
        return self.val


cs = water()
v = cs.update(0, 0)

start_time = time.time()
last_time = start_time
while time.time() - start_time < 10:
    control = pid(v)

    current_time = time.time()
    dt = current_time - last_time
    last_time = current_time

    v = cs.update(control, dt)
    print("__val: {} __delta: {}\n--------------".format(cs.val, control))
