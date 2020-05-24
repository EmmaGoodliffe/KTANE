from gpiozero import DigitalOutputDevice
from time import sleep

def get_controls(r, u, d):
    record = DigitalOutputDevice(r)
    update = DigitalOutputDevice(u)
    dataInput = DigitalOutputDevice(d)
    return record, update, dataInput

def set_outputs_with_string(b, r, u, d, num = 8):
    bits = b[::-1]
    while len(bits) < num:
        bits = '0' + bits
    print(bits)
    for bit in bits:
        if bit == '0':
            d.off()
        elif bit == '1':
            d.on()
        else:
            raise Exception('Not all the characters of the binary were 0 or 1')
        r.on()
        r.off()
    u.on()
    u.off()

def gen_find_button(r, u, d, digital, trigger_button):
    def find_button():
        for n in range(8):
            string = ''.join(['0' for _ in range(n)])
            string += '1'
            set_outputs_with_string(string, r, u, d)
            if digital.value == 1:
                set_outputs_with_string('11111111', r, u, d)
                trigger_button(n)
                return
        print('nothing was returned')
    return find_button