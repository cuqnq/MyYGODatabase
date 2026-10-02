import requests
from JSONreader import readJSON
from AddingCard import add_card

YGOPRODECK_URL = "https://db.ygoprodeck.com/api/v7/cardinfo.php"

def get_image_urls(card_names):
    unique_names = "|".join(sorted(set(card_names)))
    response = requests.get(YGOPRODECK_URL, params={"name": unique_names})
    response.raise_for_status()
    data = response.json()["data"]

    image_lookup = {}
    for card in data:
        image_lookup[card["name"]] = card["card_images"][0]["image_url"]
    return image_lookup


def import_cards():
    cards = readJSON()
    if not cards:
        print("No cards found in cards_import.json.")
        return

    card_names = [card["card_name"] for card in cards]
    image_lookup = get_image_urls(card_names)

    for card in cards:
        image_url = image_lookup.get(card["card_name"])
        if image_url is None:
            print(f"WARNING: no image found for '{card['card_name']}'")

        new_id = add_card(
            card_name=card["card_name"],
            set_code=card["set_code"],
            rarity=card["rarity"],
            card_type=card["card_type"],
            monster_type=card["monster_type"],
            is_normal=card["is_normal"],
            is_effect=card["is_effect"],
            is_fusion=card["is_fusion"],
            is_synchro=card["is_synchro"],
            is_xyz=card["is_xyz"],
            is_link=card["is_link"],
            is_ritual=card["is_ritual"],
            is_pendulum=card["is_pendulum"],
            extra_deck=card["extra_deck"],
            spell_trap_type=card["spell_trap_type"],
            level_rank=card["level_rank"],
            monster_attribute=card["monster_attribute"],
            link_arrows=card["link_arrows"],
            pendulum_scale=card["pendulum_scale"],
            attack=card["attack"],
            defense=card["defense"],
            unknown_atk=card["unknown_atk"],
            unknown_def=card["unknown_def"],
            alternative_art=card["alternative_art"],
            overframe=card["overframe"],
            quantity=card["quantity"],
            image_url=image_url
        )
        print(f"Added '{card['card_name']}' with id {new_id}")


if __name__ == "__main__":
    import_cards()