#!/usr/bin/env python
#
# Description: This program determines the next triangular number greater than 40755 that is also pentagonal and hexagonal
# 	       where triangular numbers are defined by: T_i=i*(i+1)/2, i /elem /N
#	       pentagonal numbers by: P_j=j*(3*j-1)/2, j /elem /N
#	       and hexagonal numbers by: H_k=k*(2*k-1), k /elem /N
# File: 048-powersumlastdigits.py
# Author: Dennis van den Berg
# Date: 2012/02/01
# Version: 0.1


import sys, math



###
# Define functions
###

# nextnumber(N) determines the next triangular number greater than N that is also pentagonal and hexagonal
def nextnumber(N):
	n=N+1
	while not (math.sqrt(8*n+1)%2==1 and math.sqrt(24*n+1)%6==5 and math.sqrt(8*n+1)%4==3):
		n+=1
	print "i", (-1./2. + (1./2.)*math.sqrt(8*n+1))
	print "j", (1./2. + (1./2.)*math.sqrt(24*n+1))/3.
	print "k", (1./2. + (1./2.)*math.sqrt(8*n+1))/2.
	return n

# fasternextnumber(N) determines the next triangular number greater than N that is also pentagonal and hexagonal
def fasternextnumber(N):
	n=N+1
	k=math.ceil((1./2. + (1./2.)*math.sqrt(8*n+1))/2.)
	n=k*(2*k-1)
	while not (math.sqrt(8*n+1)%2==1 and math.sqrt(24*n+1)%6==5 and math.sqrt(8*n+1)%4==3):
		k+=1
		n=k*(2*k-1)
	print "i", (-1./2. + (1./2.)*math.sqrt(8*n+1))
	print "j", (1./2. + (1./2.)*math.sqrt(24*n+1))/3.
	print "k", (1./2. + (1./2.)*math.sqrt(8*n+1))/2.
	return n


###
# Run
###

print fasternextnumber(40755)
# print fasternextnumber(1)
# print nextnumber(40755)
