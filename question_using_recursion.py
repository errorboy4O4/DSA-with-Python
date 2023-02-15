####### Power Of 2 ###### 
##### Using Recursion ######


def power(n):
	if n == 0:
		return 1
	return 2 * power(n-1)
a = power(5)
print(a)
