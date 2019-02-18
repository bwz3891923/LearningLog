users=['admin','log','erwen','shifang','wumao']  #5.8
for user in users:
    if user=='admin':
        print("御主人様ようこそ"+user.title())
    else:
        print("Hi there!"+user.title())


users.clear()   #5.9
if users==[]:
    print("we need some users!!")




current_users=['admin','log','erwen','shifang','wumao']   #5.10
new_users=['laoE','admin','laoju','mianmian','KB']

for new_user in new_users:
    if new_user.lower() in current_users:
        print(new_user.title()+"  You have been logging in")
    else:
        print(new_user.title()+" has not been used")



nums=list(range(1,10))   #5.11
print(nums)
for i in nums:
    if i==1:
        print("1st")
    elif i==2:
        print("2nd")
    elif i==3:
        print("3rd")
    else:
        print(str(i)+"th")

    
