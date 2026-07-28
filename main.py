import psycopg2

from connect2DB import DB_Connection
from JSONreader import readJSON

conn, cur = DB_Connection()


data = readJSON()
print(data)


