#!/usr/bin/env python
#
# Description: this program calculates the largest prime factor of a natural number N 
# File: 003-largestprimefactor.py
# Author: Dennis van den Berg
# Date: 2012/01/02
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

def smallestfactoratleastk(n,k):
	print "Determining smallest factor of", n, "starting at", k
	i=k
	while n%i != 0 and i*i <= n:
		i+=1
	if i*i > n:
		p = n
	else:
		p = i
	print "Found factor:", p, ". Remaining factor:", n/p
	return p

def largestprimefactoratleastk(n,k):
	p = smallestfactoratleastk(n,k)
	if p == n:
		return n
	else:
		return largestprimefactoratleastk(n/p,p)

def largestprimefactor(n):
	print "Determining largest prime factor of", n
	p = largestprimefactoratleastk(n,2)
	print "Largest prime factor is:", p


###
# Run
###

largestprimefactor(n)
