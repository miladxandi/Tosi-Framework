import pymysql
class DBConnection:
    user_name = "root"
    password = ""
    def connect(self,query):
        connection = pymysql.connect(
            host="localhost",
            user=self.user_name,
            passwd=self.password,
            database="rotic_test")
        cursor = connection.cursor()

        cursor.execute(query)
        rows = cursor.fetchall()
        # some other statements  with the help of cursor
        connection.commit()
        connection.close()

        return rows

