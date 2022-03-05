#eg.madam ,mom,kayak,racecar

#remove spaces first

def pal(s):
    s=s.replace(' ','')
    if s==s[::-1]:
        print('palindrome')
    else:
        print('not palindrome')
           
    return s

s='kadak'
print(pal(s))



