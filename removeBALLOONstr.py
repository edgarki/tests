# A string S consisting of uppercase English letters is given. In one move we can delete seven 
# letters from S, forming the word "BALLOON" (one 'B', one 'A', two 'L's, two 'O's and one 'N'),
# and leave a shorter word in S. If the remaining letters in the shortened S are sufficient to
# allow another instance of the word "BALLOON" to be removed, next move can be done. What is 
# the maximum number of such moves that we can apply to S? Write a function: def solution(S) 
# that, given a string S of length N, returns the maximum number of moves that can be applied.
# Examples: 
# 1. Given S = "BAONXXOLL", the function should return 1. 
# 2. Given S = "BAOOLLNNOLOLGBAX", the function should return 2. 
# 3. Given S = "QAWABAWONL", the function should return 0. 
# 4. Given S = "ONLABLABLOON", the function should return 1. 
# Write an efficient algorithm for the following assumptions: N is an integer within the 
# range [1..200,000]; string S consists only of uppercase letters (A−Z). 


def level(S,x):
	n = 0
	new = S
	for i in range(len(S)):
		if n == 7:
			return new
		for j in range(len(x)):
			if new.find(x[j]) < 0:
				return S
			new = new.replace( x[j], '' , 1 )
			n += 1
			if n == 7:
				break
	
	return new


def solution(S):
	x = 'BALLOON'
	new = S

	z = 0
	while len(new) > 6:
		new = level(new,x)
		z += 1
		
		if new is S:
			z -= 1
			break
	
	return z
