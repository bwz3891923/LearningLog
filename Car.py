class Car():

    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descriptive_name(self):
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" mile on it")


    def update_odometer(self,mileage):
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("you can't roll back an odometer")

    def increment_odometer(self,miles):
        if miles <0:
            print("you can't roll bcak")
        else:
            self.odometer_reading += miles

    def fill_gas_tank(self):
        print("This car has a gas tank of 150L") 
        

class ElectricCar(Car):

    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_1=Battery()
        self.battery_size=70

    def ElectBattery(self):
        print("this ElectricCar's battery is "+str(self.battery_size)+"-KWh")

    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")
        
    

class Battery():
    
    def __init__(self,battery_size_1=75):
        self.battery_size=battery_size_1

    def describe_battery(self):
        print("This car has a "+str(self.battery_size)+" -kWh battery")


    def get_range(self):
        if self.battery_size==75:
            _range= 240
        elif self.battery_size==85:
            _range=270
        print(_range)
        return _range
    
    def upgrade_battery(self):
        self.battery_size=85


my_car=Car('audi','a4',2016)
print(my_car.get_descriptive_name())

my_car.odometer_reading=23  #直接修改
my_car.read_odometer()

my_car.update_odometer(50)  #间接修改
my_car.read_odometer()

my_car.update_odometer(27)  #禁止回拨
my_car.read_odometer()

my_car.increment_odometer(-100)
my_car.increment_odometer(100)
my_car.read_odometer()

my_tesla=ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.ElectBattery()
my_tesla.fill_gas_tank()

my_tesla.battery_1.describe_battery()
my_tesla.ElectBattery()

_range=my_tesla.battery_1.get_range()
print(_range)
my_tesla.battery_1.battery_size=85
_range=my_tesla.battery_1.get_range()
print(_range)

new_car=ElectricCar('AUTO','SAIN',2017)
new_car.battery_1.upgrade_battery()
new_car.battery_1.describe_battery()
new_car.battery_1.get_range()

