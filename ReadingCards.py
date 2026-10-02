import psycopg2
from connect2DB import DB_Connection

def get_all_cards():
    conn, cur = DB_Connection()
    if conn is None:
        return []

    cur.execute("SELECT * FROM cards ORDER BY id")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return [dict(row) for row in rows]

'''REMINDER: Add comments to explain what this file do'''