import random
import uuid


from uuid import uuid1, uuid3

import uuid

def generate_short_id(item_type):
    item_type = item_type.lower()
    if item_type == "user":
        return f"C{uuid.uuid4().hex[:4]}"  # First 4 characters of the UUID
    elif item_type == "flight":
        return f"F{uuid.uuid4().hex[:4]}"
    else:
        pass

flight = "flight"
id = generate_short_id(flight)
print(id)

def generate_seat_number():
    """Generate Assigned Seat when booking"""
    seat_letter = ['A', 'B', 'C', 'D', 'E', 'F']
    seat_number = list(range(1, 30))

    #Taking random letter & random numbers
    random_letter = random.choice(seat_letter)
    random_number = random.choice(seat_number)

    # Concatenate both
    flight_seat = random_letter + random_number
    return flight_seat