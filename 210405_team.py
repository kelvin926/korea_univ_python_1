blist = ['아메리카노', '카페라테', '카푸치노', '오렌지주스', '콜라', '자몽주스']
plist = [2500, 3000, 3000, 4000, 1500, 4000]
qu = len(blist)
total = 0
for i in range(1, qu+2):
    if(i<7):
        num = int((input("%s를 몇개 구입하시겠습니까?" %(blist[i-1]))))
        total += plist[i-1]*num
        print("현재까지 %d원 입니다"%(total))
        i += 1
    else:
        print("총 %d원 입니다."%total)
        in_price = int(input("돈을 입력해 주세요"))
        if total == in_price:
            print("여기 있습니다")
        elif total > in_price:
            print("돈이 %d원 부족합니다 처음부터 다시 시도해 주세요."%(total-in_price))
        elif total < in_price:
            print("여기 있습니다")
            print("잔돈 %d원 여기 있습니다."%(in_price-total))
        else:
            print("error")