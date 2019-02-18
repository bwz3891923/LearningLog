pizzas=['Appo','Knock','Humming']   #4.1
for pizza in pizzas:
    print(pizza)

print("I really like pizza,whatever you say")



animals=['Cat','Dog','Mice']    #4.2
for animal in animals:
    print("a"+str(animal)+"is good for ours life experience")

print("I would like to take them")


for num in range(1,21):   #4.3
    print(num)



nums=list(range(1,1001))  #4.4
print(nums)
for numb in nums:
    numb+=numb
print(numb)

nums_2=list(range(1,21,2))    #4.6
print(nums_2)
for num_2 in nums_2:
    print(num_2)

nums_3=list(range(3,31,3))  #4.7
for num_3 in nums_3:
    print(num_3)


nums_5=[]
nums_4=list(range(1,10))   #4.8
for num_4 in nums_4:
    print(num_4**3)
    nums_5.append(str(num_4**3))
    
print(nums_5)
    
nums_6=[num_6**3 for num_6 in range(1,11)]   #4.9
print(nums_6)
