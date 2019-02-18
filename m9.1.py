class Restaurant():#9.1

    def __init__(self,name,*cuisines):
        self.names=name
        self.cuisines=cuisines
        self.capable_user=0

    def open_restaurant(self):
        print(self.names.title()+" is opening")

    def show_cuisine(self):
        print("We offer these today:")
        for cuiseine in self.cuisines:
            print("-"+str(cuiseine))

    def number_served(self,number=0):
        print("There is %i people come here."%number)

    def user_number(self,number_1):
        self.capable_user=number_1

    def increment_number_served(self,increment=0):
        self.capable_user+=increment

    def show(self):
        print("We offer {} people to have dinner".format(self.capable_user))

class IceCreamStand(Restaurant):

    def __init__(self,name,*cuisines):
        super().__init__(name,*cuisines)
        self.flavors=['bread','cream']

    def flavor(self,flavor):
        self.flavors.append(flavor)

    def make_icecream(self):
        print("we make a ice-cream")
        for a in self.flavors:
            print("-%s"%a)



coco=Restaurant('COCO','chaofan','pizza','ice cream')
print(coco.names)
coco.open_restaurant()
coco.show_cuisine()

chaoji=Restaurant('Chaoji','frech fry','sandwich','ice cream','sushi')
print(chaoji.names)
chaoji.open_restaurant()
chaoji.show_cuisine()
chaoji.number_served(100)

chaoji.user_number(5)
chaoji.increment_number_served(10)
chaoji.show()
chaoji.user_number(5)
chaoji.show()

ice=IceCreamStand('ice')
ice.flavor('nutmeg')
ice.make_icecream()
