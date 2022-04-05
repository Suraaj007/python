'''Problem Description :

The function accepts two positive integers ‘r’ and ‘unit’ and a positive integer array ‘arr’ of size ‘n’ as its argument ‘r’ represents the number of rats present in an area, ‘unit’ is the amount of food each rat consumes and each ith element of array ‘arr’ represents the amount of food present in ‘i+1’ house number, where 0 <= i

Note:

Return -1 if the array is null
Return 0 if the total amount of food from all houses is not sufficient for all the rats.
Computed values lie within the integer range.
Example:

Input:

r: 7
unit: 2
n: 8
arr: 2 8 3 5 7 4 1 2
Output:

4'''

r=int(input('r\t')) 
unit=int(input('unit\t'))
n=int(input('enter no of element in array\t'))
foodneed=(r*unit)
arr=[]
for i in range(0,n):
    a=int(input('eneter  a no\t'))
    arr.append(a)
if arr==0:
    print("-1")
elif sum(arr)<foodneed:
    print('0')
else:
    count=0
    sum=0
    for j in range(0,n):
        count+=1
        sum+=arr[j]
        if sum>=foodneed:
            print(count)
            break
        else:
            continue
            