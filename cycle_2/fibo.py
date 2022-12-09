#25.Fibonacci series
def fibo(a,b,n):
    a,b=b,a+b
    print(b,"\n")
    n-=1
    if n>2:
        fibo(a,b,n)
        
a,b=0,1
n=int(input("Enter the limit\n"))
print("Ther Fibonacci series is :\n")
print(a,"\n")
print(b,"\n")
fibo(a,b,n)
