########## RECURSION #########

# In  recursion base condition and recursive relation is most important.
# In Base condition it is important to write return statement.

####### Factorial ######

def fact(n):
	if n == 0:
		return 1
	return n * fact(n-1)
a = fact(4)
print(a)

