f=open('poems.txt')
t=f.read()
if 'twinkle' in t:
    print('twinkle is present')
else:

    print('twinkle not present')  
f.close()

