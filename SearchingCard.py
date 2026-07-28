import psycopg2
from JSONreader import readJSON
from connect2DB import DB_Connection

conn, cur = DB_Connection()

def cardSearcher():
    looking = readJSON()
    print("card is searched!")



'''
File should be able to search by a combination of parameters listed in AddingCard. (card_name, extra_deck, rarity, etc).
Except quantity, that will be sorted by either greatest amount or least amount.
No exact match, would be easier for the user if it's partial fuzzy.
Not case sensitive, the search algorithm will lowercase all of the user's inputs before commiting to the search.

Typeahead search? Is that possible with no UI? Or that will be a future feature. 



'''