# 함수화 작업

def f_rain(today):
    rain = open(os.getcwd()+'/py1_univ/2학기 기말 팀프로젝트/csv_file/rain.csv', 'r', encoding='cp949')
    rain_data = csv.reader(rain)
    header_1 = next(rain_data)
    print("강수량 갑니당") # debug
    rain_index = []
    rain_now_index = []
    rain_past_index = []
    for row_rain in rain_data: # 강수량 디버깅
        rain_index.append(row_rain) # 2차 배열 만듦.

    for i in range(len(rain_index)):
        if str(past_day) == str(rain_index[i][0]):
            print("작년의 오늘을 찾았습니다.")
            print(rain_index[i][0:]) # 인덱스 확인용 디버깅
            rain_past_index = rain_index[i][0:] # 인덱스 적용
            print(rain_past_index) # rain_past_index = 작년의 데이터
    if rain_index[i][2] == '': #비가 내리지 않았을 때, rain_past_index 리스트를 쓰면 사이즈 오버 오류가 발생하므로 의도적으로 원본 리스트에서 가져옴.
        rain_past_index[2] = 0
    rain.close()
    return(rain_past_index)