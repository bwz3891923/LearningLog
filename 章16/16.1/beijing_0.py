import csv
from datetime import datetime
from matplotlib import pyplot as pl

def main():
    filenames='beijing.csv'
    with open(filenames) as fl:
        reader= csv.reader(fl)
        head_row=next(reader)

        for index,column in enumerate(head_row):
            print(index,column)

        dates,highs,lows,avgs=[],[],[],[]
        for detail in reader:
            
            
            date=datetime.strptime(detail[2],"%Y-%m-%d")
            high=detail[4]
            low=detail[5]
            avg=detail[3]

            dates.append(detail[2])
            highs.append(detail[4])
            lows.append(detail[5])
            avgs.append(detail[3])


        print(highs)
        print(lows)


        plots(dates,highs)

        
                


def plots(dates='',highs='',lows='',avgs=''):
    pl.figure(dpi=128,figsize=(10,6))
    pl.plot(dates,highs,c='red')
    pl.plot(dates,lows,c='blue')
    

    
    pl.title("Weather of Beijing",fontsize=24)
    pl.xlabel('',fontsize=16)
    fi

    pl.ylabel("Tempreture",fontsize=16)
    pl.tick_params(axis='both',which='major',labelsize=16)

    pl.show()



    
    
    


            
            
        


main()
