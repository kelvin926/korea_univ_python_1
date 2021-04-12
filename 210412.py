import random
print("숫자 맞추기 게임")
while(1):
    ansNum = random.randint(1,30)
    for i in range(5):
        gussNum = int(input("1~30 사이의 숫자 입력: "))
        if ansNum == gussNum:
            print(i+1,"번에 맞췄습니다.")
            print("숫자는",gussNum,"입니다.")
            break
        else:
            if ansNum < gussNum:
                print("입력한 숫자가 큽니다")
            else:
                print("입력한 숫자가 작습니다")
    gogo = str(input("계속 하시겠습니까? (y / n) : "))
    if(gogo == 'y'):
        continue
    elif(gogo == 'n'):
        break
    else:
        print("잘못된 값을 입력하였습니다. 게임을 종료합니다")
        continue
print("게임을 종료합니다.")