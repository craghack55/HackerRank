#!/bin/python

import sys

def print_rangoli(size):
    
    for i in range(size, 0, -1):
        
        sys.stdout.write("-" * (size * 2 - 2 * (size - i + 1)))
        
        for j in range(size, i, -1):
            sys.stdout.write(chr(j + 96) + "-")
        
        sys.stdout.write(chr(i + 96))
        
        for j in range(i + 1, size + 1, 1):
            sys.stdout.write("-" + chr(j + 96))
        
        sys.stdout.write("-" * (size * 2 - 2 * (size - i + 1)))
        sys.stdout.write("\n")
        
    
    for i in range(2, size + 1, 1):
        
        sys.stdout.write("-" * ((i - 1) * 2))
        
        for j in range(size, i, -1):
            sys.stdout.write(chr(j + 96) + "-")
            
        sys.stdout.write(chr(i + 96))
        
        for j in range(i + 1, size + 1, 1):
            sys.stdout.write("-" + chr(j + 96))       
    
        sys.stdout.write("-" * ((i - 1) * 2))
        sys.stdout.write("\n")

