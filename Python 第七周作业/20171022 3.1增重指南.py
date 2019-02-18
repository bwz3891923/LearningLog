import math

earth=float(input("你的体重啊啊啊啊KG:  "))
year=eval(input("你要过多久啊啊啊Y :  "))

if year>80:
    print("拜托，你活不了那么久")
    exit()


factor= 0.5
for i in range(year):
    earth += 0.5
    moon= 0.165*earth

print("你在地球重{:.2f} Kg,在月球{:.2f} Kg".format(earth,moon))
