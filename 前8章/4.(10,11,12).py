nums_1=[num_6**3 for num_6 in range(1,11)]      #4.10
print(nums_1)
print("The first three items in the list are:"+str(nums_1[:3]))
print("The last three items in the list are:"+str(nums_1[-3:]))
print("The items from the middle of the list are:"+str(nums_1[4:7]))


pizzas=['Appo','Knock','Humming']   #4.11
for pizza in pizzas:
    print(pizza)

print("I really like pizza,whatever you say")

friend_pizzas=pizzas[:]
pizzas.append('Jackic')
friend_pizzas.append('Shroud')

print("My favorite pizza is :")
for pizza in pizzas:
    print(pizza)
print("My firend's favorite pizza is :")
for friend_pizza in friend_pizzas:
    print(friend_pizza)
