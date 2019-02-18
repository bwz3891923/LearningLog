

back=list(input("输入一个数字呗："))
print("{}".format(back))

p=0

for i in range(len(back)):
    if back[i]==back[-i-1]:
        print("right")
        p+=1
    else :
        print("false")

if p==len(back):
    print("这是一个回文数")

else:
    print("这是个P回文数")
