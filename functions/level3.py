#write a function that takes in a list of int and returns true if it contains 007 in order
#game([1,2,4,0,0,7,5])----true
#game([1,7,2,0,4,5,0])----false
#game([1,0,2,4,0,5,7])-----true
'''def game(nums):
    code=[0,0,7,'x']
    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code)==1
print(game([1,2,4,0,0,7,5]))   
print(game([1,2,4,0,5,7,5]))     
print(game([1,0,2,4,0,5,7]))'''

#write a function that returns the no. of prime no. that exist upto and including given no.
#by convention 0 and 1 not prime
def countprime(num):
    if num<2:
        return 0
    primes = [2]
    x=3
    while x<=num:
        for y in range(3,x):
            if x%y==0:
                x+=1
                break
                
            else:
                continue
        primes.append(x)
        x+=1
    print(primes)
    return len(primes) 
print(countprime(10))                