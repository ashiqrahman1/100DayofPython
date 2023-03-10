# Creating class
"""
class <ClassName>:



# create constructor in class
class <ClassName>:
    def __init__(self):
        #Initialise Attribute


# Creating Methods

class <ClassName>:
    def __init__(self):
        --------
    def MethodName():
        --------
"""


class User:
    def __init__(self, id, name):
        self.uid = id
        self.uname = name
        self.followers = 0
        self.following = 0
        # print(f"New User {self.uname} Created")

    def follower(self, user):
        user.followers += 1
        self.following += 1
    # def getUser(self):
    #     print(f"Your ID: {self.uid} and Name is : {self.uname}")


user1 = User(1, "Ashik")
user2 = User(2, "Aslah")
# print(user1.uid)
user1.follower(user2)
# user2.follower(user1)
print(f"User1 Followers : {user1.followers} Following = {user1.following}")
print(f"user2 Followers : {user2.followers} Following = {user2.following}")
