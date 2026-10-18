from AddingCard import add_card

new_id = add_card("TEST TUNER", "TEST-002", "Common", "Monster",
                  monster_type="Dragon", is_synchro=True, is_tuner=True,
                  is_effect=True, extra_deck=True, level_rank=7,
                  attack=2500, defense=2000)
print("New card id:", new_id)