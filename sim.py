#PA Assignment 2
#Stefan Taylor
#s1006260
import sys
import math

readmisses = 0.0
writemisses = 0.0
totalmisses = 0.0
total = 0.0
readtotal = 0.0
writetotal = 0.0

filename = "gcc_memref.out"#raw_input("Please enter the name of the trace file: ")
cachesize = 32#int(raw_input("Please enter the size of the cache (in KB): "))
linesize = 64#int(raw_input("Please enter the size of the cache lines (in Bytes): "))
cachelines = cachesize * 1024 / linesize
cache = [[0]] * cachelines #initialise list to model the cache


offsetbits = int(math.log(linesize, 2))
indexbits = int(math.log(cachelines, 2))

with open(filename, 'r') as f:
	for line in f:
		total += 1
		line = (line.strip()).split()
		p = line[0]
		i = line[0]
		m = line[1]
		hexaddr = int(m, 16)
		binaddr = bin(hexaddr)[2:].zfill(32)
		offset = binaddr[-offsetbits:]
		index = int(binaddr[-(offsetbits+indexbits):-offsetbits],2)
		tag = binaddr[:-(offsetbits+indexbits)]
		
		if i == "R":
			readtotal+=1
		elif i == "W":
			writetotal+=1
		if cache[index] != tag:
			if i == "R":
				readmisses+=1
			elif i == "W":
				writemisses+=1
			totalmisses+=1
			cache[index]=tag
			

			
print("Total Miss Rate = " + str(totalmisses/total*100) + " %")
print("Write Miss Rate = " + str(writemisses/writetotal*100) + " %")
print("Read Miss Rate = " + str(readmisses/readtotal*100) + " %")

print("done")

		
		
