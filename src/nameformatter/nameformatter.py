#!/usr/bin/python3
from sys import argv

def nameformatter (names):
    names = names.replace(",","").split(" ")
    arr = []
    for i in range(len(names)):
        if i % 2 == 0:
            arr.append(names[i + 1][0].upper() + names[i + 1][1:].lower() + ", " + names[i][0].upper())

    arr.sort()
    ret = "., ".join(arr[:len(arr) - 1])
    ret += ". & " + arr[len(arr) - 1] + "."
    return ret

if __name__ == "__main__":
    argv.pop(0)
    print(nameformatter(' '.join(argv)))

