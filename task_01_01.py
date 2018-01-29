x = int(input())
if x % 100 == 0 and x % 400 > 0:
    print('no')
elif x % 4 > 0:
    print('no')
else:
    print('yes')
