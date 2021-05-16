'''
<7번> - 재미있는 주사위 게임 프로그램 ~~
'''

# 2021271424 장현서 - 파이썬 과제 210516 제출. github: @kelvin926
# 7번 코드
import random
lose_list = [2, 4, 6, 8]
re_list = [3, 5, 9, 10, 11, 12]
while True:
    print("주사위 굴러가유~")
    a1 = random.randint(1,6)
    a2 = random.randint(1,6)
    a_sum = a1 + a2
    print(a1, a2)
    if a_sum == 7:
        print("플레이어 승리!")
        break
    elif a_sum in lose_list:
        print("플레이어 패배!")
        break
    elif a_sum in re_list:
        print("다시 던집니다!")
        b1 = random.randint(1,6)
        b2 = random.randint(1,6)
        b_sum = b1 + b2
        print(b1, b2)
        if a_sum == b_sum:
            print("플레이어 승리!")
            break
        else:
            print("처음부터 주사위를 다시 던집니다!")
            continue