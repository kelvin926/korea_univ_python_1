'''
<4번> - 우유병이 있다. 이 병에 담긴 물을 똑같은 양으로 나누어 몇명이 마실 수 있는지 궁금하다.
N명이 마시려면 몇 병이 필요한지도 궁금하다.
병의 크기와 잔의 용량은 가변적이라고 가정하자.
어떤 길이 정보가 필요한지를 파악하여 물의 부피와 물 잔의 개수 등을 계산하는 프로그램을 작성하시오
'''

# 2021271424 장현서 - 파이썬 과제 210516 제출. github: @kelvin926
# 4번 코드
w = float(input("가로 길이는? :" ))
d = float(input("세로 길이는? :" ))
h = float(input("높이 길이는? :" ))
v = w*d*h
p = int(input("몇 사람이 나눠마실 예정? : "))
print("1병기준으로, {}명이 {}ml씩 나눠 마실 수 있습니다.".format(p, v//p))

need_p = int(input("사람 수는? : "))
cup = float(input("잔의 크기는? (ml) : "))
if (need_p*cup) <= v:
    print("{}명이 가득 채운 잔으로 1인 1잔을 마신다고 하였을 때, 1병이 필요합니다.".format(need_p))
else:
    i=2
    while True:
        if(need_p*cup) <= (i*v):
            break
        else:
            i+=1
    print("{}명이 가득 채운 잔으로 1인 1잔을 마신다고 하였을 때, {}병이 필요합니다.".format(need_p, i))