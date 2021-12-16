from simple_pid import PID
import time


class agv:
    def __init__(self) -> None:
        self.x = 0

    def update(self, speed, dt):
        self.x += dt * speed
        return self.x


start_time = time.time()
last_time = start_time

agv = agv()
x = agv.update(0, 0)
pid = PID(5, 0, 0, setpoint=x)
pid.sample_time = 0.1
pid.output_limits = (0, 0.5)
while time.time() - start_time < 10:
    current_time = time.time()
    dt = current_time - last_time
    last_time = current_time

    controll = pid(x)
    x = agv.update(controll, dt)

    print("x: {} controll: {}".format(x, controll))

    # if have any new path
    if current_time - start_time > 2:
        pid.setpoint = 10
