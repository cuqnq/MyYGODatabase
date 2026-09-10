import psycopg2

from connect2DB import DB_Connection
from JSONreader import readJSON

conn, cur = DB_Connection()


user_card = input("What card do you want to search?\n")


