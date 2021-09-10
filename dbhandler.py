import sqlite3


class dbhandler:
    
    def __init__(self,connection):
        self.__connection = sqlite3.connect(connection)

    def search_dork(self,term):
        parameter = ['%'+term+'%']
        list_dorks = self.__connection.execute("select dorkurl from dork where dorkurl like  ? ",parameter)
        for value in list_dorks:
            print(value[0])

    def close_connection(self):
        self.__connection.close()
        


        