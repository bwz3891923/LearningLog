
def magic(name_1):
    print("Hello! "+name_1)

def make_great(name_0,name_1):
    ACTIVE=1
    while ACTIVE:
        full_name="The Great "+name_0.pop()
        name_1.append(full_name.title())
        print(name_0)
        print(name_1)
        if name_0==[]:
            ACTIVE=0

def show_magician(name):
    for i in name:
        print("WOW! "+i)

def sandwich(*materials):
    print("we have made a sandwich of :")
    for material in materials:
        print("- "+ str(material))

def user_profile(first,last,**user_info):
    profile={}
    profile['first_nmae']=first
    profile['last_name']=last
    for key,value in user_info.items():
        profile[key]=value
    return profile

        
    
def car_maker(maker,model,**info):
    profile={}
    profile['maker']=maker
    profile['model']=model
    for key,value in info.items():
        profile[key]=value
    return(profile)










while True:
    i = input("Select a function:  ")
    if i=='quit':
        exit()
    if i=='8.9':
        magician=['even','shoud','colk','academy']
        for name in magician:
            magic(name)
    if i=='8.10':
        magician=['even','shoud','colk','academy']
        magician_cov=[]
        make_great(magician,magician_cov)
        show_magician(magician_cov)
    if i=='8.11':
        magician=['even','shoud','colk','academy']
        magician_cov=[]
        make_great(magician[:],magician_cov)
        show_magician(magician_cov)
        print(magician)
    if i=='8.12':
        sandwich('carrot','cheese','rabit')
        sandwich('maze','cheese','meat')
    if i=='8.13':
        profile=user_profile('Luo','Mai',location='Wuzhou',
                             field='Material',sex='mMen',Hobby=['Piano','game'])
        print(profile)
    if i=='8.14':
        car_detail=car_maker('东风风光','580',color='blue',
                             power='102KW',lenth='4680/1845/1715')
        print(car_detail)
        

