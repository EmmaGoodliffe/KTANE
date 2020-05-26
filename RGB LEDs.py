from _74hc595 import get_controls, set_outputs_with_string
from gpiozero import RGBLED

r, u, d = get_controls(4, 5, 6)
set_outputs_with_string('111', r, u, d)

rgb = RGBLED(14, 13, 12)
rgb.color = (1, 1, 1)