from _74hc595 import get_controls, set_outputs_with_string

r, u, d = get_controls(5, 6, 7)
set_outputs_with_string('011', r, u, d)