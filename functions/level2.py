'''#given a string print a string in which every letter repeats thrice
def func(mystr):
    result=''
    for char in mystr:
        result+= char*3

    print(result)
mystr='suraj' 
func(mystr)   '''
  
#return the sum  no. in array except all element between 6 and 9 if present



def sum(arr):
    total=0
    add=True  #note: t should be capital in true
    for num in arr:
        while add:
            if num!=6:
                total+=num
                break
            else: 
                add=False
        while not add:
            if num!=9:
                break
            else:
                add=True
                break
    return total
list=[2,6,5,9,4,5]
print(sum(list))
