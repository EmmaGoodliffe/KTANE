from _74hc595 import get_controls
from gpiozero import Button
from time import sleep
from wires_target import get_wires_target

def get_pin_num(pin_str):
    return int(str(pin_str)[4:])

def create_target(buttons, colours, serial):
    on_buttons = filter(lambda b: b.value == 1, buttons)
    pins = [get_pin_num(b.pin) for b in on_buttons]
    target = get_wires_target(pins, colours, serial)
    return target

def setup_wires(wires, colours, serial, success, error):
    buttons = [Button(x) for x in wires]
    target = create_target(buttons, colours, serial)

    def check_wires(device):
        pin = get_pin_num(device.pin)
        print("Removed pin", pin)
        current = []
        for button in buttons:
            if button.value == 1:
                current.append(get_pin_num(button.pin))
        sleep(0.5)
        is_still_on = device.value == 1
        if is_still_on:
            print("cancelled")
            return
        if current == target:
            print("Success")
            success()
        elif pin in target:
            print("Error")
            error()
        else:
            raise Exception("Something went wrong")

    for button in buttons:
        button.when_released = check_wires