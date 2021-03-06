import csv
from plot_1 import high_lows
from datetime import datetime
from convert import convert

filenames='death_valley_2014.csv'  #16.1.1
with open(filenames) as f:
    reader = csv.reader(f)        
    header_row=next(reader)
    print(header_row)

    datas,highs,lows=[],[],[]
    for row in reader:
        try:
            current_date=datetime.strptime(row[2],"%Y-%m-%d")
            high=convert(float(row[4]))   
            low =convert(float(row[5]))
            
    
    
        except ValueError:
            print(current_date,'missing data')
            
        else:
            datas.append(current_date)
            highs.append(high)
            lows.append(low)
            
            
    

    
high_lows(datas,highs,lows)



for index,column_header in enumerate(header_row):
    print(index,column_header)




