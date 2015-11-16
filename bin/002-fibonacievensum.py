#!/usr/bin/env python
#
# Description: this program determines the sum of all even Fibonaci numbers: sum f[k] where f[k]<=n, f[k] even and k natural number. Where Fibonaci numbers are defined by: f[0]=0; f[1]=1; f[k]=f[k-2]+f[k-1] for k>=2
# File: 002-fibonacievensum.py
# Author: Dennis van den Berg
# Date: 2012/01/02, revised 2013/02/03
# Version: 0.2


# Max n
n=4000000

# Starting at k=1
fkmin1=0
fk=1
evensum=0

# 
k=2
while fk+fkmin1<=n:
	fkprevious=fk
	fk+=fkmin1
	fkmin1=fkprevious
	if fk%2==0:
		evensum=evensum+fk
	print "k:", k, " fk:", fk, " evensum:", evensum
	k+=1

print "evensum for max fk =",n,": ", evensum
