tran=input("请输入货币值（美元USD，人民币CNY）:")

if tran[-1] in ['d','D']:
    cyn=6*float(tran[0:-3])
    print("货币转换为：%.2f CYN"%cyn)

elif tran[-1] in ['y','Y']:
    usd =float(tran[0:-3])/6
    print("货币转换为：%0.2f USD"%usd)


else:
    print("error")
