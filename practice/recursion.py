#factorial using recursion
def fact(num):
    if num ==1:
        return num
    else:
        a=num*fact(num-1)
        return a


ans=fact(int(input('enter a no')))
print(ans)

'''#factorial using while loop
i=1
fact=1
n=20
while i<=n:
    fact=fact*i
    i+=1
print(fact)'''    