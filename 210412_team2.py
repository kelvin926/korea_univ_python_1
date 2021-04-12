blist = ['아메리카노', '카페라테', '카푸치노', '오렌지주스', '콜라', '자몽주스']
plist = [2500, 3000, 3000, 4000, 1500, 4000]
qu = len(blist)
total = 0
print("주문할 음료를 말씀하세요.\n")
for i in range(0, qu+2):
    if(i<7):
        num = int((input("%s 개수 (잔) : " %(blist[i]))))
        total += plist[i]*num
        i += 1
    else:
        print("총 금액은 : %d 원"%total)
        in_price = int(input("지불하실 금액을 입력하시오.>>"))
        if total == in_price:
            print("감사합니다.")
        elif total > in_price:
            print("돈이 %d원 부족합니다."%(total-in_price))
        elif total < in_price:
            print("감사합니다.")
            print("거스름돈은 %d 원 입니다"%(in_price-total))
        else:
            print("error")