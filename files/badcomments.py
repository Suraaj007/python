with open('sample.txt') as f:
    content= f.read()

content=content.replace('donkey','beepbeep')

with open('sample.txt','w') as f:
    f.write(content)
