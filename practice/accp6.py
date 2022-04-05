'''def LargeSmallSum(arr)

The function accepts an integers arr of size ’length’ as its arguments you are required to return the sum of second largest  element from the even positions and second smallest from the odd position of given ‘arr’

Assumption:

All array elements are unique
Treat the 0th position as even
NOTE

Return 0 if array is empty
Return 0, if array length is 3 or less than 3
Example

Input

arr:3 2 1 7 5 4

Output

7

Explanation

Second largest among even position elements(1 3 5) is 3
Second smallest among odd position element is 4
Thus output is 3+4 = 7
Sample Input

arr:1 8 0 2 3 5 6

Sample Output

8'''


def secondsmallestodd(arr,m):
    if m<=3:
        return 0
    else:    
        j=1
        max2=0
        l3=[]
        while j<m:
            l3.append(arr[j])
            j+=2  
        big=max(l3)
        l3.remove(big)
            
        big2=max(l3)   
        return big2    
    
def secondlargesteven(arr,m):
    if m<=3:
        return 0
    else:
        
        j=0
        
        l3=[]
        while j<m:
            l3.append(arr[j])
            j+=2  
        big=max(l3)
        l3.remove(big)
            
        big2=max(l3)   
        return big2
    
n=int(input('no. of elements of array'))
i=0
s1=set()
for i in range(0,n):
    a=int(input('enter an element'))
    s1.add(a)
arr=list(s1) 
m=len(arr)
p=secondsmallestodd(arr,m)
q=secondlargesteven(arr,m)
res=p+q
print(res)



