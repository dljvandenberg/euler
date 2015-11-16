#!/usr/bin/env python
#
# Description: this program determines the last d digits of the sum \Sigma_{i=1}^{k} i^i
# File: 048-powersumlastdigits.py
# Author: Dennis van den Berg
# Date: 2012/02/01
# Version: 0.1


import sys, math



###
# Define functions
###

# powersumlastdigits(k,d) determines the last d digits of the sum \Sigma_{i=1}^{k} i^i
def powersumlastdigits(k,d):
	summed=0
	for i in range(1,k+1):
		summed=(summed+i**i)
	return summed % 10**d


###
# Run
###

k=1000
d=10
print powersumlastdigits(k,d)
