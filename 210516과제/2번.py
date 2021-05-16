'''
<2번> - 양의 정수 중에서 자신과 1로만 나누어지는 수를 소수라고 한다. N이 주어지면 N보다 작은 소수를 찾는 프로그램을 작성하시오
'''

# 2021271424 장현서 - 파이썬 과제 210516 제출. github: @kelvin926
# 2번 코드
N = int(input("양의 정수 값 N을 입력 : "))
sosu = 1
for i in range(2, N):
    if N % i == 0:
        sosu = 0
if sosu == 1:
    print("{}은(는) 소수입니다.".format(N))
else:
    print("{}은(는) 소수가 아닙니다.".format(N))