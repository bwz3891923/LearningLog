import math 

dayup=math.pow((1.0+0.005),365)
daydown=math.pow((1.0-0.005),365)
print("向上:{:.2f},向下{:.2f}.".format(dayup,daydown))
