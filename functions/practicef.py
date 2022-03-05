#to check if both given no. are even or odd and return min no. if both are even else return max of two
def func(a,b):
    if a%2==0 and b%2==0:
        print(min(a,b))
    else:
        print(max(a,b))    

func(2,15)
func(2,6)
r=int(input('enter first no'))
s=int(input('ener second no.'))
func(r,s)