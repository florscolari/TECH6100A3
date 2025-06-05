import random


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
idF = generate_short_id(flight)

user = "user"
idU = generate_short_id(user)
print(idU)

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

from datetime import date

def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year
    return age

birth_date = date(1990, 5, 15) # Example birth date
age = calculate_age(birth_date)
print(f"Age: {age}")
print(type(birth_date))

#todo: when ask for date of birth: ask for dob.day = input('day'), then dob.month = input('month'), then dob.year =
# input('year'). wrap all up as dob = date(dob.year, dob.month, dob.day)