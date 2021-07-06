x=input('你的數學成績=')
y=input('你的英文成績=')
x=int(x)
y=int(y)
if x>=90 and y>=90:
    print('獲得獎品')
elif x<90 and y<90:
    print('要處罰')
else:
    print('再加油')
    