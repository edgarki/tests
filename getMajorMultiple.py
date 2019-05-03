# Write a function: def solution(A) that, given an array A consisting of N integers, 
# returns the maximum among all integers which are multiples of 11. For example, 
# given array A as follows: [-6, -91, 1011, -100, 84, -22, 0, 1, 473] the function 
# should return 473. Assume that: 
# - N is an integer within the range [1..1,000]; 
# - each element of array A is an integer within the range [−10,000..10,000]; 
# - there is at least one element in array A which satisfies the condition in the task statement.

def solution(A):
    # write your code in Python 3.6
    max = -10000
    for i in range(len(A)):
        if A[i] < -10000 or A[i] > 10000:
            continue
        if A[i] % 11 == 0 and A[i] > max:
            max = A[i]
            
    return max
