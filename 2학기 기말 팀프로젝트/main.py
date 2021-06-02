# -*- coding: utf-8 -*-

'''
제목 : 기상 예측을 통한 교통상황 예측과 차량 운행 조언 프로그램
팀 : 9조
팀원 : 장현서(조장), 강기남, 김도환, 신승록
내용 : 기온, 미세먼지, 강수확률 등의 이전 기상 데이터[딕셔너리]를 이용하여 날씨와 교통 상황을 예측하거나 세차 등의 차량 운행을 조언하는 프로그램.
'''

'''
전년도 날씨 데이터를 가져오는 것을 가장 큰 목표로 함.
'''

import csv

rain = open('py1_univ/2학기 기말 팀프로젝트/csv_file/rain.csv', 'r', encoding='cp949')
dust = open('py1_univ/2학기 기말 팀프로젝트/csv_file/dust.csv', 'r', encoding='cp949')
tem = open('py1_univ/2학기 기말 팀프로젝트/csv_file/tem.csv', 'r', encoding='cp949')
rain_data = csv.reader(rain)
header_1 = next(rain_data)

dust_data = csv.reader(dust)
header_2 = next(dust_data)

tem_data = csv.reader(tem)
header_3 = next(tem_data)

q_rain = input("날짜를 입력해주세요. ex. \'2021-01-01\'")

print("강수량 갑니당") #debug
rain_index = []
rain_now_index = []
for row_rain in rain_data: # 강수량 디버깅
    # print(row_rain)
    rain_index.append(row_rain)
    # print(rain_index)

for i in range(len(rain_index)):
    if q_rain == rain_index[i][0]:
        print("무야호")
        print(rain_index[i][0:]) # 인덱스 확인용 디버깅
        rain_now_index = rain_index[i][0:] # 인덱스 적용

if rain_now_index[2] == '': #비가 내리지 않았을 때
    print("이 날에는 비가 내리지 않았습니다")
else:
    print("이 날에는 {}mm 의 비가 내렸습니다.".format(rain_now_index[2]))

print("강수량 완료")

rain.close()



# print("미세먼지 갑니당") #debug
# for row_dust in dust_data: # 미세먼지 디버깅
#     print(row_dust)
# dust.close()



# print("기온 갑니당") #debug
# for row_tem in tem_data: # 기온 디버깅
#     print(row_tem)
# tem.close()