from random import *

i,u=0,0

for k in range(10):
    gamble=list("TFF")
    shuffle(gamble)
    print("洗牌后的顺序为{}".format(gamble))

    choose=randint(0,len(gamble)-1)
    print("选手的选择是{}".format(choose))

    point=gamble[choose]
    print("选手{}车子".format("获得" if str(point)=="T" else "没有获得"))

    if str(point)=="T":
        u=u+1
        print(u)


    


    

    i+=1
    print("\n\n\n")
   


ratio=u/i

print(ratio)
