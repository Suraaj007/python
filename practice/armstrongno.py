#153 is armstrong no. as 1*1*1 +(5*5*5)+(3*3*3)=153
print('Hello, world!')
n=53
x=53
print(n)
sum=0
m=len(str(n))
print(m)
for i in range(0,m):
    a=n%10
    sum=sum+(a*a*a)
    n=n//10
    print(sum)

print(sum)    
if sum == x:
  print('armstrong no.')
else:
  print('Not an armstrong no.')          