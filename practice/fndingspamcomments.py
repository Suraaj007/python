l=['make a lot of money', 'buy now', 'subscribe this','click this']
i=input('enter a comment here\n')
for item in l:
  if item==i:
    print('its a spam!')
    break
  else:
    pass
else:
  print('its not a  spam!')