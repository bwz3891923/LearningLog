import csv
from plot_1 import high_lows
from datetime import datetime


filenames='death_valley_2014.csv'  #16.1.1
with open(filenames) as f:
    reader = csv.reader(f)
    header_row=next(reader)
    print(header_row)

    datas,highs,lows=[],[],[]
    for row in reader:
        current_date=datetime.strptime(row[0],"%Y-%m-%d")
        datas.append(current_date)
        highs.append(row[1])
        low= int(row[3])
        lows.append(low)
    print(highs)

    
high_lows(datas,highs,lows)



for index,column_header in enumerate(header_row):
    print(index,column_header)




