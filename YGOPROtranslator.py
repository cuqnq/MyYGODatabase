#Turns ONE card from YGOPRODeck's data into a dictionary that matches add_card()'s parameters.
#
#   api_card = one card's dictionary from YGOPRODeck (has "name", "type", "desc", "race", ...)
#   set_code, rarity, quantity = the user's choices (YGOPRODeck doesn't know which printing
#                                you own or how many copies you're adding)
#
#Returns a dictionary whose keys match add_card()'s parameter names EXACTLY,
#so it can be passed straight into add_card() later.
def translate_card(api_card, set_code, rarity, quantity):
    #---------- CARD TYPE: "Monster", "Spell" or "Trap" ----------
    #YGOPRODeck's "type" is detailed (ex: "Synchro Monster", "Trap Card"),
    #but our database only stores 3 simple values.
    #The CHECK uses YGOPRODeck's wording; the SAVED value uses ours.
    if "Monster" in api_card["type"]:
        card_type = "Monster"
    elif api_card["type"] == "Spell Card":
        card_type = "Spell"
    else:
        card_type = "Trap"

    #----------- The Prototype -----------------
    #Left side = add_card()'s parameter names.
    #Right side = where the value comes from within the YGOPRODECK API.
    #(This return is lined up with the "if", so it runs for EVERY card, not just monsters.
    return {
            "card_name": api_card["name"], #YGO api
            "set_code": set_code, #from the user
            "rarity": rarity, #from the user
            "quantity": quantity, #from the user
            "description": api_card["desc"], #YGO api
            "card_type": card_type,
    }


