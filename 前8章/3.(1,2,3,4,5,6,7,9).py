
my_friends=['Amy','Shark','Smug','Kat']
for name in my_friends:
    print(name)   #3.1
    print("How good day is it "+str(name))  #3.2


my_list=['Mura','Mati','Sukima']   #3.3
for Mise in my_list:
    print ("I want to visit "+ Mise)


for inv in my_friends:   #3.4
    print("Hey, I invite you to my party "+inv)



matter=my_friends.pop(1)   #3.5
print("what a pity "+matter+" can not arrive")  
my_friends.insert(1,'UMR')
for inv2 in my_friends:
    print("Hey, I invite you to my party "+inv2)


print("I have found a big table!")    #3.6
my_friends.insert(0,'Knock')
my_friends.insert(int(len(my_friends)/2),'Jeff')
my_friends.append('Keora')
for inv3 in my_friends:
    print("Hey, I invite you to my party "+inv3)

print("I can only invite 2 person")  #3.7
for i in range(len(my_friends)):
    u=my_friends.pop()
    print(u+" no site for you!!")
    if len(my_friends)<=2:
        break


for inv4 in my_friends:
    print("Hey, I invite you to my party "+inv4)
    
del my_friends[0]
del my_friends[0]
print(my_friends)

print(len(my_list))  #3.9
print(len(my_friends))
