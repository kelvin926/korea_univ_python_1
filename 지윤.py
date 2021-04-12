blist = ['아메리카노', '카페라테', '카푸치노', '오렌지주스', '콜라', '자몽주스']
plist = [2500, 3000, 3000, 4000, 1500, 4000]
#q = len(blist) #얜 필요 없따
total = 0
print({total},"안녕")
for menu in blist: #a말고 blist가져와서 그냥 넣어도 돼 갯수개념이라
    print ("1.아메리카노", "2.카페라테", "3.카푸치노", "4.오렌지주스","5.콜라", "6.자몽주스")
    menu = int(input("메뉴를 선택하세요. : "))
    num = int(input("잔 수를 입력하세요. : "))
    total+= plist[menu-1]*num
    a = str(input("주문을 끝내시겠습니까?(y/n) "))
    if a == 'y':
        print("총 가격은 %d원 입니다." %total) #그리고 ,%total이 아니라 %total 이런식으로 하는거. 너무 c언어에 잡혀있는데...? :(
        break #브레이크 문 안넣어서 애가 다음으로 못넘어가고 무한 루프에 빠져서 중지됨
    else:
        continue
money=int(input("지불하실 금액을 입력하세요. : "))
if total == money:
    print("주문이 완료되었습니다.")
elif total<money: #여기 부등호 바뀜
    print("거스름돈은 %d원 입니다." %int(money-total)) #여기 total은 위에 for문에서는 int로 사용됐지만, 여기서 int로 명시적 형변환을 해줘야지 오류가 안생겨
elif total>money: #여기 부등호 바뀜
    print("돈이 %d원 부족합니다. 다시 결제해주세요." %int(total-money)) #total 스펠링 오류 , 여기도 위처럼 명시적 형변환 ㄲ
else:
    print("error")
    