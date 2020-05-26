def get_last_index(li, value):
    return len(li) - 1 - li[::-1].index(value)

def get_wires_target(pins, colours, serial):
    num = len(pins)
    colours_list = [colours[n] for n in pins]
    red_num = colours_list.count("red")
    last_colour = colours_list[-1]
    last_blue_wire_index = get_last_index(colours_list, "blue")
    serial_last_digit = int(serial[1])
    serial_last_digit_is_odd = serial_last_digit % 2 != 0
    blue_num = colours_list.count("blue")
    yellow_num = colours_list.count("yellow")
    black_num = colours_list.count("black")
    white_num = colours_list.count("white")
    to_cut = None
    if num == 3:
        if red_num == 0:
            to_cut = 2
        elif last_colour == "white":
            to_cut = 3
        elif blue_num > 1:
            to_cut = last_blue_wire_index
        else:
            to_cut = 3
    elif num == 4:
        if red_num > 1 and serial_last_digit_is_odd:
            to_cut = 4
        elif last_colour == "yellow" and red_num == 0:
            to_cut = 1
        elif blue_num == 1:
            to_cut = 1
        elif yellow_num > 1:
            to_cut = 4
        else:
            to_cut = 2
    elif num == 5:
        if last_colour == "black" and serial_last_digit_is_odd:
            to_cut = 4
        elif red_num == 1 and yellow_num > 1:
            to_cut = 1
        elif black_num == 0:
            to_cut = 2
        else:
            to_cut = 1
    elif num == 6:
        if yellow_num == 0 and serial_last_digit_is_odd:
            to_cut = 3
        elif yellow_num == 1 and white_num > 1:
            to_cut = 4
        elif red_num == 0:
            to_cut = 6
        else:
            to_cut = 4
    else:
        raise Exception("Must be between 3 and 6 wires")
    target = [*pins[0:to_cut - 1], *pins[to_cut:]]
    print(to_cut, target)
    return target