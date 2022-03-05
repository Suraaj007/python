#write a function that capitalize the first and fourth letter of a name
def func(name):
    mylist=[]
    for letter in name:
        mylist.append(letter)
    mylist[1]=mylist[1].upper()
    mylist[4]=mylist[4].upper()
    print(mylist)
    
    s= ''.join(mylist)
    #result=str(mylist)
    print(s)
name=' peakyfamily'
func(name)