
m,n=eval(input("输入两个整数，我们可以统计所有的公约数:（ ， ）"))
i=1
M=[]
N=[]




while True:
    if n%i==0:
        print(i)
        N.append(i)

    if m%i==0:
        print(i)
        M.append(i)

    i+=1


    if i>=n and i>=m:
        break

        
print(M+N)


M+=N
for j in range(len(M)):
    for u in range(len(M)):
        if M[j]==M[u]:
            del M[u]
            print(M)


    
