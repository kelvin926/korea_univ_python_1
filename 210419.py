import random
import time

Y = 0
X = 0

cnt = int(input("몇번할까요?"))
while cnt != 0:
    a= random.randint(3,9)
    b= random.randint(3,9)
    if a ==5 or b ==5:
        continue

    cnt -= 1
    print("%d * %d은?" %(a,b))
    starts = time.time()
    right = int(input())
    finishs = time.time()
    print("%.1f 초만에 답을 하셨습니당" %(starts-finishs))

    if right == a*b:
        Y += 1
        print("맞아요!\n")
    else:
        X += 1
        print("틀렸어요!\n")

print("%d번중 %d번 맞았어요!" %(Y+X, Y))