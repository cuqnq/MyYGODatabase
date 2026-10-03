import psycopg2
from connect2DB import DB_Connection

'''Add comments the next time you see this to wrap your mind around it more clearer.'''

def update_quantity(card_id, quantity):
    conn, cur = DB_Connection()
    if conn is None:
        return None

    try:
        sql_update = "UPDATE cards SET quantity = %s WHERE id = %s RETURNING *"
        updateTuple = (quantity, card_id)
        cur.execute(sql_update, updateTuple)
        rowZ =  cur.fetchone() #rowZ will need a new name for sure...
        conn.commit()

        if rowZ is None:
            return None
        return dict(rowZ)

    except psycopg2.Error as e:
        conn.rollback()
        print("ERROR updating data: ", e)
        return None

    finally:
        cur.close()
        conn.close()