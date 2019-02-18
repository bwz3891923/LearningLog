import math

Factor,day= 1.0,1
holiday=int(input("假日多少："))


for i in range(365):
    if day in [0,4]:
        Factor=Factor
    else:
        Factor*=1.01

    day+=1

    if i%holiday==0:
        day=0

    print("{:8},{:8},{:.5f} \n".format(i,day, Factor))

print("能力值：{:.3f}".format(Factor))

    




