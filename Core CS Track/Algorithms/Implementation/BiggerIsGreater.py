from itertools import permutations

def next_permutation(arr):
	# Find non-increasing suffix
	i = len(arr) - 1
	while i > 0 and arr[i - 1] >= arr[i]:
		i -= 1
	if i <= 0:
		return False
	
	# Find successor to pivot
	j = len(arr) - 1
	while arr[j] <= arr[i - 1]:
		j -= 1
	arr[i - 1], arr[j] = arr[j], arr[i - 1]
	
	# Reverse suffix
	arr[i : ] = arr[len(arr) - 1 : i - 1 : -1]
	return 

t = int(raw_input())

for i in range(t):
    w = raw_input()
    temp = set(w)
    sortedW = "".join(sorted(w, reverse = True))
    
    if len(temp) <= 1 or sortedW == w or len(w) == 1:
        print "no answer"
    else:
        temp = next_permutation(list(w))
        print "".join(temp)
        
        
        
        
