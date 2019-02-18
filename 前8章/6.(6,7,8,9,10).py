favorite_languages={     #6.6
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
    }

for name,language in favorite_languages.items():
    print(name.title()+"'s  "+language.title())


actives=['boob','hook','jen','sarah','friend']   
for active in actives:
    if active in favorite_languages.keys():
        print("Welcome "+active.title()+", thanks of your joining "+favorite_languages[active].title())
    else:
        print(active.title() +", come here ")
    

someone_1={                          #6.7
    'first_name':'Evin', 
    'last_name':'Cryatal',
    'age':23,
    'city':'wuzhou'
    }

someone_2={                          
    'first_name':'Kerb', 
    'last_name':'Annal',
    'age':41,
    'city':'London'
    }

someone_3={                          
    'first_name':'Shrub', 
    'last_name':'Mummy',
    'age':3,
    'city':'Tokyo'
    }

people=[]
people.append(someone_1)
people.append(someone_2)
people.append(someone_3)
print(people)




dog={'name':'Jelly','master':'Chorle'}  #6.8
gold_fish={'name':'Milla','master':'Mummy'}
cat={'name':'Sex','master':'Bare'}

pets=[]
pets.append(dog)
pets.append(cat)
pets.append(gold_fish)
print(pets)


favorite_places={           #6.9
    'honey':['Tokyo','Ououya'],
    'laojv':['dark city'],
    'mianmian':['wuzhou','shanghai','guangzhou']
    }

for keys,values in favorite_places.items():
    print( keys+"  would like to go to ")
    for value in values:
        print(value)





fav_nums={                #6.10    
    'honey':[23,444],
    'evil':[12],
    'marth':[4],
    'white':[233,225]
    }
print(fav_nums)
   

for keys,values in fav_nums.items():
    print(keys+" like")
    for value in values:
       print(value) 


























