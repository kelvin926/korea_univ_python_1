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

###################################################################################

# 강수량 함수

def f_rain(day,date_option):
    rain = open('./csv_file/rain.csv', 'r', encoding='cp949')
    rain_data = csv.reader(rain)
    header_1 = next(rain_data)
    
    rain_index = []
    rain_past_index = []
    
    for row_rain in rain_data:
        rain_index.append(row_rain) # 2차 배열 만듦. rain_index

    for i in range(len(rain_index)):
        if str(day) == str(rain_index[i][0]):
            # print("작년의 오늘을 찾았습니다.")
            rain_past_index = rain_index[i+date_option][0:] # 인덱스 적용
    
    if rain_past_index[2] == '': #비가 내리지 않았을 때, rain_past_index 리스트를 쓰면 사이즈 오버 오류가 발생하므로 의도적으로 원본 리스트에서 가져옴.
        rain_past_index[2] = 0 # 빈 공간을 0으로 치환.

    return(rain_past_index)
    rain.close()

###################################################################################

# 미세먼지 함수

def f_dust(day,date_option):
    dust = open('./csv_file/dust.csv', 'r', encoding='cp949')
    dust_data = csv.reader(dust)
    header_2 = next(dust_data)
    
    dust_index = []
    dust_past_index = []
    
    for row_dust in dust_data:
        dust_index.append(row_dust) # 2차 배열 만듦. dust_index

    for i in range(len(dust_index)):
        if str(day) == str(dust_index[i][2]):
            # print("작년의 오늘을 찾았습니다.")
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
    tem = open('./csv_file/tem.csv', 'r', encoding='cp949')
    tem_data = csv.reader(tem)
    header_3 = next(tem_data)
    
    tem_index = []
    tem_past_index = []
    
    for row_tem in tem_data:
        tem_index.append(row_tem) # 2차 배열 만듦. tem_index

    for i in range(len(tem_index)):
        if str(day) == str(tem_index[i][0]):
            # print("작년의 오늘을 찾았습니다.")
            tem_past_index = tem_index[i+date_option][0:] # 인덱스 적용
    
    # 데이터: 평균, 최저, 최고 기온
    return(tem_past_index[2:])
    tem.close()

###################################################################################

# 교통량 함수

def f_transport(day,date_option):
    transport = open('./csv_file/transport.csv', 'r', encoding='cp949')
    transport_data = csv.reader(transport)
    header_4 = next(transport_data)
    
    transport_index = []
    transport_past_index = []
    
    for row_transport in transport_data:
        transport_index.append(row_transport)
        
    for i in range(len(transport_index)):
        if str(day) == str(transport_index[i][0]):
            # print("작년의 오늘을 찾았습니다.")
            transport_past_index = transport_index[i+date_option][0:] 

    return(transport_past_index)
    transport.close()


###################################################################################
    
# 교통량 정도 함수
def transport_per(percent):
    if int(percent) <=500: 
        return("매우 좋음")
    elif (int(percent)>500 & int(percent) <= 800): 
        return("좋음")
    elif (int(percent)>800 & int(percent) <= 1200): 
        return("보통")
    elif (int(percent)>1200 & int(percent) <= 1600): 
        return("나쁨")
    elif (int(percent)>1600): 
        return("매우 나쁨")
    
###################################################################################

# 차량운행지수
def transport_p(percent):
    if int(percent) <=500: 
        return("1")
    elif (int(percent)>500 & int(percent) <= 800): 
        return("2")
    elif (int(percent)>800 & int(percent) <= 1200): 
        return("3")
    elif (int(percent)>1200 & int(percent) <= 1600): 
        return("4")
    elif (int(percent)>1600): 
        return("5")
    
def  dust_p(percent):
    if int(percent) <=25: 
        return("1")
    elif (int(percent)>25 & int(percent) <= 50): 
        return("2")
    elif (int(percent)>50 & int(percent) <= 80): 
        return("3")
    elif (int(percent)>80 & int(percent) <= 150): 
        return("4")
    elif (int(percent)>150): 
        return("5")

###################################################################################
    
# 날짜 입력, 선택 부분

start_num = 1
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
    now = input("원하시는 날짜를 입력해주세요. ex. \'2021-01-01\' : ")

    if int(now[5:7]) >= 13:
        print("정확한 날짜를 입력해주세요!")
        continue
    
    if int(now[8:]) >= 32:
        print("정확한 날짜를 입력해주세요!")
        continue

    global now_year, past_day
    # 작년의 오늘을 구하기.
    now_year = int(now[0:4])
    past_day = str(now_year-1)+now[4:]
    print("1년전은 {} 입니다.".format(past_day))
    print("-------------------------------------------------------------------------------------")
    select = int(input("무엇을 실행할까요?\n1.작년의 강수량\n2.작년의 미세먼지\n3.작년의 기온\n4.기상 예측\n5.교통 상황 예측\n6.차량 운행 조언\n7.종료\n숫자로 입력해주세요! : "))
    print("-------------------------------------------------------------------------------------")

###################################################################################

    if select == 1: # 강수량
        
        rain_now_index = f_rain(past_day,0)
        if rain_now_index[2] == 0:
            print("{}에는 비가 내리지 않았습니다.".format(rain_now_index[0]))
        else:
            print("{}애는 {}mm의 비가 내렸습니다.".format(rain_now_index[0], rain_now_index[2]))
        
        # print("강수량 완료")
        print("-------------------------------------------------------------------------------------")
        start_num = int(input("그만하시겠으면 0번을, 다시 하시겠으면 1번을 눌러주세요 : "))

###################################################################################

    if select == 2: # 미세먼지
        
        print("{}의 미세먼지는 {} 입니다.".format(past_day, dust_per(f_dust(past_day,0)[3])))
        
        # print("미세먼지 완료")
        print("-------------------------------------------------------------------------------------")
        start_num = int(input("그만하시겠으면 0번을, 다시 하시겠으면 1번을 눌러주세요 : "))

###################################################################################

    if select == 3: # 기온
        
        tem_now_index = f_tem(past_day,0) # 평균, 최저, 최고 기온
        print("{}의 평균 기온은 {}도, 최저 기온은 {}도, 최고 기온은 {}도 입니다.".format(past_day, tem_now_index[0], tem_now_index[1], tem_now_index[2]))
        
        # print("기온 완료")
        print("-------------------------------------------------------------------------------------")
        start_num = int(input("그만하시겠으면 0번을, 다시 하시겠으면 1번을 눌러주세요 : "))

###################################################################################
    if select == 4: # 기상 예측
        print("{}에는 {}mm가 오고, {}에는 {}mm가 오고, {}에는 {}mm의 비가 왔습니다.".format(f_rain(past_day,-1)[0], f_rain(past_day,-1)[2], past_day, f_rain(past_day, 0)[2], f_rain(past_day,1)[0], f_rain(past_day, 1)[2]))
        avg_rain = (float(f_rain(past_day, -1)[2]) + float(f_rain(past_day, 0)[2]) + float(f_rain(past_day, 1)[2]))/3
        if avg_rain == 0:
            print("따라서, 작년 데이터를 기반으로 예측했을 때 {}에는 비가오지 않을 것 같습니다.\n".format(now))
        else:
            print("따라서, 작년 데이터를 기반으로 예측했을 때 {}에는 {:.1f}mm의 비가 올 가능성이 있습니다.\n".format(now, avg_rain))
        
        print("{}에는 미세먼지 {}이고, {}에는 미세먼지 {}이고, {}에는 미세먼지가 {}이었습니다.".format(f_dust(past_day,-1)[2], dust_per(f_dust(past_day,-1)[3]), past_day, dust_per(f_dust(past_day,0)[3]), f_dust(past_day,1)[2], dust_per(f_dust(past_day,1)[3])))
        avg_dust = (int(f_dust(past_day, -1)[3]) + int(f_dust(past_day, 0)[3]) + int(f_dust(past_day, 1)[3]))/3
        print("따라서, 작년 데이터를 기반으로 예측했을 때 {}에는 미세먼지가 {}일 가능성이 있습니다.\n".format(now, dust_per(avg_dust)))
        
        print("{}에는 평균기온 {}도, {}에는 평균기온 {}도, {}에는 평균기온이 {}도이었습니다.".format(f_dust(past_day,-1)[2], f_tem(past_day,-1)[0], past_day, f_tem(past_day,0)[0], f_dust(past_day,1)[2], f_tem(past_day,1)[0])) 
        avg_tem = (float(f_tem(past_day, -1)[0]) + float(f_tem(past_day, 0)[0]) + float(f_tem(past_day, 1)[0]))/3
        print("따라서, 작년 데이터를 기반으로 예측했을 때 {}에는 평균기온이 {:.1f}도일 가능성이 있습니다.\n".format(now, avg_tem))
    # 온도부분에서는 의도적으로 날짜를 리턴하지 않게 했기 때문에, 미세먼지 날짜 데이터를 임시로 가져오게 했습니다.
    
        print("-------------------------------------------------------------------------------------")
        start_num = int(input("그만하시겠으면 0번을, 다시 하시겠으면 1번을 눌러주세요 : "))

###################################################################################

    if select == 5: # 교통 상황 예측
        
        print("{}의 교통량은 {} 입니다.".format(past_day, transport_per(f_transport(past_day,0)[1])))

        print("-------------------------------------------------------------------------------------")
        start_num = int(input("그만하시겠으면 0번을, 다시 하시겠으면 1번을 눌러주세요 : "))
        
###################################################################################

    if select == 6: # 차량 운행 조언
        print('길 막히는 정도에 따라 1-5로 나눔(5가 막힘)//미세먼지 정도에 따라 1-5로 나눔(5가 더러움)')
        print("{}의 미세먼지는 {} 이고,교통량은 {} 입니다. 따라서 예측한 차량운행지수는 {} 입니다.".format(past_day, dust_per(f_dust(past_day,0)[3]), transport_per(f_transport(past_day,0)[1]), int(dust_p(f_dust(past_day,0)[3])) + int(transport_p(f_transport(past_day,0)[1]))))

        print("-------------------------------------------------------------------------------------")
        start_num = int(input("그만하시겠으면 0번을, 다시 하시겠으면 1번을 눌러주세요 : "))
        
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
