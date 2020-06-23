# SPI must be enabled

from busio import SPI as SPI_BUS
from digitalio import DigitalInOut as ChipSelect
from board import SCK, MISO, MOSI, D5 as GPIO5
from adafruit_mcp3xxx.mcp3008 import MCP3008, P0
from adafruit_mcp3xxx.analog_in import AnalogIn
from time import sleep

VOLTAGE_INPUT = 3.3

def get_adc(cs_pin, channel_num):
    spi = SPI_BUS(clock=SCK, MISO=MISO, MOSI=MOSI)
    cs = ChipSelect(cs_pin)
    mcp = MCP3008(spi, cs)
    channel = AnalogIn(mcp, channel_num)
    return channel

adc = get_adc(GPIO5, P0)

while True:
    position = VOLTAGE_INPUT / adc.voltage
    position = int(position * 10) / 10 # ?
    boundary1 = 1.5
    boundary2 = 3.0
    if position < boundary1:
        print(0)
    elif position < boundary2:
        print(1)
    else:
        print(2)
    sleep(1)
