#multiplication table
n=int(input('enter a no. to get its table'))
list1=[n*i for i in range(1,11)]
print(list1)

with open("table.txt","a") as f:  #a means append mode
    f.write(str(list1))
    f.write('\n')