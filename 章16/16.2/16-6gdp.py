import json
import countries_codes as cc
from pygal.style import LightColorizedStyle as LCS,RotateStyle as RS
import pygal

def main(year=2010):
    filename='gdp_json.json'
    with open(filename) as f:
        datas=json.load(f)

    x={}
    for data in datas:
        if data['Year']==year :
            country=data['Country Name']
            gdp=data['Value']
            code=cc.get_country_code(country)

            if code:
                x[code]=gdp



    return x

def plot(locate):
    wm=pygal.Worldmap()
    wm.title='Gdp of 2016'
    wm.add('2016',locate)
    wm_style=RS('#336699',base_style=LCS)

    wm.render_to_file('gdp_2016.svg')
    
    

                

            

    





plot(main(2016))

