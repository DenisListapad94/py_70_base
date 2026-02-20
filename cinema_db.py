import sqlite3
from dataclasses import dataclass
# connection = sqlite3.connect("cinema.db")
cinema = "cinema.db"
actors_table = "actors"
actors = [
    ("Rene","Zelveger",56,"f"),
    ("Rese","Wizerspoon",54,"f")
]

# query = """
# insert into actors (name,surname,age,sex) values (?,?,?,?)
# """
# # query = "select * from actors"
#
# with sqlite3.connect(cinema) as connection:
#     cursor = connection.cursor()
#
#     data  = cursor.executemany(query,actors)
#     connection.commit()


@dataclass
class Actor:
    name: str
    surname: str
    age: int
    sex: str

actor = Actor("Pirs","Brosnan",62,"m")



class SQLiteEngine:
    def __init__(self,db_name):
        self.db_name = db_name

    @property
    def connection(self):
        with sqlite3.connect(self.db_name) as conn:
            return conn


class SQLActorManager:
    def __init__(self,db_name,table_name = actors_table):
        self.db_name = db_name
        self.table_name = table_name

    @property
    def connection(self):
        with sqlite3.connect(self.db_name) as conn:
            return conn


    def cursor(self,conn):
        return conn.cursor()

    def read_all(self,conn) -> list[Actor]:

        data = self.cursor(conn).execute(f"select * from {self.table_name}")
        return [Actor(*item[1:]) for item in data]

    def create(self,conn,actor:Actor):
        self.cursor(conn).execute(f"insert into {self.table_name} (name,surname,age,sex) values (?,?,?,?)" , tuple(actor.__dict__.values()))
        conn.commit()

    def read_one(self,conn,item_id):
        data = self.cursor(conn).execute(f"select * from {self.table_name} where actor_id = {item_id}")
        print(data.fetchone())

    def update(self, conn, age, item_id):
        self.cursor(conn).execute(f"UPDATE {self.table_name} SET age = ? WHERE actor_id = ?",(age,item_id))
        conn.commit()

    def delete(self,conn,item_id):
        self.cursor(conn).execute(f"DELETE FROM {self.table_name} WHERE actor_id = '%s'" , "actor_id")
        conn.commit()

manager = SQLActorManager(cinema)
manager.delete(manager.connection,actor)


