class User():  #9.3

    def __init__(self,first_name="None",last_name="None",**info):
        self.first=first_name
        self.last=last_name
        self.full_name=first_name+"  "+last_name
        self.info=info
        self.login_attempt=0

    def describe_user(self):
        print("%s  %s"%(self.first,self.last))

    def user_info(self):
        if self.info=={}:
            return 0
        for key,value in self.info.items():
            print(key+":"+value)

    def greet_user(self):
        print("Greeting "+self.full_name)

    def increment_login_attempts(self):
        self.login_attempt+=1

    def increment_reset(self):
        self.login_attempt=0
        
class Admin(User):
    def __init__(self,first_name,last_name,**info):
        super().__init__(first_name,last_name,**info)
        self.privileges=['can add post','can delete post','can ban user']
        self.control=Privileges()
        

    def show_privileges(self):
        self.defined=Privileges()
        for i in self.privileges:
            print("You have got the privilage:%s"%i)
        



class Privileges():
    def __init__(self):
        self.privileges=['can add post','can delete post','can ban user']

    def show_privileges(self):
        self.defined=Privileges()
        for i in self.privileges:
            print("You have got the privilage:%s"%i)
        
    




name=User('Alica','Errun',Sex='man',Hobby='swimming')
name.describe_user()
name.user_info()
name.greet_user()

name.increment_login_attempts()
name.increment_login_attempts()
name.increment_login_attempts()
print(name.login_attempt)
name.increment_reset()
print(name.login_attempt)

son=Admin('Linkern','Berry',k='d')
son.show_privileges()
son.control.show_privileges()
