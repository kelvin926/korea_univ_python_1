# -*- coding: utf-8 -*-

'''
제목 : 기상 예측을 통한 교통상황 예측과 차량 운행 조언 프로그램
팀 : 9조
팀원 : 장현서(조장), 강기남, 김도환, 신승록
내용 : 기온, 미세먼지, 강수확률 등의 이전 기상 데이터[딕셔너리]를 이용하여 날씨와 교통 상황을 예측하거나 세차 등의 차량 운행을 조언하는 프로그램.
'''

import os
import csv
import time

###################################

# 함수화 작업

def f_rain():
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
        rain_past_index.append('')
    rain.close()
    return(rain_past_index)

################################

start_num = 1
while(1):
    
    if start_num == 1:
        pass
    elif start_num == 0:
        break
    else:
        print("에러 발생")
        break
    
    print("오늘의 날짜는 {} 입니다.".format(time.strftime('%Y-%m-%d', time.localtime(time.time()))))
    now = input("원하시는 날짜를 입력해주세요. ex. \'2021-01-01\' : ")

    if int(now[5:7]) >= 13:
        print("정확한 날짜를 입력해주세요!")
        continue
    
    if int(now[8:]) >= 32:
        print("정확한 날짜를 입력해주세요!")
        continue

    # 작년의 오늘을 구하기.
    now_year = int(now[0:4])
    past_day = str(now_year-1)+now[4:]
    print("1년전은 {} 입니다.".format(past_day))


    select = int(input("무엇을 실행할까요?\n1.작년의 강수량\n2.작년의 미세먼지\n3.작년의 기온\n4.기상 예측\n5.차량 운행 조언\n6.종료\n숫자로 입력해주세요! : "))

###################################################################################

    if select == 1: # 강수량
        
        print(f_rain())
        
        # rain = open(os.getcwd()+'/py1_univ/2학기 기말 팀프로젝트/csv_file/rain.csv', 'r', encoding='cp949')
        # rain_data = csv.reader(rain)
        # header_1 = next(rain_data)
        # print("강수량 갑니당") #debug
        # rain_index = []
        # rain_now_index = []
        # rain_past_index = []
        # for row_rain in rain_data: # 강수량 디버깅
        #     rain_index.append(row_rain) # 2차 배열 만듦.

        # # 작년, 오늘의 날씨를 구하는 부분
        # for i in range(len(rain_index)):
        #     if str(past_day) == str(rain_index[i][0]):
        #         print("작년의 오늘을 찾았습니다.")
        #         print(rain_index[i][0:]) # 인덱스 확인용 디버깅
        #         rain_past_index = rain_index[i][0:] # 인덱스 적용
        #         print(rain_past_index) # rain_past_index = 작년의 데이터

        # # 구동부
        # if rain_index[i][2] == '': #비가 내리지 않았을 때, rain_past_index 리스트를 쓰면 사이즈 오버 오류가 발생하므로 의도적으로 원본 리스트에서 가져옴.
        #     print("이 날에는 비가 내리지 않았습니다")
        # else:
        #     print("이 날에는 {}mm 의 비가 내렸었습니다.".format(rain_past_index[2]))

        print("강수량 완료")
        # rain.close()
        start_num = int(input("그만하시겠으면 0번을, 다시 하시겠으면 1번을 눌러주세요 : "))

###################################################################################

    if select == 2: # 미세먼지
        dust = open(os.getcwd()+'/py1_univ/2학기 기말 팀프로젝트/csv_file/dust.csv', 'r', encoding='cp949')
        dust_data = csv.reader(dust)
        header_2 = next(dust_data)

        print("미세먼지 갑니당") #debug
        dust_index = []
        dust_now_index = []
        dust_past_index = []
        for row_dust in dust_data: # 미세먼지 디버깅
            dust_index.append(row_dust) # 2차 배열 만듦.

        # 작년, 오늘의 미세먼지를 구하는 부분
        for i in range(len(dust_index)):
            if str(past_day) == str(dust_index[i][2]):
                print("작년의 오늘을 찾았습니다.")
                print(dust_index[i][0:]) # 인덱스 확인용 디버깅
                dust_past_index = dust_index[i][0:] # 인덱스 적용
                print(dust_past_index) # dust_past_index = 작년의 데이터

        # 구동부
        if dust_past_index[3] == '': # 미세먼지가 존재하지 않았을 때
            print("이 날의 과거 미세먼지 데이터가 존재하지 않습니다.")
        else:
            print("이 날에는 {}의 미세먼지가 있었습니다.".format(dust_past_index[3]))

        print("미세먼지 완료")
        dust.close()
        start_num = int(input("그만하시겠으면 0번을, 다시 하시겠으면 1번을 눌러주세요 : "))

###################################################################################

    if select == 3: # 기온
        tem = open(os.getcwd()+'/py1_univ/2학기 기말 팀프로젝트/csv_file/tem.csv', 'r', encoding='cp949')
        tem_data = csv.reader(tem) 
        header_3 = next(tem_data) #평균,저,고

        print("기온 갑니당") #debug
        tem_index = []
        tem_now_index = []
        tem_past_index = []
        for row_tem in tem_data: # 기온 디버깅
            tem_index.append(row_tem) # 2차 배열 만듦.

        # 작년, 오늘의 기온(평균,최저,최고)을 구하는 부분
        for i in range(len(tem_index)):
            if str(past_day) == str(tem_index[i][0]):
                print("작년의 오늘을 찾았습니다.")
                print(tem_index[i][0:]) # 인덱스 확인용 디버깅
                tem_past_index = tem_index[i][0:] # 인덱스 적용
                print(tem_past_index) # tem_past_index = 작년의 데이터

        # 구동부
            print("이 날에는 평균{}도, 최고{}도, 최소{}도의 기온을 가지고 있었습니다.".format(tem_past_index[2],tem_past_index[3],tem_past_index[4]))

        print("기온 완료")
        tem.close()
        start_num = int(input("그만하시겠으면 0번을, 다시 하시겠으면 1번을 눌러주세요 : "))

###################################################################################
    if select == 4: # 기상 예측

# 강수량 부분
        rain = open(os.getcwd()+'/py1_univ/2학기 기말 팀프로젝트/csv_file/rain.csv', 'r', encoding='cp949')
        rain_data = csv.reader(rain)
        header_1 = next(rain_data)
        print("강수량 갑니당") #debug
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

    # 미세먼지 부분
        dust = open(os.getcwd()+'/py1_univ/2학기 기말 팀프로젝트/csv_file/dust.csv', 'r', encoding='cp949')
        dust_data = csv.reader(dust)
        header_2 = next(dust_data)

        print("미세먼지 갑니당") #debug
        dust_index = []
        dust_now_index = []
        dust_past_index = []
        for row_dust in dust_data: # 미세먼지 디버깅
            dust_index.append(row_dust) # 2차 배열 만듦.
        
        for i in range(len(dust_index)):
            if str(past_day) == str(dust_index[i][2]):
                print("작년의 오늘을 찾았습니다.")
                print(dust_index[i][0:]) # 인덱스 확인용 디버깅
                dust_past_index = dust_index[i][0:] # 인덱스 적용
                print(dust_past_index) # dust_past_index = 작년의 데이터

        tem = open(os.getcwd()+'/py1_univ/2학기 기말 팀프로젝트/csv_file/tem.csv', 'r', encoding='cp949')
        tem_data = csv.reader(tem) 
        header_3 = next(tem_data) #평균,저,고

        print("기온 갑니당") #debug
        tem_index = []
        tem_now_index = []
        tem_past_index = []
        for row_tem in tem_data: # 기온 디버깅
            tem_index.append(row_tem) # 2차 배열 만듦.
        
        # 작년, 오늘의 기온(평균,최저,최고)을 구하는 부분
        for i in range(len(tem_index)):
            if str(past_day) == str(tem_index[i][0]):
                print("작년의 오늘을 찾았습니다.")
                print(tem_index[i][0:]) # 인덱스 확인용 디버깅
                tem_past_index = tem_index[i][0:] # 인덱스 적용
                print(tem_past_index) # tem_past_index = 작년의 데이터

        print("--------------------------------------")
        print("-- 작년의 기상 데이터 --")
        print("{}에는 강수량:{}mm, 미세먼지:{}, 평균기온:{}".format(past_day, rain_past_index[2], dust_past_index[3], tem_past_index[2]))
        rain.close()
        dust.close()
        tem.close()
###################################################################################

    if select == 5: # 교통 상황 예측
        pass
###################################################################################

    if select == 6: # 차량 운행 조언
        pass
###################################################################################

    if select == 7: # 종료
        break

print("종료합니당~")


'''
[to do list]
1. 기온 부분 디버깅 - 6/3
2. 날씨 데이터들 함수화. -> 날씨 지수 만들려면 함수화를 해야할 듯. - 6/3
3. 차량 운행 조언 부분 도환이한테 받아서 넣기 - 6/3
4. 교통 상황 예측 - 날씨 지수 + time함수를 통해 종합적으로 판단하도록. - 6/4
5. 전체 디버깅 - 6/4~5
6. PPT + 순서도 제작 - 6/5~6/6
'''