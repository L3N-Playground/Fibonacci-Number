#Fibonacci number

#Fibonacci number definition:
#F(n) = 0  for n=0
#F(n) = 1  for n=1
#F(n) = F(n-1)+F(n-2)  for n>1



def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

for i in range (0,30):
    print(fib(i))


