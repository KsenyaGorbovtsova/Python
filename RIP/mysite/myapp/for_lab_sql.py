import pymysql

"""db=pymysql.connect(
    host="localhost",
    user="dbuser",
    password='0807Ksenya',
    db='musicbands_db'
)

c=db.cursor()
c.execute("insert into bands (name, origin, genre, founding_date, description, image) values (%s, %s, %s, %s, %s, %s);", ('Little Big','Russia, St. Petersburg', 'Rave, rap rave', '2013-07-02', 'Little Big is a Russian rave group, founded in 2013 in St. Petersburg. The set includes Ilya Ilich Prusikin, Sergey Gokk Makarov, Sophia Tayurskaya, Olympia Ivleva and Anton Boo Lissov. The first full-length album, "With Russia From Love" was released on March 17, 2014. Throughout its existence the group has released two albums and three singles.', '/media/band2.jpg' ))
db.commit()

c.execute("select * from bands;")

entries=c.fetchall()

for e in entries:
    print (e)

c.close()
db.close()"""


class Connection:
    def __init__(self, user, password, db, host='localhost'):
        self.user = user
        self.host = host
        self.password = password
        self.db = db
        self._connection = None

    @property
    def connection(self):
        return self._connection

    def __enter__(self):
        self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    def connect(self):
        if not self._connection:
            self._connection = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                db=self.db
            )

    def disconnect(self):
        if self._connection:
            self._connection.close()


class Band:
    def __init__(self, db_connection, name, origin, genre, founding_date, description, image):
        self.db_connection = db_connection.connection
        self.name = name
        self.origin = origin
        self.genre = genre
        self.founding_date = founding_date
        self.description = description
        self.image = image

    def save(self):
        c = self.db_connection.cursor()
        c.execute(
            "insert into bands (name, origin, genre, founding_date, description, image) values (%s, %s, %s, %s, %s, %s);",
            (self.name, self.origin, self.genre, self.founding_date, self.description, self.image))
        self.db_connection.commit()
        c.close()

    def select(self, band_name):
        c = self.db_connection.cursor()
        c.execute("select * from bands where name= %s;", (band_name))
        item = c.fetchone()
        self.name = item[0]
        self.origin = item[1]
        self.genre = item[2]
        self.founding_date = item[3]
        self.description = item[4]
        self.image = item[5]
        c.close()


con = Connection("dbuser", '0807Ksenya', 'musicbands_db')
"""with con:
    band= Band(con, 'Imagine Dragons', 'Las Vegas, Nevada, U.S.', 'Alternative rock', '2008-01-01', 'Imagine Dragons is an American rock band from Las Vegas, Nevada, consisting of lead vocalist Dan Reynolds, lead guitarist Wayne Sermon, bassist and keyboardist Ben McKee, and drummer Daniel Platzman.', '/media/band3.jpg')
    band.save()"""
with con:
    band1 = Band(con, 'Little Big', None, None, None, None, None)
    band1.select('Imagine Dragons')
print(band1.name, band1.origin, band1.description)
