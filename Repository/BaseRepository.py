#!C:\Users\Hossein\AppData\Local\Programs\Python\Python38\python.exe
from Core.DBConnection import DBConnection
class BaseRepository():
    def insert(self,table,table_values):
        db = DBConnection()
        keys = ""
        values= ""
        counter = 0
        for key , value in table_values.items():
            if counter > 0:
                keys = keys+", "+key
                values = values +", "+ "'"+str(value)+"'"
            else:
                keys = keys+key
                values = values + "'" + str(value) + "'"
            counter = counter + 1


        query = "INSERT INTO " +\
                table + " (" + keys + ")" +  " VALUES (" +values+");"
        #print (query)
        db.connect(query)

    def getCount(self,table):
        db  = DBConnection()
        query = "SELECT Count(*)" \
                " FROM " + table
        #query = "SELECT * FROM " + table+";"
        print(query)
        result = db.connect(query)
        return result[0][0]

    def findbyID(self,table,id):
        db  = DBConnection()

        query = "SELECT * FROM " + table +" WHERE "+\
                "id=" + str(id) + ";"
        print(query)
        result = db.connect(query)
        return result

br = BaseRepository()
# user1 = {
#     "name" : "ali" ,
#     "id" : 2
# }
#
# br.insert("users",user1)
length = br.getCount("users")
print(length)

# result = br.findbyID("users",2)
# print(result[0][0])



