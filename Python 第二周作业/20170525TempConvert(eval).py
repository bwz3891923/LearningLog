val=input("please imput a tempreture with symbol (exp.32F):")

if val[-1] in ['c','C']:
    f=1.8*eval(val[0:-1])+32
    print("converted tempreture is :%.2fF"%f)
elif val[-1] in ['f','F']:
    c =(eval(val[0:-1])-32)/1.8
    print("converted tempreture is :%.2fC"%c)
else:
    print("error")
    
    
