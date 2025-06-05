# TECH6100 Assessment 3 Florencia Scolari ID 1847863 June 2025
# Check the full project and references on the GitHub Public Repo https://github.com/florscolari/TECH6100A3.git

# User for Testing Purposes:
#todo: update testing user

# First Name: Elle
# Last Name: Test
# Username: test2025
# Email: test@t.com.au
# Password: 123
# Order ID: 0011122

# Out of scope:
#todo: update out of scope section

# 1. Global command to cancel an ongoing task.
# 2. No user input validation for: phone, email & shipping address.
# 3. Turning back for case: If user selects she/he has an account and doesn't know username & password, no way to recover from that. Dead End.
# 4. Login as different user types at tge beginning. You can create account & login to place an order.
# 5. Although I have set __str__ & __repr__ for Book, Order & User, I've used __str__ in most cases instead of __repr__


# PEP 8 Naming Conventions:
# Variable name: lowercase_with_underscores - user_name
# Function name: verb_lowercase_underscore - send_email()
# Class name: CapitaliseWords - UseNouns

import uuid #to generate unique ids
import hashlib #to handle passwords in a safer manner
from datetime import datetime #to set datestamp when booking a flight
import random #to create random combinations for flight seat assignation

# ------ START Datasets needed on Class Definition --------- #
# User > Roles
user_roles = ('customer', 'agent')

# User > Tags
user_tags = ('New','Silver','Premium', 'Black', 'VIP')

# Booking > Status
booking_status = ('confirmed', 'cancelled')

# ------ END Datasets needed on Class Definition --------- #

# ------ START Functions needed on Class Definition --------- #
def generate_short_id(item_type):
    """Generates uniques IDs of 4 characters, for multiple items such as customers and flights"""
    item_type = item_type.lower()
    if item_type == "user":
        return f"C{uuid.uuid4().hex[:4]}"  # First 4 characters of the UUID
    elif item_type == "flight":
        return f"F{uuid.uuid4().hex[:4]}"
    else:
        pass

def hash_password(password):
    """Handles passwords with hash technique instead of storing it as plain text"""
    return hashlib.sha256(password.encode()).hexdigest()

def generate_flight_seat():
    """Generates Assigned Seat when booking"""
    seat_letter = ['A', 'B', 'C', 'D', 'E', 'F']
    seat_number = list(range(1, 30))

    # Taking random letter & random numbers
    random_letter = random.choice(seat_letter)
    random_number = random.choice(seat_number)

    # Concatenate both
    flight_seat = random_letter + random_number
    return flight_seat

# ------ END Functions needed on Class Definition --------- #

# ------ START 🙋‍♀️️ User Class --------- #
class User:
    def __init__(self, id, first_name, last_name, email, password, phone_number, role, birth_date):
        self.__id : str = id
        self.__first_name : str = first_name
        self.__last_name : str = last_name
        self.__email : str = email
        self.__password : str = password
        self.__phone_number: str = phone_number
        self.__role : str = role            #todo: 'agent' or 'customer'
        self.__birth_date: str = birth_date # for age calculation / filtering
        self.__address = None #Applied concept of Composition
        self.__city = None
        #self.__total_points: int = total_points #loyalty points accumulated
        self.__total_spent: float = 0.0 # total amount spent on flights
        self.__flight_history = []  #list of Flight objects as Purchased Flight History

    #To display data from a class object to users
    def __str__(self):
        #order_list_str = "\n".join([f"- ID: {order.get_order_id()}\tItems: {order.get_total_items()}\tAmount: $"
         #                           f"{order.get_total_amount()}\tDate:"
          #                          f" {order.get_order_date()}"
           #                         for order in self.__order_history])
        return (f"# --------------- #\n"
                f"Name: {self.__first_name.title()} {self.__last_name.title()}\n"
                f"Email: {self.__email}\n"
                f"Phone Number: {self.__phone_number}\n"
                f"Date of Birth: {self.__birth_date}\n"
                f"Address: {self.__address} {self.__city}\n"
                #f"Reward Points: {self.__total_points}"
                f"Flight History: {len(self.__flight_history)} flights\n"
                #f"{order_list_str}\n"
        )

    # To display data from a class object to programmers
    def __repr__(self):
        return (f"------\n"
                f"Name: {self.__first_name} : {type(self.__first_name)} + {self.__last_name} :"
                f" {type(self.__last_name)}\n"
                f"Email: {self.__email} : {type(self.__email)}\n"
                f"Phone Number: {self.__phone_number} : {type(self.__phone_number)}\n"
                f"Password: {self.__password} : {type(self.__password)}\n"
                f"Date of Birth: {self.__birth_date} : {type(self.__birth_date)}\n"
                f"Address: {self.__address} : {type(self.__address)}\n"
                #f"Reward Points: {self.__total_points} : {type(self.__total_points)}\n"
                f"Flight History: {self.__flight_history} : {type(self.__flight_history)}"
        )

    #User Getters:
    def get_id(self):
        return self.__id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_email(self):
        return self.__email

    def get_password(self):
        return self.__password

    def get_phone_number(self):
        return self.__phone_number

    def get_role(self):
        return self.__role

    def get_address(self):
        return self.__address

    def get_flight_history(self):
        return self.__flight_history

    # User Setters:
    def set_id(self):
        item_type = "user"
        self.__id = generate_short_id(item_type)

    def set_first_name(self, value):
        self.__first_name = value

    def set_last_name(self, value):
        self.__last_name = value

    def set_email(self, value):
        self.__email = value

    def set_password(self, value):
        self.__password = hash_password(value)

    def set_phone_number(self, value):
        self.__phone_number = value

    def set_role(self, value):
        self.__role = value

    def set_birth_date(self, value):
        self.__birth_date = value

    def add_flight(self, flight):
        self.__flight_history.append(flight)

    """Set Address if is within Address class. If not -> show message"""
    def set_address(self,value):
        if isinstance(value, Address):
            self.__address = value
        else:
            raise TypeError("The address must be valid.")

class Address:
    def __init__(self, street, city, state, postal_code, country):
        self.__street: str = street
        self.__city: str = city
        self.__state: str = state
        self.__zip_code: str = postal_code
        self.__country: str = country

    def __str__(self):
        return (f"{self.__street.title()} {self.__city.title()} {self.__state.upper()} ({self.__zip_code})"
                f" {self.__country.title()}")
# ------ END 🙋‍♀️️ USER Class --------- #

# ------ START 🙋‍♀️🙋 USER MANAGER Class --------- #
#todo: Adjust UserManager Class
class UserManager:
    def __init__(self, name):
        self.__name = name
        self.__user_list = []
        self.__total_users = 0
        self.__email_list = []
        self.__username_list = []
        self.__password_list = []

    #Getters
    def get_user_list(self):
        return self.__user_list

    def get_email_list(self):
        self.__email_list = []
        for user in self.__user_list:
            self.__email_list.append(user.get_email())
        return self.__email_list

    def get_username_list(self):
        self.__username_list = []
        for user in self.__user_list:
            self.__username_list.append(user.get_username())
        return self.__username_list

    def get_password_list(self):
        self.__password_list = []
        for user in self.__user_list:
            self.__password_list.append(user.get_password())
        return self.__password_list

    def __str__(self):
        return (f"🙋‍♀️️  {self.__name}  🙋‍♀️\n\t"
                f"Current users: {self.__total_users}\n")

    def display_user_list(self):
        for user in self.__user_list:
            print(f"{user.__str__()}")

    def add_user(self, user: User):
        self.__user_list.append(user)
        self.__total_users += 1

    def remove_user(self, user: User):
        self.__user_list.remove(user)
        self.__total_users -= 1

# ------ END 🙋‍♀️🙋️ USER MANAGER Classes --------- #

# ------ START ✈️ Flight Class --------- #
class Flight:
    def __init__(self, origin, destination, departure_time, arrival_time, price, points_by_flight, seats_available):
        self.__flight_number = None
        self.__origin: str = origin
        self.__destination: str = destination
        self.__departure_time: str = departure_time
        self.__arrival_time: str = arrival_time
        self.__price: float = price
        self.__points_by_flight: int = points_by_flight
        self.__seats_available: int = seats_available

    # To display data from a class object to users
    def __str__(self):
        return (f"# --------------- #\n"
                f"Flight Number: {self.__flight_number}\n"
                f"Origin: {self.__origin}\n"
                f"Destination: {self.__destination}\n"
                f"Departure Time: {self.__departure_time}\n"
                f"Arrival Time: {self.__arrival_time}\n"
                f"Price: ${self.__price}\n"
                f"Reward Points: ${self.__points_by_flight}\nYou'll win these points by booking this flight (limited "
                f"offer).\n"
                f"Seats Available: {self.__seats_available}"
                )

    # To display data from a class object to programmers
    def __repr__(self):
        return (f"------\n"
                f"Flight Number: {self.__flight_number} : {type(self.__flight_number)}\n"
                f"Origin: {self.__origin} : {type(self.__origin)}\n"
                f"Destination: {self.__destination} : {type(self.__destination)}\n"
                f"Departure Time: {self.__departure_time} : {type(self.__departure_time)}\n"
                f"Arrival Time: {self.__arrival_time} : {type(self.__arrival_time)}\n"
                f"Price: ${self.__price} : {type(self.__price)}\n"
                f"Reward Points: ${self.__points_by_flight} : {type(self.__points_by_flight)}\n"
                f"Seats Available: {self.__seats_available} : {type(self.__seats_available)}"
        )

    #Getters
    def get_flight_number(self):
        return self.__flight_number

    def get_origin(self):
        return self.__origin

    def get_destination(self):
        return self.__destination

    def get_departure_time(self):
        return self.__departure_time

    def get_arrival_time(self):
        return self.__arrival_time

    def get_price(self):
        return self.__price

    def get_points_by_flight(self):
        return self.__points_by_flight

    def get_seats_available(self):
        return self.__seats_available

    #Setters
    def set_flight_number(self):
        item_type = "flight"
        self.__flight_number = generate_short_id(item_type)

    def set_origin(self, value):
        self.__origin = value

    def set_destination(self, value):
        self.__destination = value

    def set_departure_time(self, value):
        self.__departure_time = value

    def set_arrival_time(self, value):
        self.__arrival_time = value

    def set_price(self, value):
        self.__price = value

    def set_points_by_flight(self, value):
        self.__points_by_flight = value

    def set_seats_available(self, value):
        self.__seats_available = value

# ------ END ✈️ Flight Class --------- #

# ------ START 📗 Booking Class --------- #
class Booking:
    def __init__(self, user, flight: Flight, status):
            timestamp = datetime.now()
            self.__booking_number = None
            self.__user_id: User = user
            self.__flight: Flight = flight
            self.__purchase_date: str = timestamp.strftime("%a %d %b %H:%M")
            self.__price_paid = None
            self.__status: str = status
            self.__flight_seat = None

# To display data from a class object to users
    def __str__(self):
        return (f"# --------------- #\n"
                f"Booking Number: {self.__booking_number}\n"
                f"Purchased on: {self.__purchase_date}\n"
                f"Paid: {self.__price_paid}"
                f"Reward Points Won: {self.__flight.get_points_by_flight()}"
                f"Status: {self.__status}"
                f"# ------- Flight Details -------- #\n"
                f"Flight Number: {self.__flight.get_flight_number()}\n"
                f"Origin: {self.__flight.get_origin()}\n"
                f"Destination: {self.__flight.get_destination()}\n"
                f"Departure Time: {self.__flight.get_departure_time()}\n"
                f"Arrival Time: {self.__flight.get_arrival_time()}\n"
                f"Seat: {self.__flight_seat}"
                )

    # To display data from a class object to programmers
    def __repr__(self):
        return (f"------\n"
                f"Booking Number: {self.__booking_number} : {type(self.__booking_number)}\n"
                f"Purchased on: {self.__purchase_date} : {type(self.__purchase_date)}\n"
                f"Paid: {self.__price_paid} : {type(self.__price_paid)}"
                f"Reward Points Won: {self.__flight.get_points_by_flight()} : {type(self.__flight.get_points_by_flight())}"
                f"Status: {self.__status} : {type(self.__status)}"
                f"# ------- Flight Details -------- #\n"
                f"Flight Number: {self.__flight.get_flight_number() : {type(self.__flight.get_flight_number())}}\n"
                f"Origin: {self.__flight.get_origin()} : {type(self.__flight.get_origin())}\n"
                f"Destination: {self.__flight.get_destination() : {type(self.__flight.get_destination())}}\n"
                f"Departure Time: {self.__flight.get_departure_time()} : {type(self.__flight.get_departure_time())}\n"
                f"Arrival Time: {self.__flight.get_arrival_time()} : {type(self.__flight.get_arrival_time())}\n"
                f"Seat: {self.__flight_seat} : {type(self.__flight_seat)}"
        )

    #Getters
    def get_booking_number(self):
        return self.__booking_number

    def get_purchase_date(self):
        return self.__purchase_date

    def get_price_paid(self):
        return self.__price_paid

    def get_points_by_flight(self):
        return self.__flight.get_points_by_flight()

    def get_status(self):
        return self.__status

    #Setters
    def set_booking_number(self, flight):
        self.__booking_number = f"B{flight.get_flight_number()}"

    def set_purchase_date(self, value):
        self.__purchase_date = value

    def set_price_paid(self, value):
        self.__price_paid = value

    def set_status(self, value):
        self.__status = value

    def set_flight_seat(self):
        self.__flight_seat = generate_flight_seat()

# ------ END 📗 Booking Class --------- #


