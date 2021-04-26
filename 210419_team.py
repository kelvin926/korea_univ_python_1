import random
import time

Y = 0
X = 0
alist = []
blist = []
cnt = int(input("몇번할까요?"))
timeout = int(input("제한시간은?"))
while cnt != 0:
    a= random.randint(3,9)
    b= random.randint(3,9)
    alist.append(a)
    blist.append(b)
    
    if a ==5 or b ==5:
        continue
    
    elif ((alist.index(a)==1 and blist.index(b)==1) or (alist.index(a)==1 and blist.index(b)==1)):
        continue
    
    else:
        cnt -= 1
        print("%d * %d은?" %(a,b))
        starts = time.time()
        right = int(input())
        finishs = time.time()
        print("%.1f 초만에 답을 하셨습니당" %(finishs-starts))
        if ((finishs - starts) > timeout):
            print("제한시간 초과!, 답으로 인정되지 않습니다.")
            continue
        else:
            pass

        if right == a*b:
            Y += 1
            print("맞아요!\n")
        else:
            X += 1
            print("틀렸어요!\n")

print("%d번중 %d번 맞았어요!" %(Y+X, Y))