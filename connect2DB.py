import os
import psycopg2
import psycopg2.extras
from dotenv import load_dotenv

load_dotenv()

def DB_Connection():
    try:
        conn = psycopg2.connect(
            host = "localhost",
            database = "yugioh_collection",
            user = "postgres",
            password = os.getenv("YGO_Password")
        )
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        
        return conn, cur
    except psycopg2.OperationalError as e:
        print("ERROR: ", e)
        return None, None