x=[1,2,3]
for item in x:
    #kskskkks
    pass 

print('end of script')


mystring="sammy"
for letter in mystring:
    print(letter) #after performing print operation print directly moves to next line

for letter in mystring:
    if letter=='a':
        continue #go back to top now
    print(letter)

for letter in mystring :
    if letter == 'a':
        break
    print(letter)

m=0
while m<5:
    if m==2:
        break # you wiil be out of while loop go on a next line 
    print(m)
    m+=1






    
