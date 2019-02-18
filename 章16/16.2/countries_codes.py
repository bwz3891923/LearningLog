from pygal.i18n import COUNTRIES


def get_country_code(country_name):
    for code,name in COUNTRIES.items():
        if name==country_name:
            return code

def treat_unnamed_code(codes):
    x={}
    for code,name in COUNTRIES.items():
        if code not in codes:
            x[code]=name
    return x

       
        
