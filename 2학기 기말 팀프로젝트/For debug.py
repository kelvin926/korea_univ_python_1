import csv
f = open('py1_univ/2학기 기말 팀프로젝트/csv_file/rain.csv')
data = csv.reader(f)
header = next(data)
for row in data:
    print(row)
f.close()