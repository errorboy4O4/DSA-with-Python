####### Power Of 2 ###### 
##### Using Recursion ######


def power(n):
	if n == 0:
		return 1
	return 2 * power(n-1)
a = power(5)
print(a)


####### Print Counting ###### 
##### Using Recursion ######

def counting(n):
	if n == 0:
		return 
	print(n)
	return counting(n-1)	
a = counting(5)
print(a)   



####### FIBONACCI NUMBER ###### 
##### Using Recursion ######

def fib(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	return fib(n-1) + fib(n-2)
a = fib(4)
print(a)

########### Count Ways To Climb N Stairs ################
##### Using Recursion ######


def cwtns(n):
	if n < 0:
		return 0
	if n == 0:
		return 1
	return cwtns(n-1) + cwtns(n-2)

a = cwtns(5)
print(a)


########### SORT A ARRAY ################
##### Using Recursion ######


arr = [1,2,3,3,3]
def sortrecur(arr):
	n = len(arr)
	if n == 0 or n == 1:
		return True
	if arr[0] > arr[1]:
		return False
	else:
		return sortrecur(arr[1:])
if sortrecur(arr):
	print('Array is Sorted')
else:
	print("Array is not Sorted")



########### SUM OF AN ARRAY  ################
##### Using Recursion ######


arr = [1,2,3,3,3]
def sumrecur(arr):
	n = len(arr)
	if n == 0:
		return 0
	if n == 1:
		return arr[0]
	remainingpart = sumrecur(arr[1:])
	return arr[0] + remainingpart
# a = sumrecur(arr)
# print(a)








