#Fibonacci number

#Fibonacci number definition:
#F(n) = 0  for n=0
#F(n) = 1  for n=1
#F(n) = F(n-1)+F(n-2)  for n>1



n = 30
#initialize
i = 0
fib = 0
f_1 = 0
f_2 = 0

while i <= n:
    if i == 0:
        f_1 = 0
        fib = f_1
    elif i == 1:
        f_2 = 1
        fib = f_2
    else:
        fib = f_1 + f_2
        f_1 = f_2
        f_2 = fib
    i += 1
    print(fib)


