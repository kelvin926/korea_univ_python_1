# import time
# print("[현재시각]", time.strftime("%H:%M:%S"))
# alarm_time = input("알람 시각 :")
# alarm_hms = alarm_time.split(":")
# if len(alarm_hms) == 3 and 0 <= int(alarm_hms[0]) \
#     and 0 <= int(alarm_hms[1]) and 0 <= int(alarm_hms[2]):
#         time.sleep(int(alarm_hms[0]) * 60 * 60 \
#             + int(alarm_hms[1]) * 60 + int(alarm_hms[2]))
#         for i in range(1, 10):
#             print("\a") # 맥북이라 알람을 그냥 비프음으로 했습니다.
# else:
#     print("입력한 알람 시각 표기에 오류가 있습니다")


value = 0
while True:
    print("\n 현재 값 :", value)
    line = input("작업 명령 입력 :")
    tokens = line.split()
    if len(tokens) > 0:
        operator = tokens[0]
        if len(tokens) == 1:
            if operator == 'x':
                break
            print("잘못된 작업 명령")
        elif len(tokens) == 2:
            operand = float(tokens[1])
            if operator == '=':
                value = operand
            elif operator == '+':
                value += operand
            elif operator == '*':
                value *= operand
            elif operator == '/' or operator == '%':
                if operand != 0:
                    if operator == '/':
                        value /= operand
                    else:
                        value %= operand
                else:
                    print("잘못된 작업 명령 (0으로 나누기)!!")
            else:
                print("잘못된 작업 명령!!")
        else:
            print("잘못된 작업 명령!!")