#!/usr/bin/python
import sys
def BinaryTo4BitSection(input):
    # This function divides binary number provided as argument to this script 
    # into four bit sections (this of course works for any string but is 
    # intended for mentioned use). Returns the formatted value.
    start = len(input)%4
    # Initializing the final string
    final=""
    # Loop to add the spaces in required places
    i=0
    while i<len(input):
        final+=input[i]
        if (i+1)%4==start:
            final+=" "
        i+=1

    return final

if __name__ == "__main__":
    if len(sys.argv)!=2:
        sys.exit("Usage: "+sys.argv[0]+" [binary number]")
    input = sys.argv[1]
    print BinaryTo4BitSection(input)