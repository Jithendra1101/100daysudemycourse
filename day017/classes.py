class user:
    def __init__(self,id,name):
        print("new user with name ",self,"is created")
        self.id = id
        self.name = name
    def __str__(self):
        return self.name
user_1 = user(559,"jithendra")    
print(user_1.id,user_1.name)