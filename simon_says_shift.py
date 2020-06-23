from _74hc595 import get_controls, gen_find_button
from gpiozero import DigitalInputDevice

def trigger_button(n, guess, target, leds):
    guess.append(n)
    i = len(guess) - 1
    led = leds.index(n)
    print('LED:', led)
    if guess == target:
        print('SUCCESS!')
    elif guess[i] != target[i]:
        guess = guess[0:i]
        print('ERROR!')
    else:
        print('PROGRESS!')

def setup(r_p, u_p, d_p, dig_pin, target, leds):
    r, u, d = get_controls(r_p, u_p, d_p)
    digital = DigitalInputDevice(dig_pin)
    digital.when_activated = gen_find_button(r, u, d, digital, trigger_button, [[], target, leds])

# index.py
TARGET = [0, 1]
LEDS_ENCRYPTION = [1, 0]
setup(4, 5, 6, 12, TARGET, LEDS_ENCRYPTION)
