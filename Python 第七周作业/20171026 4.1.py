from random import *

x=randint(0,9)
k=0

while True:
    user=eval(input("输入一个数字吧"))
    if user > x :
        print("大了呀")
        k+=1
    if user < x :
        print("小了呀")
        k+=1
    if user== x :
        print("预测了{}次，猜对了".format(k))
        break
      
