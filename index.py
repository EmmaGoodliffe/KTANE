from wires import setup_wires
from pygame import mixer
from random import randint

# Music
mixer.init()
mixer.music.set_volume(0.2)

# Wires
WIRES = [4, 5, 6, 7, 8, 9]
WIRES_TARGET = [5, 6, 8]
def wires_success():
    print(':)')
def wires_error():
    print(':(')
def wires_progress():
    mixer.music.load('sound/wires/progress' + str(randint(1, 2)) + '.mp3')
    mixer.music.play()
setup_wires(WIRES, WIRES_TARGET, wires_success, wires_error, wires_progress)