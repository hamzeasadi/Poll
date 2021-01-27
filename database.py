import psycopg2 as pg
import numpy as np



db_info = {'database': 'myDatabase', 'user': 'postgres', 'port': '5432',
           'host': 'localhost', 'password':'hamze95123'}

tbl_info = {'filed1': 'ID INT PRIMARY KEY NOT NULL', 'filed2': 'NAME TEXT NOT NULL',
            'filed3': 'LAST_NAME TEXT NOT NULL', 'filed4': 'EMAIL TEXT',
            'filed5': 'STUDNET_NUMBER INT NOT NULL'}

class Database():
    """we will create a simple a database manipulation class"""
    def __init__(self, **db_info):
        super().__init__()
        self.db_info = db_info
        self.con = self.check_connection()

    def check_connection(self):
        try:
            conn = pg.connect(database=self.db_info['database'], host=self.db_info['host'],
                              port=self.db_info['port'], user=self.db_info['user'],
                              password=self.db_info['password'])
        except Exception as e:
            print(e)
        else:
            print("the connection was successfull")
            return conn

    def createTable(self, tbl_name, **tbl_info):
        fields_list = list(tbl_info.values())
        fields = ", ".join(fields_list)
        create_table = f"CREATE TABLE {tbl_name}({fields})"
        # return create_table
        cur = self.con.cursor()
        cur.execute(create_table)
        cur.close()
        self.con.commit()
        self.con.close()

    def deleteTable(self, tbl_name):
        delete_table = f"DROP TABLE {tbl_name}"
        cur = self.con.cursor()
        cur.execute(delete_table)
        cur.close()
        self.con.commit()
        self.con.close()

    def readData(self, tbl_name, *fields):
        field = ", ".join(fields)
        command = f"SELECT {field} FROM {tbl_name}"
        cur = self.con.cursor()
        cur.execute(command)
        rows = cur.fetchall()
        cur.close()
        return rows

    def insertdata(self, tbl_name, **data):
        pass



dbman = Database(**db_info)
# dbman.createTable('STUDENT', **tbl_info)
# dbman.deleteTable('STUDENT')

# read_field = ['ID', 'NAME']
# rows = dbman.readData('employee', *read_field)
# for data in rows:
#     print(f'name={data[1]} ID={data[0]} Eemail={data[2]}')



# # cur.execute("INSERT INTO Employee (ID, NAME, EMAIL) VALUES(2, 'John', 'John@gmail.com')")
