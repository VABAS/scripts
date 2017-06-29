#!/usr/bin/python
import sys
from BinaryTo4BitSection import BinaryTo4BitSection as BinaryTo4BitSection
def SectionsBit(bits,value):
    try:
        bits=int(bits)
    except ValueError:
        raise BaseException("Bits argument must be integer!")
    if len(value)%bits!=0:
        raise BaseException("Length of value must be dividable by bits number!")
    final=""
    value=BinaryTo4BitSection(value).split(" ")
    counter=0
    for section in value:
        final+=section+" "
        counter+=len(section)
        if counter%bits==0:
            final+="\n"
    return final
if __name__ == "__main__":
    if len(sys.argv)!=3:
        sys.exit("Usage: "+sys.argv[0]+" [bits/row] [binary number]")
    bits = sys.argv[1]
    value = sys.argv[2]
    print SectionsBit(bits,value)