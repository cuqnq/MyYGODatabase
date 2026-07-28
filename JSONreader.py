import json


def readJSON():
    '''
    Reads and parses cards_import.json.
    Returns the parsed JSON data when succesful, or an empty list if the file is missing or invalid.
    '''
    try:
        with open("cards_import.json", "r") as file:
            json_data = json.load(file)
            return json_data
    except FileNotFoundError as b:
        print("ERROR: ", b)
        return []  #Purpose of return lines is keep callers' for-loops safe from crashing.
    except json.JSONDecodeError as c:
        print("ERROR! Invalid JSON syntax: ", c)
        return []

