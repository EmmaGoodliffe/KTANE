from _74hc595 import get_controls
from gpiozero import Button

def get_pin_num(pin_str):
    return int(str(pin_str)[4:])

def setup_wires(WIRES, TARGET, success, error, progress):
    buttons = [Button(x) for x in WIRES]

    def check_wires(device):
        pin = get_pin_num(device.pin)
        print("Removed pin", pin)
        current = []
        for button in buttons:
            if button.value == 1:
                current.append(get_pin_num(button.pin))
        if current == TARGET:
            print("Success")
            success()
        elif pin in TARGET:
            print("Error")
            error()
        else:
            print("Progress")
            progress()

    for button in buttons:
        button.when_released = check_wires