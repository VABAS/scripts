#!/usr/bin/python3

from sys import argv
from sys import exit

def converter(mod, to_conv):
    modes = {
            "nothing":lambda x: x,
            "milestokm":lambda x: x * 1.609344,
            "kmtomiles":lambda x: x / 1.609344,
            "fttom":lambda x: x / 3.2808,
            "mtoft":lambda x: x * 3.2808,
            "ctof":lambda x: x * 1.8 + 32,
            "ftoc":lambda x: (x - 32) / 1.8,
            "ktoc":lambda x: x + 273.15,
            "ctok":lambda x: x - 273.15,
            "kmhtoms":lambda x: x / 3.6,
            "mstokmh":lambda x: x * 3.6,
            "lbtokg":lambda x: x / 0.45359237,
            "kgtolb":lambda x: x * 0.45359237,
            "oztog":lambda x: x / 0.035274,
            "gtooz":lambda x: x * 0.035274,
    }
    return modes[mod](to_conv)

if __name__ == "__main__":
    if len(argv) <= 2:
        print("Not enough arguments!")
        print("Usage: " + argv[0] + " mod to_conv")
        exit()

    print(converter(argv[1], int(argv[2])))

