#0 1 1 2 3 5 8 13 21 34 
#wap to print fib series upto n
i=0
n=10#input from user
sum=0

a=0
b=1
print(a,b, end=' ')
for i in range(0,n-2):
    sum=a+b
    print(sum, end=' ')
    a=b
    b=sum
