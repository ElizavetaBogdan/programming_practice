v = int(input())
t=int(input())
if v>0:
    print((v*t)%109)
else:
    print(109-(abs(v)*t)%109)