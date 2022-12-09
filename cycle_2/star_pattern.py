def pattern(n):
	for x in range(n+1):
		for y in range(x):
			print ("*",end=" ")
		print("\n")
	for x in range(n-1,0,-1):
		for y in range(x):
			print("*",end=" ")
			print("\n")

n=int(input("Enter a number"))
pattern(n)


