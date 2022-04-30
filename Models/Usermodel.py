from CutomeRepositories.UserRepository import UserRepository


class Usermodel():

    def __init__(self, name):
        self.name = name

    def insert(self):
        ur = UserRepository()
        ur.insert(self.name)



