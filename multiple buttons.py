from gpiozero import DigitalInputDevice
from _74hc595 import get_controls, set_outputs_with_string, gen_find_button

# set up 74HC595
r, u, d = get_controls(5, 6, 7)
set_outputs_with_string('11111111', r, u, d)

digital = DigitalInputDevice(8)
digital.when_activated = gen_find_button(r, u, d, digital, print)