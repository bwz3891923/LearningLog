import json
import pygal
from countries_codes import *
from pygal.style import RotateStyle as RS

def main(year):
    x,y,z={},[],[]
    filename='population_data.json'
    with open(filename) as f:
        datas=json.load(f) 

    for data in datas:
        if data['Year']==year:
            country_name=data['Country Name']
            country_code=get_country_code(country_name)
            population=int(float(data['Value']))
            if country_code:
                x[country_code]=population
                z.append(country_code)
            else:
                y.append(country_name)
    

    

    return(x,y,z,year)

def classify(dict_0):
    group1,group2,group3={},{},{}
    for cc,pop in dict_0.items():
        if pop <10e7:
            group1[cc]=pop
        elif pop <10e8:
            group2[cc]=pop
        else:
            group3[cc]=pop

    return(group1,group2,group3)
        
    

def plot(year,pop1,pop2='',pop3=''):
    wm_style=RS('#336655')
    wm = pygal.Worldmap(style=wm_style)
    wm.title='Population of The World'

    if pop2 and pop3 :
        wm.add('0-10m',pop1)
        wm.add('10m-1bn',pop2)
        wm.add('>1bn',pop3)

    else :
        wm.add(year,pop1)

    


    wm.render_to_file("World Population %s.svg"%year)

    
            
        

(dict_0,cc,cn,year)=main('2008')
(k1,k2,k3)=classify(dict_0)

plot(year,k1,k2,k3)








