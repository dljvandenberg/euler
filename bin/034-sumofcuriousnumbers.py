#!/usr/bin/env python
#
# Description: this program determines the sum of all curious numbers. A number n consisting of digits n_1, n_2, .. n_imax (imax>1) is called curious if \Sigma_{i=0}^{imax(n)} n_i! = n and n \elem \N
# File: 034-sumofcuriousnumbers.py
# Author: Dennis van den Berg
# Date: 2012/02/01
# Version: 0.2


import sys, math



###
# Define functions
###

# numlength(n) determines the number of digits (excluding decimals) of a positive number n.
def numlength(n):
	return math.floor(math.log(n,10)+1)

def curiousq(n):
	nlist=list(map(int,str(n)))
	return sum(map(math.factorial,nlist))==n

def curiouslist():
	clist=[]
	n=10
	while numlength(n)*math.factorial(9)>=n:
		if curiousq(n):
			clist[len(clist):]=[n]
		n+=1
	return clist


###
# Run
###

print sum(curiouslist())
