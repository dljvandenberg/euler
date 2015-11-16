#!/usr/bin/env python
#
# Description: this program determines the sum of the digits of the number n!
# File: 020-factorialdigitsum.py
# Author: Dennis van den Berg
# Date: 2012/02/01
# Version: 0.1


import sys, math

# Check arguments
if len(sys.argv) != 2:
	sys.exit("Must provide 1 natural number as argument")

# Convert the argument from string into number
n = int(sys.argv[1])
if n < 1:
	sys.exit("Argument is smaller than 1.")


###
# Define functions
###

def digitsum(n):
	return sum(list(map(int,str(n))))


###
# Run
###

print digitsum(math.factorial(n))
