import json
from pygal.i18n import COUNTRIES
from countries_codes import get_country_code


filename='population_data.json'
with open(filename) as f:
    pop_data=json.load(f)

for pop_dict in pop_data:
    if pop_dict['Year']=='2010':
        country_name=pop_dict['Country Name']
        code=get_country_code(country_name)
        population=int(float(pop_dict['Value']))
        if code:
            print(code+" : "+str(population))
        else:
            print('Error -'+country_name)


