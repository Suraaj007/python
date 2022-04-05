n=12345
mul=1
while n>0 or mul>9:
    if n==0:
        n=mul
        mul=1
    mul=mul*(n%10) 
    n=n//10
print(mul)       