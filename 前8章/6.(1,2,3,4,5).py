

someone={                           #6.1
    'first_name':'Evin', 
    'last_name':'Cryatal',
    'age':23,
    'city':'wuzhou'
    }
print(someone)


fav_nums={                     #6.2
    'honey':23,
    'evil':12,
    'marth':4,
    'white':233
    }
print(fav_nums)

meaning={                     #6.3,4
    'in':'something in the list' ,
    'of':'somrthing from a list ',
    'print':'display the defined context  ',
    'for':'a beginning of a recycle '
    }

for i in meaning:
    print(i+"  "+meaning[i])


rivers={                   #6.5
    'Changjiang':'ChongQing',
    'Huanghe':'LanZhou',
    'XiJiang':'WuZhou'
    }

for river in rivers:
    print("The {} runs through {}".format(river,rivers[river]))
    
