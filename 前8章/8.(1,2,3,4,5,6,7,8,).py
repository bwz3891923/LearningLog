def display_message():   #8.1
    print("Hello world")

def favorite_book(book):   #8.2
    print("My favorite book is "+book.title())

def make_shirt(size,letter_type): 
    print("you got a {} feet shirt of '{}'".format(size,letter_type))  #8.3
    print("you got a {} feet shirt of '{}'".format(size,letter_type.title())) #8.4


def describe_city_pro():  #8.5
    cities={
        'Beijing':'China',
        'Tokyo':'Japan',
        'New York':'USA'
        }
    for u in cities.keys():
        describe_city(u,cities[u])

def describe_city(city,country):#8.6
    print(city+" belong to "+country)



def city_country(city,country):
    full=city+"  "+country
    return(full)

    
def greeter():
    print("hello")
        
            
def pets(animal,name):
    print("\n I have a "+animal+".")
    print("My "+animal+"'s name is "+name.title()+".")

def pets_1(animal='hamster',name='chorome'):
    print("\n I have a "+animal+".")
    print("My "+animal+"'s name is "+name.title()+".")


def make_album(singer,album,song=''):  #8.7 8.8
    if song=='':
        OK_album={'name':singer,'album':album}
    else :
        OK_album={'name':singer,'album':album,'song':song}
    return(OK_album)


while True:
    i = input("Select a function:  ")
    if i=='quit':
        exit()
    if i=='8.1':
        display_message()
    elif i=='8.2':
        article=input("your favorite book is ?")
        favorite_book(article)
    elif i=='8.3'or i=='8.4':
        size=input("your zise?")
        letter_type=input("your type?")
        make_shirt(size,letter_type)
    elif i=='8.5':
        describe_city_pro()
    elif i=='8.6':
        full_detail=city_country('Wuzhou','China')
        print(full_detail)
        full_detail=city_country('Tokyo','Japan')
        print(full_detail)
    elif i=='8.7':
        album=[]
        make_album_OK_1=make_album('Taylor','Reputation')
        make_album_OK_2=make_album('Taylor','Wildest Dreams',7)
        make_album_OK_3=make_album('DECCA','Ultimate Classical Piano','many')
        album.append(make_album_OK_1)
        album.append(make_album_OK_2)
        album.append(make_album_OK_3)
        print(album)
    elif i=='8.8':
        album_collect=[]
        while True:
            name=input("Input a singer's name ")
            if name=='q':
                break
            album=input("Input a album")
            songs=input("How many song?")
            make_album_OK=make_album(name,album,songs)
            album_collect.append(make_album_OK)
        print(album_collect)

            
#***************************************************************************#
    elif i=='greeter':
        greeter()
    elif i=='pets':
        pets('cat','shall')
        pets('dog','swit')
        pets(name='chorome',animal='hamster')
    elif i=='pets_1':
        pets_1()
        pets_1('mice','jelly')
        

        


        
