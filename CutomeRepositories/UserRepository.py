from Repository.BaseRepository import BaseRepository


class UserRepository(BaseRepository):
    def insert(self,name):
        values = {}
        values["name"] = name
        super().insert("users",values)

