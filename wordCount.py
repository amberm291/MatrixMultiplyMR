#!/usr/bin/python
import glob
import mincemeat

text_files = glob.glob('hw3data/*')

def file_contents(file_name):
	f = open(file_name)
	try:
		return f.read()
	finally:	
		f.close()
	
source= dict((file_name,file_contents(file_name))
		for file_name in text_files)

def mapfn(key, value):
	import re
	for line in value.splitlines():
        	wordsinsentence = line.split(":::")
        	authors = wordsinsentence[1].split("::")
               	words = str(wordsinsentence[2])
        	words = re.sub(r'([^\s\w-])+', '', words)
               	words = words.split(" ")
        	for author in authors:
            		for word in words:
                		word = word.replace("-"," ")
                		word = word.lower()
                		yield author, word

def reducefn(key, value):
	from collections import Counter
	return Counter(value)

s = mincemeat.Server()
s.datasource = source 
s.mapfn = mapfn
s.reducefn = reducefn
results = s.run_server(password="pass")
#print results
w = open('output.txt','w')
w.write(str(results))
w.close()
