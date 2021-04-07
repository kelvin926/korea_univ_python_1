"""
gender = input("성별?")
year = int(input("학년?"))

if(gender == "여"):
    print("진리관 배정")
elif(gender == "남" and (year == 1 or year == 2)):
    print("정의관 배정")
elif(gender == "남" and (year == 3 or year == 4)):
    print("창조관 배정")
else:
    print("입력 오류")
"""

#########################################################

"""
numbers = [24, 1, 98, 20, 10, 33]
userno = int(input("찾고자 하는 킷값"))
find = False
for no in numbers:
    if no == userno:
        print("키 값 %d : 찾았습니다." %userno)
        find = True
        break
if find == False:
    print("키 값 %d: 목록에 없습니다." %userno)
"""

#########################################################

"""
for value in range(5):
    print(value)

for value in range(5, 10, 2):
    print(value)
"""

#########################################################

"""
minh = 3.0
maxh = 0.0
avgh = 0.0
height = [1.50, 1.44, 1.38, 1.55, 1.58, 1.65, 1.35, 1.48]
for i in range(len(height)):
    if height[i] < minh:
        minh = height[i]
    if height[i] > maxh:
        maxh = height[i]
    avgh += height[i]
avgh = avgh/len(height)

print("가장 작은 키 : %5.2f, 가장 큰 키 : %5.2f, 평균 키 : %5.2f" %(minh, maxh, avgh))
"""

#########################################################

"""
minh = 3.0
maxh = 0.0
avgh = 0.0
height = [1.50, 1.44, 1.38, 1.55, 1.58, 1.65, 1.35, 1.48]
i=0
nodata = len(height)

while (i<nodata):
    if height[i] < minh:
        minh = height[i]
    elif height[i] > maxh:
        maxh = height[i]
    avgh += height[i]
    i += 1

avgh = avgh/len(height)

print("가장 작은 키 : %5.2f, 가장 큰 키 : %5.2f, 평균 키 : %5.2f" %(minh, maxh, avgh))
"""

#########################################################

"""
numbers = 5
data = [10, -20, 40, 30, -5]
sum = 0
for n in data :
    if n < 0:
        continue
    sum += n
print("sum = ", sum)

"""

#########################################################

"""
numbers = 5
data = [10, -20, 40, 30, -5]
sum = 0
for n in data :
    if n < 0:
        break
    sum += n
print("sum = ", sum)
"""