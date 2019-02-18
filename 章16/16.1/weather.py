

class weather():

    def __init__(self,fl1='death_valley_2014.csv',fl2='sitka_weather_2014.csv'):
        self.fl1=fl1
        self.fl2=fl2

    def excute(self):
        self.collect(self.fl1)
        self.collect(self.fl2)
        


    def collect(self,fl):
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
        for index,column_header in enumerate(header_row):
            print(index,column_header)


    def high_lows(self,datas,highs,lows=''):
        fig=plt.figure(dpi=128,figsize=(10,6))
        plt.plot(datas,highs,c='red',alpha=0.5)
        if lows != 0:
            plt.plot(datas,lows,c='blue',alpha=0.5)
            plt.fill_between(datas,highs,lows,facecolor='blue',alpha=0.1)

        plt.title("Daily high tempretures,July 2014",fontsize=24)
        plt.xlabel('',fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature(F)",fontsize=16)
        plt.tick_params(axis='both',which='major',labelsize=16)

        plt.show()
        
        
