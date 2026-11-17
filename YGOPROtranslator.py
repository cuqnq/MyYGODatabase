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
    #The CHECK uses YGOPRODeck's wording; the SAVED value uses ours.
    if "Monster" in api_card["type"]:
        card_type = "Monster"
    elif api_card["type"] == "Spell Card":
        card_type = "Spell"
    else:
        card_type = "Trap"

    #---------- MONSTER TYPE or SPELL/TRAP TYPE ----------
    #YGOPRODeck puts BOTH in one field called "race":
    #   Monster -> "race" is the monster type (ex: "Machine", "Dragon")
    #   Spell/Trap -> "race" is the Spell/Trap type (ex: "Counter", "Quick-Play")
    #Both start as None (empty), so both ALWAYS exist no matter which branch runs.
    #Then only the matching one gets filled in. The other stays None.
    monster_type = None
    spell_trap_type = None
    if card_type == "Monster":
        monster_type = api_card["race"]
    else:
        spell_trap_type = api_card["race"]

    #---------- ATTRIBUTE (monsters only) ----------
    #Spells and Traps don't HAVE an "attribute" key at all, utilized .get() statement to return None.
    monster_attribute = api_card.get("attribute", None)

    #---------- SUMMON TYPES, SUBTYPES, NORMAL / EFFECT ----------
    #"typeline" is the card's type line as a list of words, ex:
    #   Jade Dragon Mech -> ["Machine", "Synchro", "Effect"]
    #   Vidolium         -> ["Fairy", "Pendulum", "Effect"]
    #Spells and Traps have no "typeline", btw --> falls into an empty list.
    #With an empty list, every check below is simply False.
    #also from the API as well.
    typeline = api_card.get("typeline", [])

    #Each line asks "is this word in the type line?" and saves True or False.
    #Summoning types
    is_fusion = "Fusion" in typeline
    is_synchro = "Synchro" in typeline
    is_xyz = "Xyz" in typeline or "XYZ" in typeline   #the typeline says "Xyz"; "XYZ" is just in case
    is_link = "Link" in typeline
    is_ritual = "Ritual" in typeline
    is_pendulum = "Pendulum" in typeline

    #Subtypes (the 3rd slot of the type line)
    is_tuner = "Tuner" in typeline
    is_flip = "Flip" in typeline
    is_gemini = "Gemini" in typeline
    is_spirit = "Spirit" in typeline
    is_toon = "Toon" in typeline
    is_union = "Union" in typeline

    #Last slot
    is_normal = "Normal" in typeline
    is_effect = "Effect" in typeline

    #Extra Deck monsters: Fusion, Synchro, Xyz and Link.
    extra_deck = is_fusion or is_synchro or is_xyz or is_link

    #---------- STATS (monsters only) ----------
    #Spells and Traps have none of these keys, so every .get() below gives None for them.

    #Level, or Rank for Xyz monsters. YGOPRODeck calls both "level".
    #Link monsters have no Level at all, so this is None for them.
    level_rank = api_card.get("level", None)

    #Pendulum Scale. Only Pendulum monsters have "scale".
    pendulum_scale = api_card.get("scale", None)

    #Link Rating and Link Arrows. Only Link monsters have these.
    link_rating = api_card.get("linkval", None)

    #YGOPRODeck sends the arrows as a LIST. ( ["Left", "Right", "Bottom-Left"] )
    #The database stores them as ONE piece of text, ex: "Left, Right, Bottom-Left".
    link_markers = api_card.get("linkmarkers", None)
    if link_markers:
        link_arrows = ", ".join(link_markers)
        # ", ".join(list) glues the list together with ", " BETWEEN each item.
    else:
        link_arrows = None

    #ATK and DEF.
    #YGOPRODeck uses -1 for a "?" stat (ex: Slifer the Sky Dragon is ATK ? / DEF ?).
    #We store "?" as: the number left empty (None) + unknown_atk/unknown_def set to True.
    #That's what the sidebar reads to show "?".
    attack = api_card.get("atk", None)
    unknown_atk = attack == -1          #True only when YGOPRODeck sent -1
    if unknown_atk:
        attack = None

    defense = api_card.get("def", None)
    unknown_def = defense == -1
    if unknown_def:
        defense = None

    #Link monsters NEVER have a DEF.
    if is_link:
        defense = None
        unknown_def = False

    #---------- IMAGE ----------
    #card_images is a list of every artwork the card has. [0] = the first (main) artwork.
    card_images = api_card.get("card_images", [])
    if card_images:
        image_url = card_images[0]["image_url"]
    else:
        image_url = None

    #---------- THE RESULTS ----------
    #Left side = add_card()'s parameter name. Right side = where the value comes from.
    return {
        "card_name": api_card["name"],       #YGOPRODeck calls it "name"
        "set_code": set_code,                #from the user
        "rarity": rarity,                    #from the user
        "quantity": quantity,                #from the user
        "description": api_card["desc"],     #YGOPRODeck calls it "desc"
        "card_type": card_type,              #worked out above
        "monster_type": monster_type,        #worked out above (None for Spells/Traps)
        "spell_trap_type": spell_trap_type,  #worked out above (None for monsters)
        "monster_attribute": monster_attribute,  #None for Spells/Traps

        #Summoning types
        "is_fusion": is_fusion,
        "is_synchro": is_synchro,
        "is_xyz": is_xyz,
        "is_link": is_link,
        "is_ritual": is_ritual,
        "is_pendulum": is_pendulum,

        #Subtypes
        "is_tuner": is_tuner,
        "is_flip": is_flip,
        "is_gemini": is_gemini,
        "is_spirit": is_spirit,
        "is_toon": is_toon,
        "is_union": is_union,

        #Normal / Effect and Extra Deck
        "is_normal": is_normal,
        "is_effect": is_effect,
        "extra_deck": extra_deck,

        #Stats
        "level_rank": level_rank,
        "pendulum_scale": pendulum_scale,
        "link_rating": link_rating,
        "link_arrows": link_arrows,
        "attack": attack,
        "defense": defense,
        "unknown_atk": unknown_atk,
        "unknown_def": unknown_def,

        #Card art
        "image_url": image_url,
    }