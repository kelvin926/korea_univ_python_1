coffee = int(input("커피를 몇 잔 구매하시겠습니까?(2000원) : "))
juice = int(input("쥬스는 몇 잔 구매하시겠습니까?(1000원) : "))
coffee = coffee
juice = juice
total = (coffee*2000)+(juice*1000)
print("총 금액은 %d 원 입니다."%(total))
in_price = int(input("돈을 넣어 주세요 : "))
if total == in_price:
    print("여기 커피%d잔과 쥬스%d잔 입니다"%(coffee, juice))
elif total > in_price:
    print("돈이 %d원 부족합니다 처음부터 다시 시도해 주세요."%(total-in_price))
elif total < in_price:
    print("여기 커피%d잔과 쥬스%d잔 입니다"%(coffee, juice))
    print("잔돈 %d원 여기 있습니다."%(in_price-total))
else:
    print("오류가 발생했습니다. 다시 시도해 주세요.")