from matplotlib import pyplot as plt




def high_lows(datas,highs):
    fig=plt.figure(dpi=128,figsize=(10,6))
    plt.plot(datas,highs,c='red')

    plt.title("Daily high tempretures,July 2014",fontsize=24)
    plt.xlabel('',fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature(F)",fontsize=16)
    plt.tick_params(axis='both',which='major',labelsize=16)

    plt.show()
    
    
