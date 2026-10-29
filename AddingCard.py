import psycopg2
from connect2DB import DB_Connection


def add_card(
    card_name,
    set_code,
    rarity,
    card_type,
    monster_type=None,
    description=None,
    is_normal=False,
    is_effect=False,
    is_fusion=False,
    is_synchro=False,
    is_xyz=False,
    is_link=False,
    is_ritual=False,
    is_pendulum=False,
    is_tuner=False,
    is_flip=False,
    is_gemini=False,
    is_spirit=False,
    is_toon=False,
    is_union=False,
    extra_deck=False,
    spell_trap_type=None,
    level_rank=None,
    monster_attribute=None,
    link_arrows=None,
    link_rating=None,
    pendulum_scale=None,
    attack=None,
    defense=None,
    unknown_atk=False,
    unknown_def=False,
    alternative_art=False,
    overframe=False,
    quantity=1,
    image_url = None
):

    conn, cur = DB_Connection()
    if conn is None:
        return None


    columns = [
        "card_name",
        "set_code",
        "rarity",
        "card_type",
        "monster_type",
        "description",
        "is_normal",
        "is_effect",
        "is_fusion",
        "is_synchro",
        "is_xyz",
        "is_link",
        "is_ritual",
        "is_pendulum",
        "is_tuner",
        "is_flip",
        "is_gemini",
        "is_spirit",
        "is_toon",
        "is_union",
        "extra_deck",
        "spell_trap_type",
        "level_rank",
        "monster_attribute",
        "link_arrows",
        "link_rating",
        "pendulum_scale",
        "attack",
        "defense",
        "unknown_atk",
        "unknown_def",
        "alternative_art",
        "overframe",
        "quantity",
        "image_url"
    ]

    placeholders = ", ".join(["%s"] * len(columns))
    #Placeholders will hold the %s in the columns.

    column_list = ", ".join(columns)
    #Column List will replace all %s with its respective parameter.

    card_info = (
        card_name,
        set_code,
        rarity,
        card_type,
        monster_type,
        description,
        is_normal,
        is_effect,
        is_fusion,
        is_synchro,
        is_xyz,
        is_link,
        is_ritual,
        is_pendulum,
        is_tuner,
        is_flip,
        is_gemini,
        is_spirit,
        is_toon,
        is_union,
        extra_deck,
        spell_trap_type,
        level_rank,
        monster_attribute,
        link_arrows,
        link_rating,
        pendulum_scale,
        attack,
        defense,
        unknown_atk,
        unknown_def,
        alternative_art,
        overframe,
        quantity,
        image_url
    )


    sqlPush = f"INSERT INTO cards ({column_list}) VALUES ({placeholders}) RETURNING id"
    
    try:
        cur.execute(sqlPush, card_info)
        new_id = cur.fetchone()["id"]
        conn.commit()
        return new_id

    except psycopg2.Error as e:
        #Undos half finished INSERT so the database isn't left in a bad state.
        conn.rollback()
        print("ERROR adding card: ", e)
        return None

    finally:
        #Finally runs regardless the try worked or failed, so the connection always closes
        cur.close()
        conn.close()

