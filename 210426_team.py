mybooks = [
{"제목":"안드로이드앱개발", "저자" : "최전산", "출판사": "PCB", "가격": 25000, "출판년도": 2017},
{"제목":"파이썬", "저자" : "강수라", "출판사": "연두", "가격": 23000, "출판년도": 2019},
{"제목":"자바스크립트", "저자" : "박정식", "출판사": "SSS", "가격": 38000, "출판년도": 2018},
{"제목":"HTML5", "저자" : "주환", "출판사": "대한", "가격": 33000, "출판년도": 2012},
{"제목":"컴파일러", "저자" : "장진웅", "출판사": "PCB", "가격": 24000, "출판년도": 2011},
{"제목":"C언어", "저자" : "홍말숙", "출판사": "한국", "가격": 29000, "출판년도": 2010},
{"제목":"프로그래밍언어론", "저자" : "현정숙", "출판사": "정의출판", "가격": 41000, "출판년도": 2009},
{"제목":"안드로이드", "저자" : "이광희", "출판사": "한국", "가격": 42000, "출판년도": 2013},
{"제목":"앱인벤터", "저자" : "박규진", "출판사": "대한", "가격": 30000, "출판년도": 2015}
]
while True:
    find = False
    exit_num = 0
    while True:
        choice = input('''도서 입력 / 검색
        1. 도서 입력
        2. 도서명으로 검색
        3. 저자명으로 검색
        4. 출판사명으로 검색
        5. 종료
        선택(1, 2, 3, 4, 5) : ''')
        if choice == '1': #도서 입력
            new_title=input("제목 >> ")
            new_author=input("저자명 >> ")
            new_company=input("출판사명 >> ")
            new_price=input("가격 >> ")
            new_when=input("출판년도 >> ")
            new_book = {"제목":new_title, "저자":new_author, "출판사":new_company, "가격":new_price, "출판년도":new_when}
            mybooks.append(new_book)
            print("새로운 도서를 등록했습니다.")
            continue
        elif choice == "2":
            kwd = "제목"
            break
        elif choice == "3":
            kwd = "저자"
            break
        elif choice == "4":
            kwd = "출판사"
            break
        elif choice == "5":
            kwd = "종료"
            exit_num = 1
            break
        else:
            print("입력이 잘못되었습니다.")
    
    if exit_num == 1:
        print("프로그램을 종료합니다")
        break
    
    userin = input("정확한 "+kwd+"을(를) 알려주세요!: ")
    for onebook in mybooks:
        if userin == onebook[kwd]:
            print("제 목: ", onebook["제목"])
            print("저 자: ", onebook["저자"])
            print("출판사: ", onebook["출판사"])
            print("가 격: ", onebook["가격"])
            find = True
    if find == False:
        print("찾지 못했습니다 ㅠㅠ ")
    
    keepgoing = input("계속 하시겠습니까? (1:네 0:아니오): ")
    if keepgoing == '1':
        continue
    elif keepgoing == '0':
        print("프로그램을 종료합니다")
        break
    else:
        print("입력 에러, 프로그램을 종료합니다")
        break