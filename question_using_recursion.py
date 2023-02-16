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















