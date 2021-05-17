'''
def sumandavg(a, b):
    print("합 =",a+b)
    print("평균 =", (a+b)/2)

a = int(input("첫번째 수 : "))
b = int(input("두번째 수 : "))

sumandavg(a, b)

'''

'''
def sumanavg(a, b):
    sum = a+b
    avg = (a+b)/2
    return sum, avg

for i in range (0, 2):
    a1 = int(input("a값은? : "))
    b1 = int(input("b값은? : "))
    sum1, avg1 = sumanavg(a1, b1)
    print("합 : {}\n평균 : {}".format(sum1, avg1))
'''

def sumanavg(a, b):
    global sum, avg
    sum = a+b
    avg = (a+b)/2
    # return sum, avg # 글로벌 변수라서 굳이 리턴할 필요가 없다.

for i in range (0, 2):
    a1 = int(input("a값은? : "))
    b1 = int(input("b값은? : "))
    sum1, avg1 = sumanavg(a1, b1)
    print("합 : {}\n평균 : {}".format(sum1, avg1))
