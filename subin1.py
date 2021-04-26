past = int(input("전 달 전력량: "))
this = int(input("이번 달 전력량: "))
if(this>past):
    usage = int(this-past)
    print("이번 달 전력 사용량: %d" %usage)
else:
    usage = int(past-this)
    print("이번 달 전력 사용량: %d" %usage)

if (usage<=200):
    total = 910 + usage * 93.3
elif (201<usage<=400):
    total = 1600 + usage * 187.9
else:
    total = 7300 + usage * 280.6

print("전기요금 = %0.1f" %total)