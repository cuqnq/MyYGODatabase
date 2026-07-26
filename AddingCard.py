import psycopg2

from connect2DB import DB_Connection

conn, cur = DB_Connection()

def add_card(
    card_name,
    set_code,
    rarity,
    card_type,
    monster_type=None,
    is_normal=False,
    is_effect=False,
    is_fusion=False,
    is_synchro=False,
    is_xyz=False,
    is_link=False,
    is_ritual=False,
    is_pendulum=False,
    extra_deck=False,
    spell_trap_type=None,
    level_rank=None,
    monster_attribute=None,
    link_arrows=None,
    pendulum_scale=None,
    attack=None,
    defense=None,
    unknown_atk=False,
    unknown_def=False,
    alternative_art=False,
    overframe=False,
    quantity=1
):

    columns = [
        "card_name",
        "set_code",
        "rarity",
        "card_type",
        "monster_type",
        "is_normal",
        "is_effect",
        "is_fusion",
        "is_synchro",
        "is_xyz",
        "is_link",
        "is_ritual",
        "is_pendulum",
        "extra_deck",
        "spell_trap_type",
        "level_rank",
        "monster_attribute",
        "link_arrows",
        "pendulum_scale",
        "attack",
        "defense",
        "unknown_atk",
        "unknown_def",
        "alternative_art",
        "overframe",
        "quantity"
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
        is_normal,
        is_effect,
        is_fusion,
        is_synchro,
        is_xyz,
        is_link,
        is_ritual,
        is_pendulum,
        extra_deck,
        spell_trap_type,
        level_rank,
        monster_attribute,
        link_arrows,
        pendulum_scale,
        attack,
        defense,
        unknown_atk,
        unknown_def,
        alternative_art,
        overframe,
        quantity
    )

    sqlPush = f"INSERT INTO cards ({column_list}) VALUES ({placeholders})"
    cur.execute(sqlPush, card_info)
    conn.commit()

add_card(
    "Gem-Knight Pearl",
    "BP01-EN031",
    "Common Rare",
    "Monster",
    monster_type="Rock",
    is_xyz=True,
    extra_deck=True,
    level_rank=4,
    monster_attribute="Earth",
    attack=2600,
    defense=1900
)

cur.close()
conn.close()