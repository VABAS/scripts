#!/usr/bin/python3
from sys import argv

def _from_string (names_string):
    return nameformatter(names_string.split(", "))

def nameformatter (names):
    arr = []
    for name in names:
        name = name.split(" ")
        arr.append(name[len(name) - 1][0].upper() + name[len(name) - 1][1:].lower() + ", " + name[0][0].upper())

    arr.sort()
    ret = ""
    if len(arr) > 1:
        ret = "., ".join(arr[:len(arr) - 1])
        ret += ". & " + arr[len(arr) - 1]
    else:
        ret = arr[0]
    return ret

if __name__ == "__main__":
    argv.pop(0)
    print(_from_string(" ".join(argv)))

