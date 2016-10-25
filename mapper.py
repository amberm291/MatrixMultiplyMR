#!/usr/bin/env python

import sys
row_a = 5
col_b = 5

for line in sys.stdin:
	matrix_index, row, col, value = line.rstrip().split(",")
	if matrix_index == "a":
		for i in xrange(col_b):
			key = row + "," + str(i)
			print "%s\t%s\t%s"%(key,col,value)
	else:
		for j in xrange(row_a):
			key = str(j) + "," + col 
			print "%s\t%s\t%s"%(key,row,value)
