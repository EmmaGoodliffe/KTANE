from wires import setup_wires
from pygame import mixer
from random import randint

# Serial number
serial = "A1"

# Music
mixer.init()
mixer.music.set_volume(0.2)

# Wires
WIRES = [4, 5, 6, 12, 13, 14]
WIRE_COLOURS = {
    4: "red", # orange
    5: "blue", # green
    6: "blue",
    12: "white", # grey
    13: "blue", # purple
    14: "yellow"
}
def wires_success():
    mixer.music.load('sound/wires/progress' + str(randint(1, 2)) + '.mp3')
    mixer.music.play()
def wires_error():
    print(':(')
setup_wires(WIRES, WIRE_COLOURS, serial, wires_success, wires_error)