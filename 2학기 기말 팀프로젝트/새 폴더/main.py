#-*- coding: utf-8 -*-

'''
제목 : 기상 예측을 통한 교통상황 예측과 차량 운행 조언 프로그램
팀 : 9조
팀원 : 장현서(조장), 강기남, 김도환, 신승록
내용 : 기온, 미세먼지, 강수확률 등의 이전 기상 데이터[딕셔너리]를 이용하여 날씨와 교통 상황을 예측하거나 세차 등의 차량 운행을 조언하는 프로그램.
'''



'''
[to do list]
1. 교통 상황 예측 부분 코딩. [교통 상황을 CSV로 받는게 아니라, time함수를 이용해서, 출퇴근 시간 + 날씨(비 오는지)에 따라 교통 상황 예측.] (6/5) 완
2. 차량 운행 지수 코딩. [미세먼지 정도 + 날씨[비 오는지]] (6/5) 완
3. 전체 디버깅 + 중복 함수 제거 (6/5) 완
4. 발표자료 제작을 위한 전체 구조도 글로 작성 (6/5)
5. 최종 발표 자료 제작 [PPT + 순서도] (6/6)
'''



import os
import csv
import time

###################################################################################

# 강수량 함수
def f_rain(day,date_option):
    # rain = open('py1_univ/2학기 기말 팀프로젝트/csv_file/rain.csv', 'r', encoding='cp949')
    rain = open('./csv_file/rain.csv', 'r', encoding='cp949')
    rain_data = csv.reader(rain)
    header_1 = next(rain_data)
    
    rain_index = []
    rain_past_index = []
    
    for row_rain in rain_data:
        rain_index.append(row_rain) # 2차 배열 만듦. rain_index

    for i in range(len(rain_index)):
        if str(day) == str(rain_index[i][0]):
            rain_past_index = rain_index[i+date_option][0:] # 인덱스 적용
    
    if rain_past_index[2] == '': #비가 내리지 않았을 때, rain_past_index 리스트를 쓰면 사이즈 오버 오류가 발생하므로 의도적으로 원본 리스트에서 가져옴.
        rain_past_index[2] = 0 # 빈 공간을 0으로 치환.

    return(rain_past_index)
    rain.close()

###################################################################################

# 미세먼지 함수
def f_dust(day,date_option):
    # dust = open('py1_univ/2학기 기말 팀프로젝트/csv_file/dust.csv', 'r', encoding='cp949')
    dust = open('./csv_file/dust.csv', 'r', encoding='cp949')
    dust_data = csv.reader(dust)
    header_2 = next(dust_data)
    
    dust_index = []
    dust_past_index = []
    
    for row_dust in dust_data:
        dust_index.append(row_dust) # 2차 배열 만듦. dust_index

    for i in range(len(dust_index)):
        if str(day) == str(dust_index[i][2]):
            dust_past_index = dust_index[i+date_option][0:] # 인덱스 적용
    
    return(dust_past_index)
    
    dust.close()

###################################################################################

# 미세먼지 농도 함수
def dust_per(percent):
    if int(percent) <=25: # 좋음
        return("매우 좋음")
    elif (int(percent)>25 & int(percent) <= 50): # 보통
        return("좋음")
    elif (int(percent)>50 & int(percent) <= 80): # 보통
        return("보통")
    elif (int(percent)>80 & int(percent) <= 150): # 나쁨
        return("나쁨")
    elif (int(percent)>150): # 매우 나쁨
        return("매우 나쁨")
    
    '''
    [미세먼지 단계]
    매우 좋음:0~25
    좋음 : 26~50
    보통 : 51~80
    나쁨 : 81~150
    매우 나쁨 : 151 ~ 
    '''

###################################################################################

# 기온 함수
def f_tem(day, date_option):
    # tem = open('py1_univ/2학기 기말 팀프로젝트/csv_file/tem.csv', 'r', encoding='cp949')
    tem = open('./csv_file/tem.csv', 'r', encoding='cp949')
    tem_data = csv.reader(tem)
    header_3 = next(tem_data)
    
    tem_index = []
    tem_past_index = []
    
    for row_tem in tem_data:
        tem_index.append(row_tem) # 2차 배열 만듦. tem_index

    for i in range(len(tem_index)):
        if str(day) == str(tem_index[i][0]):
            tem_past_index = tem_index[i+date_option][0:] # 인덱스 적용
    
    # 데이터: 평균, 최저, 최고 기온
    return(tem_past_index)
    tem.close()

###################################################################################

# 교통량 함수
'''
6~10시 , 18~21시 : 출퇴근 시간 + 강수량에 따른 교통 혼잡도 구성. (1 ~ 5)
1. 출퇴근 시간 + 강수량 많음 : 매우 막힘 (5)
2. 출퇴근 시간 + 강수량 적음 : 막힘 (4)
3. 출퇴근 시간 + 강수량 없음 : 보통 (3)
4. 출퇴근 아님 + 강수량 많음 : 막힘 (4)
5. 출퇴근 아님 + 강수량 적음 : 원활함 (2)
6. 출퇴근 아님 + 강수량 없음 : 매우 원활함 (1)
'''
def f_transport(hour):
    avg_rain = (float(f_rain(past_day, -1)[2]) + float(f_rain(past_day, 0)[2]) + float(f_rain(past_day, 1)[2]))/3
    if ((int(hour >=6) & int(hour<=10)) | (int(hour>=18) & int(hour<=21))): # 출퇴근 시간
        if (avg_rain > 20): #강수량 많음
            return("매우 막힘")
        elif ((avg_rain <= 20) & (avg_rain > 0)): # 강수량 적음
            return("막힘")
        else: #강수량 없음
            return ("보통")
    else: # 출퇴근 시간 아님
        if (avg_rain > 20): #강수량 많음
            return("막힘")
        elif ((avg_rain <= 20) & (avg_rain > 0)): # 강수량 적음
            return("원활함")
        else: #강수량 없음
            return("매우 원활함")
    

###################################################################################

# 차량 운행 지수
'''
(비 오는 날에 미세먼지가 많을리가 없지만, 전 날에 미세먼지가 있었다면 운행 지수를 높인다.)
1. 미세먼지 많음(70 이상) + 비 옴 : 매우 더러움 (5)
2. 미세먼지 보통(30~70) + 비 옴 : 더러움 (4)
3. 미세먼지 적음(30 이하) + 비 옴 : 보통 (3)
4. 미세먼지 많음(70 이상) + 비 안옴 : 보통 (3)
5. 미세먼지 보통(30~70) + 비 안옴 : 깨끗함 (2)
6. 미세먼지 적음(30 이하) + 비 안옴 : 매우 깨끗함 (1)
'''

def transport_per():
    avg_dust = (int(f_dust(past_day, -1)[3]) + int(f_dust(past_day, 0)[3]) + int(f_dust(past_day, 1)[3]))/3
    avg_rain = (float(f_rain(past_day, -1)[2]) + float(f_rain(past_day, 0)[2]) + float(f_rain(past_day, 1)[2]))/3
    if (avg_rain > 0): # 비 옴
        if (avg_dust >= 70):
            return("올", "매우 더러움")
        if ((avg_dust>30) & (avg_dust < 70)):
            return("올", "더러움")
        if (avg_dust <= 30):
            return("올", "보통")
    else: # 비 안 옴
        if (avg_dust >= 70):
            return("안올", "보통")
        if ((avg_dust>30) & (avg_dust < 70)):
            return("안올", "깨끗함")
        if (avg_dust <= 30):
            return("안올", "매우 깨끗함")
###################################################################################

# 스타팅 넘버
start_num = 1

###################################################################################

# 날짜 입력, 선택 부분
while(1):
    print("-------------------------------------------------------------------------------------")
    
    if start_num == 1:
        pass
    elif start_num == 0:
        break
    else:
        print("에러 발생")
        break
    
    print("오늘의 날짜는 {} 입니다.".format(time.strftime('%Y-%m-%d', time.localtime(time.time()))))
    now = input("원하시는 날짜를 입력해주세요. 2021년만 지원합니다. ex. \'2021-01-01\' : ")

    if int(now[5:7]) >= 13: # 13월 이상
        print("정확한 날짜를 입력해주세요!")
        continue
    
    if int(now[8:]) >= 32: # 32일 이상
        print("정확한 날짜를 입력해주세요!")
        continue

    global now_year, past_day

    # 작년의 오늘을 구하기.
    now_year = int(now[0:4])
    past_day = str(now_year-1)+now[4:]
    # print("1년전은 {} 입니다.".format(past_day))
    print("-------------------------------------------------------------------------------------")

###################################################################################

    # 시간 입력 부분
    print("현재 시각은 {}시 {}분 입니다.".format(time.strftime('%H', time.localtime(time.time())), time.strftime('%M', time.localtime(time.time()))))
    print("-------------------------------------------------------------------------------------")
    now_time = input("기준 시간을 입력해주세요! ex. \'18:03\' : ")
    
    global now_hour, now_min
    
    now_hour = int(now_time[0:1])
    now_min = int(now_time[3:4])

###################################################################################

    # 기상 예측
    print("{}에는 {}mm가 오고, {}에는 {}mm가 오고, {}에는 {}mm의 비가 왔습니다.".format(f_rain(past_day,-1)[0], f_rain(past_day,-1)[2], past_day, f_rain(past_day, 0)[2], f_rain(past_day,1)[0], f_rain(past_day, 1)[2]))
    
    avg_rain = (float(f_rain(past_day, -1)[2]) + float(f_rain(past_day, 0)[2]) + float(f_rain(past_day, 1)[2]))/3
    print("{}에는 미세먼지 {}이고, {}에는 미세먼지 {}이고, {}에는 미세먼지가 {}이었습니다.".format(f_dust(past_day,-1)[2], dust_per(f_dust(past_day,-1)[3]), past_day, dust_per(f_dust(past_day,0)[3]), f_dust(past_day,1)[2], dust_per(f_dust(past_day,1)[3])))
    
    avg_dust = (int(f_dust(past_day, -1)[3]) + int(f_dust(past_day, 0)[3]) + int(f_dust(past_day, 1)[3]))/3
    print("{}에는 평균기온 {}도, {}에는 평균기온 {}도, {}에는 평균기온이 {}도이었습니다.\n".format(f_tem(past_day,-1)[0], f_tem(past_day,-1)[2], past_day, f_tem(past_day,0)[2], f_tem(past_day,1)[0], f_tem(past_day,1)[2])) 
    
    avg_tem = (float(f_tem(past_day, -1)[2]) + float(f_tem(past_day, 0)[2]) + float(f_tem(past_day, 1)[2]))/3
    print("따라서, 작년 데이터를 기반으로 예측했을 때 {}에는 평균기온이 {:.1f}도일 가능성이 있고, 미세먼지는 {}일 가능성이 있으며.".format(now, avg_tem, dust_per(avg_dust)))
    
    if avg_rain == 0:
        print("{}에는 비가오지 않을 것 같습니다.".format(now))
    else:
        print("{:.1f}mm의 비가 올 가능성이 있습니다. 우산 챙기세요!".format(avg_rain))
    
    print("-------------------------------------------------------------------------------------") 
###################################################################################

    # 교통 상황 예측
    print("{}의 예상 교통량은 {} 입니다.".format(now, f_transport(now_hour)))

    print("-------------------------------------------------------------------------------------")
###################################################################################

    # 차량 운행 조언
    is_rain, is_transport = transport_per()
    print("{}의 예상 미세먼지 정도는 {} 이고, 비가 {} 것 같습니다. 따라서 예측한 차량운행지수는 {} 입니다.".format(now, dust_per(avg_dust), is_rain, is_transport))
    
    print("-------------------------------------------------------------------------------------")
    
###################################################################################

    # 종료 확인
    start_num = int(input("종료하시려면 0을, 다시 시도하시겠으면 1을 입력해주세요. : "))
    