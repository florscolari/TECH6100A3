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

def calculate_age(dob):
    """Calculates age based on date of birth with an object of class date(yyyy, m, dd)"""
    today = date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return age

birth_date = date(1990, 5, 15) # Example birth date
age = calculate_age(birth_date)
print(f"Age: {age}")
print(type(birth_date))

def login_user(username):
    print(f'{username} successfully logged in!!')
def check_password(password):
    if password == '1234':
        return True
    else:
        return False
username = input('Enter username')
password = input('Enter password')
try:
    if not check_password(password):
        raise ValueError
except ValueError:
    print('Wrong Password! Try again!')
else:
     login_user(username)

def hash_password(password):
    """Handles passwords with hash technique instead of storing it as plain text"""
    return hashlib.sha256(password.encode()).hexdigest()



#1 Clean user list & add testing user type agent
#2 Test OK email & OK password -> outcome: user
#3 Test WRONG email & OK password -> outcome: None
#4 Test OK email & WRONG password -> outcome: None