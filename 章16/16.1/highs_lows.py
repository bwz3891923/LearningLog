import csv
from plot import high_lows
from datetime import datetime


filenames='sitka_weather_07-2014.csv'  #16.1.1
with open(filenames) as f:
    reader = csv.reader(f)
    header_row=next(reader)
    print(header_row)

    datas,highs=[],[]
    for row in reader:
        current_date=datetime.strptime(row[0],"%Y-%m-%d")
        datas.append(current_date)
        highs.append(row[1])
    print(highs)

    
high_lows(datas,highs)




for index,column_header in enumerate(header_row):
    print(index,column_header)




