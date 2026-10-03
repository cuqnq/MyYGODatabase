import psycopg2
from connect2DB import DB_Connection

def del_cards():
    conn, cur = DB_Connection()
    if conn is None:
        return None

    try:
pass