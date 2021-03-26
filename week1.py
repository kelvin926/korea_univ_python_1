# print("hello")
# a = input('a =')
# print(a)
# print(input() + "을 입력하셨답니당")
# a = 1
# id(a)
# type(a)
# age = input("나이?")
# print(age)
# kk = 3
# print(kk)
# id(age)
# id(kk)
# ll = input()
# print(ll)
# id(ll)
# c = 3
# d = 3
# print(id(c))
# print(id(d))
# import keyword
# print(keyword.kwlist)

# s = "python"
# print(s[1:3])
# a=[1,2,3]
# b=['a','b']
# c=[[1,2],[20,30]]
# print(a.append(4))
# print(a.insert(2,10))
# print(a.remove(3))

# d={'a':100,'b':95}
# print(d.keys())

# print(d.values())

# puppy=dict()
# puppy["이름"]="밍키"
# puppy["나이"]=3
# puppy["ahaanrp"]=10.5
# print(puppy)

# a = (1,2,3,10)
# b = (10,20,30)
# print(a + b)

# age = len(a)
# print(age)


# age = int(input("나이?"))
# fee = 10000
# if (age >= 65):
#     fee = int(fee*0.8)

# print('입장료는' , fee, '원 입니다')

year = int(input("년도?"))
if (year % 400 == 0 or (year % 4 == 0 and year % 100)):
    print(year, "년은 윤년이다")
else:
    print(year, "년은 윤년이 아니다")
