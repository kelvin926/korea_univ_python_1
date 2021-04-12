import random
print("숫자 맞추기 게임")
computer_win = 0
player_win = 0
name = str(input("너의 이름은 뭐니? : "))
print("반가워 {}. 내가 1부터 30까지의 숫자를 가지고 있어. 맞춰봐".format(name))
while(1):
    ansNum = random.randint(1,100)
    for i in range(5):
        gussNum = int(input("1~100 사이의 숫자 입력: "))
        if ansNum == gussNum:
            print(i+1,"번에 맞췄습니다.")
            # print("숫자는 {} 입니다.".format(gussNum))
            print("숫자는",gussNum,"입니다.")
            print("{}. 너가 당신이 이겼습니다.".format(name))
            player_win += 1
            break
        elif ansNum < gussNum:
            print("입력한 숫자가 큽니다")
        elif gussNum < ansNum:
            print("입력한 숫자가 작습니다")
    if ansNum == gussNum:
        pass
    else:
        print("컴퓨터가 이겼습니다")
        computer_win += 1
    gogo = str(input("계속 하시겠습니까? (y / n) : "))
    if(gogo == 'y'):
        continue
    elif(gogo == 'n'):
        break
    else:
        print("잘못된 값을 입력하였습니다. 게임을 종료합니다")
        break
print("게임을 종료합니다.")
print(name,"은(는)",player_win, "번 이겼고, 컴퓨터는",computer_win,"번 이겼습니다.")
# print("플레이어는{}번 이겼고, 컴퓨터는{}번 이겼습니다.".format(player_win, computer_win))