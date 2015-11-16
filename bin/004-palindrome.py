#!/usr/bin/env python
#
# Description: this program determines the largest palindromic number made from the product of 2 numbers smaller than or equal to n
# File: 004-palindrome.py
# Author: Dennis van den Berg
# Date: 2012/01/03
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

# Incorrect standard functions used. Look up correct version!
def checkpalindromic(n):
	s = str(n)
	return bool(s[::-1] == s)

# Find largest palindromic number made from the product of 2 numbers smaller than or equal to n
def largestpalindromic(n):
	if n < 1:
	        sys.exit("Argument is smaller than 1.")
	p = 1
	i = n
	while i > 0:
		j = n
		while j >= i and i*j > p:
			if checkpalindromic(i*j):
				p = i*j
			j+=-1
		i+=-1
	return p

###
# Run
###

print largestpalindromic(n)

