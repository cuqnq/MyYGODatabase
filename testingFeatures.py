from AddingCard import add_card
from UpdatingCards import change_quantity

# Make a throwaway test card with quantity 2, so no real card gets touched
test_id = add_card("TEST CARD", "TEST-001", "Common", "Monster", quantity=2)
print("Test card id:", test_id)

# 1. Add 1: should go from 2 to 3
print("1. +1   ->", change_quantity(test_id, 1))
# Expected: {'id': ..., 'quantity': 3, 'deleted': False}

# 2. Remove 1: back to 2
print("2. -1   ->", change_quantity(test_id, -1))
# Expected: {'id': ..., 'quantity': 2, 'deleted': False}

# 3. Remove more than you own: should be rejected, nothing changes
print("3. -5   ->", change_quantity(test_id, -5))
# Expected: None (quantity stays 2)

# 4. Card that doesn't exist
print("4. 9999 ->", change_quantity(9999, 1))
# Expected: None

# 5. Not a number
print("5. abc  ->", change_quantity(test_id, "abc"))
# Expected: an "ERROR changing quantity" message, then None

# 6. Remove exactly what you own: the card should be deleted
print("6. -2   ->", change_quantity(test_id, -2))
# Expected: {'id': ..., 'quantity': 0, 'deleted': True}

# 7. Try to change it again: it's gone now
print("7. +1   ->", change_quantity(test_id, 1))
# Expected: None

'''This file's entire purpose is to test specific functions throughout the project.'''