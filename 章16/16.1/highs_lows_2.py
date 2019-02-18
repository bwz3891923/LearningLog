import csv
from plot_1 import high_lows
from datetime import datetime
from convert import convert

def main(fl):
    filenames=fl  #16.1.1
    with open(filenames) as f:
        reader = csv.reader(f)
        header_row=next(reader)
        print(header_row)

        datas,highs,lows=[],[],[]
        for row in reader:
            try:
                current_date=datetime.strptime(row[0],"%Y-%m-%d")
                high=convert(float(row[1]))   
                low= convert(float(row[3]))
            
    
    
            except ValueError:
                print(current_date,'missing data')
            
            else:
                datas.append(current_date)
                highs.append(high)
                lows.append(low)
               
    high_lows(datas,highs,lows)
    return datas,highs,lows
    for index,column_header in enumerate(header_row):
        print(index,column_header)




main('death_valley_2014.csv')
main('sitka_weather_2014.csv')







