#!/bin/python

import sys

def print_formatted(number):
    length = len(bin(number)[2:])

    for i in range(1, number + 1):
        decimal = str(i).rjust(length)
        octal = oct(i)[2:].rjust(length)
        hexal = hex(i)[2:].upper().rjust(length)
        binary = bin(i)[2:].rjust(length)

        
        print (decimal, octal, hexal, binary)
        
        