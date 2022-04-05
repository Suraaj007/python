while True:
    print('press q to quit')
    a=input(' enter a no.')
    if a=="q":
        break
    try:
        print('trying')
        a=int(a)
        if a>6:
            print('you entered a no. greater than 6')
    except Exception as e:
        print(f'your input resulted an error  {e}')
print('Thanks for playing this game')





