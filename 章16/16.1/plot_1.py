from matplotlib import pyplot as plt




def high_lows(datas,highs,lows='',datas_1='',highs_1='',lows_1=''):
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
    
    
