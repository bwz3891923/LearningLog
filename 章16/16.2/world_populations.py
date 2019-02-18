import json
import pygal
from countries_codes import *

def main():
    x,y,z={},[],[]
    filename='population_data.json'
    with open(filename) as f:
        datas=json.load(f)

    for data in datas:
        if data['Year']=='2009':
            print(data)
            country_name=data['Country Name']
            country_code=get_country_code(country_name)
            population=int(float(data['Value']))
            if country_code:
                x[country_code]=population
                z.append(country_code)
            else:
                y.append(country_name)
    

    return(x,y,z)


def plot(popl):
    wm = pygal.Worldmap()
    wm.title='Population of Countries in North Amercia'
    wm.add('2010',popl)
    wm.render_to_file('World Population 2009.svg')

    
            
        

(x,y,z)=main()

plot(x)

