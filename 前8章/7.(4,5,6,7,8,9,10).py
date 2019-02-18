
def pizza():                      #7.4
    materials=[]
    confirm=True
    while confirm:
        material=input("please write down material('quit' to end):")
        if material=='quit':
            confirm=False
            continue
        materials.append(material)


    print("we will add :")
    for _material in materials:
        print(_material)


def movie():           #7.5
    while True:
        age=input("show your age:")
        if age=='quit':
            break
        age=int(age)
        if age <=3:
            print("it's free")
        elif 3 < age <=12:
            print("It takes 10$")
        elif 12<age:
            print("It takes 15$")

def whiletrue():        #7.7
    while True:
        i=1
        
       
def sandwich():
    sandwich_order=['tuna','lemon','bread','egg']  #7.8
    finished_sandwiches=[]
    while True:
        material=sandwich_order.pop()
        print("I have made your {} sandwich".format(material))
        finished_sandwiches.append(material)
        print(sandwich_order)

        if sandwich_order==[]:
            print("we have finish:")
            for finished_sandwich in finished_sandwiches:
                print(str(finished_sandwich)+" sandwich")
            break
                
        

 
def pastrami():   #7.9
    sandwich_order=['pastrami','tuna','pastrami','lemon','bread','egg','pastrami','pastrami']
    print("we have sell-out partrami")
    while 'pastrami' in  sandwich_order:
        sandwich_order.remove('pastrami')
        print(sandwich_order)

    print(sandwich_order)
    

def vocation():  #7.10
    vocations={}
    while True:
        name=input("what's your name")
        vocation=input("a place that you want to go :")
        vocations[name]=vocation

        continue_=input("continue?")
        if continue_=='no':
            break
        

    for name,vocation in vocations.items():
        print( name+" want to go to "+vocation)
        
        
def mountain_poll(): #7.3.3
    responses={}
    polling_active=1
    while polling_active:
        name=input("\nWhat is your name")
        response=input("Which mountain would you like to climb?")

        responses[name]=response

        repeat=input("would you like to let another person respond?(yes/no)")
        if repeat=='no':
            polling_active=False

    print("\n---result---")
    for name,response in responses.items():
        print(name + "   "+response)
        
    
















while True:
    use=input("input a function:")
    if use=='1':
        pizza()
    if use=='2':
        movie()
    if use=='3':
        whiletrue()
        print("you got into a dead cycle")
    if use=='4':
        sandwich()
    if use=='5':
        pastrami()
    if use=='6':
        vocation()
    if use=='7':
        mountain_poll()
