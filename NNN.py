#17. Accept an integer N, and compute N + NN + NNN 
n=int(input("Enter value of N"))
n=n+(n*10+n)+(n*100+n*10+n)
print("computed value is",n)
