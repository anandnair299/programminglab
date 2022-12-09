def pattern(n):
	for x in range(n+1):
		i=x
		for y in range(x):
			print (i,end="\t")
			i=i*x
		print()

n=int(input("Enter a number"))
pattern(n)



			