import csv
from datetime import datetime
from convert import convert
from matplotlib import pyplot as plt

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

    title=[]
    title.append(datas)
    title.append(highs)
    title.append(lows)
    return title          


def high_lows(weather,weather_1=''):
    datas,highs,lows=weather
    if weather_1 != 0:
        datas_1,highs_1,lows_1=weather_1
            
    fig=plt.figure(dpi=128,figsize=(10,6))
    plt.plot(datas,highs,c='red',alpha=0.5)
    plt.plot(datas,lows,c='blue',alpha=0.5)
    plt.fill_between(datas,highs,lows,facecolor='blue',alpha=0.1)

    if weather_1 != 0:
        plt.plot(datas_1,highs_1,c='#C71585',alpha=0.5)
        plt.plot(datas_1,lows_1,c='#8A2BE2',alpha=0.5)
        plt.fill_between(datas_1,highs_1,lows_1,facecolor='#FFA500',alpha=0.1)

    

    plt.title("Daily tempretures, 2014",fontsize=24)
    plt.xlabel('',fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature(C)",fontsize=16)
    plt.tick_params(axis='both',which='major',labelsize=16)

    plt.show()







weather=main('sitka_weather_07-2014.csv')
weather_1=main('death_valley_2014.csv')
high_lows(weather,weather_1)








