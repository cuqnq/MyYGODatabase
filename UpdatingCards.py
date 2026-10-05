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


def change_quantity(card_id, change):
    """
    Add to or remove from a card's quantity by `change` (e.g. +1 or -2).
    If the quantity reaches 0, the card is deleted.
    Returns {"id", "quantity", "deleted"}, or None if the card doesn't exist
    or the change would make the quantity negative.
    """
    conn, cur = DB_Connection()
    if conn is None:
        return None

    try:
        #1) Add the change to the CURRENT quantity, but only if the
        # result stays 0 or higher. If not, nothing matches and nothing changes.
        sql_change = """
            UPDATE cards
            SET quantity = quantity + %s
            WHERE id = %s AND quantity + %s >= 0
            RETURNING quantity
        """

        # "change" appears twice in sql_change, so it appears twice in the tuple
        # General idea of the placeholders(%s) in sql_change:
        # 1st %s = change (the math)
        # 2nd %s = card_id (the specific card)
        # 3rd %s = change (the "won't go below 0" check)
        cur.execute(sql_change, (change, card_id, change))
        row = cur.fetchone()

        #If no row returns, the card either doesn't exist or the card amount goes below 0.
        if row is None:
            conn.rollback()
            return None

        new_quantity = row["quantity"]
        deleted = False #becomes True only if the card is deleted below

        #2) If the quantity hit 0, remove the card entirely
        if new_quantity == 0:
            cur.execute("DELETE FROM cards WHERE id = %s", (card_id,)) #Be aware that this is a tuple (trailing comma)
            deleted = True                            #cur.execute requires a tuple of values, even for just one value

        #3) Save BOTH statements together (one transaction)
        conn.commit()
        return {"id": card_id, "quantity": new_quantity, "deleted": deleted}

    except psycopg2.Error as e:
        # Undo BOTH statements if anything failed
        conn.rollback()
        print("ERROR changing quantity: ", e)
        return None

    finally:
        cur.close()
        conn.close()