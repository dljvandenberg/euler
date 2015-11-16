#!/usr/bin/env python
#
# Description: this program determines the product abc such that a^2+b^2=c^2, a<b<c natural numbers with a+b+c=n
# File: 009-pythagoreantriplet.py
# Author: Dennis van den Berg
# Date: 2012/01/30
# Version: 0.3


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

def pythagoreanproduct(n):
	for a in range(1,n//3):
		if (n*(n-2*a)) % (2*(n-a)) == 0:
			b=n*(n-2*a)/(2*(n-a))
			c=n-(a+b)
			print "a:",a
			print "b:",b
			print "c:",c
			return a*b*c


###
# Run
###

print pythagoreanproduct(n)
