
car=input("What kinds of cars would you like: ")   #7.1
print("I can help you find the {}".format(car))

party=int(input("How  many people take part:") )#7.2
if party>8:
    print(" Not enough site")
else:
    print("Enjoy yourself")

nums=int(input("select a numbers"))  #7.3
if nums%10==0:
    print(str(nums)+" is a number that can be devide by 10")
