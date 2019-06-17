# A computer system decides what packages are to be loaded on what trucks. All rooms and spaces are abstracted into space units which is represented as an integer. For each type of truck, they have different space units. For each package, they will be occupying different space units.
#As a software development engineer in sort centers, you will need to write a method. Given truck space units and a list of product space units, find out exactly TWO products that fit into the truck. You will also implement an internal rule that the truck has to reserve exactly 30 space units for safety purposes.
#
# Each package is assigned a unique ID, numbered from 0 to N-1.
# Assumptions: 
# 1. You will pick up exactly 2 packages. 
# 2. You cannot pick up one package twice.
# 3. If you have multiple pairs, select the pair with the largest package.
#
# Input
# The input to the function/method consists of two arguments 
# - truckSpace, an integer representing the truck space.
# - packagesSpace, a list of integers representing the space units occupying by packages.

# Output
# Return a list of integers representing the IDs of two packages whose combined space will leave exactly 30 space units on the truck.

# Example
#Input:
# - truckSpace = 90
# - packagesSpace = [1, 10, 25, 35, 60]
# Output: 
# [2, 3]
# Explanation:
# Given a truck of 90 space units, a list of packages space units [1, 10, 25, 35, 60], Your method should select the third(ID-2) and fourth(ID-3) package since you have to reserve exactly 30 space units.

# in (truckSpace packagesSpace) :
# 110 [20, 70, 90, 30, 60, 110]
# out:
# 0 4

def IDsOfPackages(truckSpace, packagesSpace):
    # WRITE YOUR CODE HERE
    #print  packagesSpace
    ava = truckSpace - 30
    #v = [20, 70, 90, 30, 60, 110]
    b = [0,0,0]
    for i in range(len(packagesSpace)):
    	for j in range(i,len(packagesSpace)):
    		if i == j:
    			continue
    		#print i,j
    		s = packagesSpace[i] + packagesSpace[j]
    		if s >= b[2] and s <= ava:
    			if s == b[2]:
    				if packagesSpace[b[0]] < packagesSpace[i] or packagesSpace[b[1]] < packagesSpace[j]:
    					b[0] = i
    					b[1] = j
    					b[2] = s
    			b[0] = i
    			b[1] = j
    			b[2] = s
    return [b[0],b[1]]
