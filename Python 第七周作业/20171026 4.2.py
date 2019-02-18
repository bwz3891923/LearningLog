
go=input("输入一段文字吧：")

alp,num,oth=0,0,0
for i in range(len(go)):
    if "a" <= go[i] <= "z" or "A" <= go[i] <="Z" :
        alp+=1
    elif "0" <= go[i] <= "9":
        num+=1
    else:
        oth+=1


print("有{}个字母，{}个数字，{}个其他字符".format(alp,num,oth))
