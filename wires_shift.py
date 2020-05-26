from _74hc595 import get_controls, collect_values
from gpiozero import DigitalInputDevice
from time import sleep

def setup(r_p, u_p, d_p, dig_pin, target):
    r, u, d = get_controls(r_p, u_p, d_p)
    digital = DigitalInputDevice(dig_pin)
    first_values = collect_values(r, u, d, digital)

    def run(prev):
        values = collect_values(r, u, d, digital)
        if values[target] == 0:
            return values, True
        for i in range(len(values)):
            if prev[i] == 1 and values[i] == 0:
                return values, False
        return values, None
    
    return run, first_values
    
# index.py
TARGET = 1
wires_run, wires_state = setup(4, 5, 6, 12, TARGET)
while True:
    wires_state, wires_success = wires_run(wires_state)
    print(wires_success)
    sleep(1)