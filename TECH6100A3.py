# TECH6100 Assessment 3 Florencia Scolari ID 1847863 June 2025
# Check the full project and references on the GitHub Public Repo https://github.com/florscolari/TECH6100A3.git

# NOTE: You'll find the unit tests below the script to run the program. Please follow the instructions to activate them.
# Thank you.

# User for Testing Purposes:

# Customer
# Email: test@t.com.au
# Password: Abc123
# First Name: Elle
# Last Name: Test

# Agent
# Email: abc@a.com.au
# Password: Abc123
# First Name: Alan
# Last Name: Doe

# Reward Program Conditions applied by the system:
# A customer is VIP when more than 1200 are earned & more than 4 flights.
# A customer is also Silver level when they have 0-1 flights, Premium when 2-4, and Black with 5 or more flights

# Out of scope:
# 1. Global command to cancel an ongoing task in some cases.
# 2. System creates Customer users by default. Agents are added by Admin role (out of scope)
# 3. When flight is removed from Agent's side, no notifications or Actions are taken on Customer's side
# 4. Reward points Qty is set by the agent when creating a new flight (not by any condition run by the system)
# 5. Some user inputs don't have full validation.
# 6. Although I have set __str__ & __repr__ for User, Flight & Booking, I've used __str__ in most cases instead of __repr__


# PEP 8 Naming Conventions:
# Variable name: lowercase_with_underscores - user_name
# Function name: verb_lowercase_underscore - send_email()
# Class name: CapitaliseWords - UseNouns

import uuid #to generate unique ids
import hashlib #to handle passwords in a safer manner
from datetime import datetime #to set datestamp when booking a flight
import random #to create random combinations for flight seat assignation
from datetime import date #to calculate dates/age
import csv #to export customer data to a CSV file

# ------ START Datasets needed on Class Definition --------- #
# User > Roles
user_roles = ('customer', 'agent')

# User > Tags
user_tags = ('Silver','Premium', 'Black')

# Booking > Status
booking_status = ('Confirmed', 'Canceled')

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
    flight_seat = random_letter + str(random_number)
    return flight_seat

def calculate_age(dob):
    """Calculates age based on date of birth with an object of class date(yyyy, m, dd)"""
    today = date.today()
    age = today.year - dob.year
    return age


# ------ END Functions needed on Class Definition --------- #
# ------ START ✈️ Flight Class --------- #
class Flight:
    def __init__(self, flight_date, origin, destination, departure_time, arrival_time, price, points_by_flight, seats_available):
        self.__flight_number = None
        self.__flight_date: date = flight_date
        self.__flight_status = "Confirmed" #'Confirmed', 'Canceled' or 'Completed'
        self.__date_status = None # 'Past' or 'Current'
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
                f"Flight Status: {self.__flight_status}\n"
                f"Date: "
                f"{self.__date_status}\t {self.__flight_date.day}-{self.__flight_date.month}"
                f"-{self.__flight_date.year}\n"
                f"Origin: {self.__origin}\n"
                f"Destination: {self.__destination}\n"
                f"Departure Time: {self.__departure_time}\n"
                f"Arrival Time: {self.__arrival_time}\n"
                f"Price: ${self.__price}\n"
                f"Reward Points: {self.__points_by_flight} // Win them when booking it (limited "
                f"offer).\n"
                f"Seats Available: {self.__seats_available}"
                )

    # To display data from a class object to programmers
    def __repr__(self):
        return (f"------\n"
                f"Flight Number: {self.__flight_number} : {type(self.__flight_number)}\n"
                f"Flight Status: {self.__flight_status}\n"
                f"Date of Flight: {self.__flight_date.day}-{self.__flight_date.month}-{self.__flight_date.year}\n"
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

    def get_flight_date(self):
        return self.__flight_date

    def get_flight_status(self):
        return self.__flight_status

    def get_date_status(self):
        return self.__date_status

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
        """Generates unique IDs for flight numbers"""
        item_type = "flight"
        self.__flight_number = generate_short_id(item_type)

    def set_flight_number_fixed(self, value):
        """Hardcodes a fixed IDs for flight numbers... Only for populated data purposes"""
        self.__flight_number = value

    def set_flight_date(self, value):
        self.__flight_date = value

    def set_flight_status(self, value):
        self.__flight_status = value

    def set_date_status(self, value):
        self.__date_status = value

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

# ------ START ✈️✈️ FLIGHT MANAGER Classes --------- #
class FlightManager:
    def __init__(self, name):
        self.__name = name
        self.__flight_list = []
        self.__total_flights = 0

    #Getters
    def get_name(self):
        return self.__name

    def get_flight_list(self):
        return self.__flight_list

    def get_total_flights(self):
        return self.__total_flights

    def __str__(self):
        return (f"️️✈️️️  {self.__name}   ✈️\n\t"
                f"Total Flights: {len(self.__flight_list)}\n")

    def display_flight_list(self):
        if not self.__flight_list:
            print("No flights to display.")
        else:
            for flight in self.__flight_list:
                print(f"{flight}")

    def add_flight(self, flight: Flight):
        self.__flight_list.append(flight)


    def remove_flight(self, flight: Flight):
        self.__flight_list.remove(flight)


    def get_flight_by_flight_number(self, flight_number):
        for flight in self.__flight_list:
            if flight.get_flight_number() == flight_number:
                return flight
        return None

    def clear_flight_list(self):
        return self.__flight_list.clear()



# ------ END ✈️✈️ FLIGHT MANAGER Classes --------- #

# ------ START 🙋‍♀️️ User Class --------- #
class User:
    def __init__(self, id, first_name, last_name, email, password, phone_number, birth_date):
        self.__user_status = 'Active' # Active or Deleted when delete customer
        self.__id : str = id
        self.__first_name : str = first_name
        self.__last_name : str = last_name
        self.__email : str = email
        self.__password : str = password
        self.__phone_number: str = phone_number
        self.__role : str = '' # by default, this system creates Customer users. Agents are added by Admin (out of scope)
        self.__birth_date: date = birth_date # for age calculation / filtering
        self.__address = None #Applied concept of Composition
        self.__city = None
        self.__total_points: int = 100 #loyalty points accumulated. 100pt when new user.
        self.__total_spent: float = 0.0 # total amount spent on flights
        self.__flight_history = []  #list of Flight objects as Purchased Flight History
        self.__booking_list = []  # list of Booking objects this user has
        self.__vip = 'No' #No VIP when new user.
        self.__tag = user_tags[0]  # Silver when new user.

    #To display data from a class object to users
    def __str__(self):
        flight_list_str = "\n".join([f"- ID: {flight.get_flight_number()}\tFrom: {flight.get_origin()}\tTo: "
                                     f"{flight.get_destination()}\tDate: {flight.get_flight_date()}\t "
                                     f"Status: {flight.get_date_status()} - {flight.get_flight_status()}\tAmount: $"
                                     f"{flight.get_price()}\t"
                                    for flight in self.__flight_history])
        return (f"# --------------- #\n"
                f"ID: {self.__id}\n"
                f"Name: {self.__first_name.title()} {self.__last_name.title()}\n"
                f"VIP: {self.__vip}\n\n"
                f"▸Personal Details:\n"
                f"Date of Birth: {self.__birth_date.day}-{self.__birth_date.month}-{self.__birth_date.year}\n"
                f"Age: {self.get_age()}\n\n"
                f"▸Contact Details:\n"
                f"Email: {self.__email}\n"
                f"Phone Number: {self.__phone_number}\n"
                f"Address: {self.__address}\n"                
                f"▸Transaction Details:\n"
                f"Total Flights: {len(self.__flight_history)}\n"
                f"Total Spent: ${self.__total_spent}\n\n"
                f"▸Reward Program Details:\n"
                f"Total Points: {self.__total_points}\n"
                f"Level: {self.__tag}\n\n"

                f"Flight List: {len(self.__flight_history)} flights\n"
                f"{flight_list_str}\n"
        )

    # To display summarised data for customers
    def __repr__(self):
        return (f"# --------------- #\n"
                f"ID: {self.__id}\n"
                f"Name: {self.__first_name.title()} {self.__last_name.title()}\n"
                f"VIP: {self.__vip}\n"
                f"Total Flights: {len(self.__flight_history)}\n"
                f"Total Spent: ${self.__total_spent}\n"
                f"Reward Points: {self.__total_points}\n"
                f"Reward Level: {self.__tag}\n"
                )

    def display_flight_history(self):
        flight_list_str = "\n".join([f"- ID: {flight.get_flight_number()}\tFrom: {flight.get_origin()}\tTo: "
                                     f"{flight.get_destination()}\tDate: {flight.get_flight_date()}\tAmount: $"
                                     f"{flight.get_price()}\t"
                                     for flight in self.__flight_history])
        print(f"Booking List: {len(self.__flight_history)} flights\n"
            f"{flight_list_str}\n")
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

    def get_dob(self):
        return self.__birth_date

    def get_age(self):
        today = date.today()
        age = today.year - self.__birth_date.year
        return age

    def get_address(self):
        return self.__address

    def get_city(self):
        return self.__address.get_city()

    def get_user_status(self):
        return self.__user_status

    def get_vip_status(self):
        return self.__vip

    def get_tag_level(self):
        return self.__tag

    def get_points(self):
        return self.__total_points

    def get_total_spent(self):
        return self.__total_spent

    def get_flight_history(self):
        return self.__flight_history

    def get_booking_list(self):
        return self.__booking_list

    # User Setters:
    def set_id(self):
        item_type = "user"
        self.__id = generate_short_id(item_type)

    def set_id_fixed(self, value):
        """Hardcodes a fixed IDs for users... Only for populated data purposes"""
        self.__id = value

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

    def update_vip_status(self):
        """Sets VIP as Yes if Customer has > 3 flights && > 600 as amount spent"""
        if len(self.__flight_history) > 4 and self.__total_spent > 1200:
            self.__vip = '🏆 Yes'
        else:
            self.__vip = 'No'

    def update_user_status(self):
        """Sets User Status as Deleted if Customer account has been deleted"""
        self.__user_status = 'Deleted'

    def update_tag_level(self):
        """Updates Reward Program Level based on points earned with flights/bookings"""
        num_flights = len(self.__flight_history)

        if 0 <= num_flights <= 1:
            self.__tag = user_tags[0] #Silver
        elif 2 <= num_flights <= 4:
            self.__tag = user_tags[1] # Premium
        elif num_flights >= 5:
            self.__tag = user_tags[2] # Black

    def add_flight_to_flight_history(self, flight):
        self.__flight_history.append(flight)
        self.update_vip_status()
        self.update_tag_level()

    def add_booking_to_booking_list(self, booking):
        self.__booking_list.append(booking)

    def clear_booking_list(self):
        self.__booking_list = []

    def add_total_spent(self, value):
        self.__total_spent = value

    def add_points(self, value):
        self.__total_points = value

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

    def get_city(self):
        return self.__city

# ------ END 🙋‍♀️️ USER Class --------- #

# ------ START 🙋‍♀️🙋 USER MANAGER Class --------- #

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
            print(f"{user.__repr__()}")

    def add_user(self, user: User):
        self.__user_list.append(user)
        self.__total_users += 1

    def remove_user(self, user: User):
        self.__user_list.remove(user)
        self.__total_users -= 1

# ------ END 🙋‍♀️🙋️ USER MANAGER Classes --------- #



# ------ START 📗 Booking Class --------- #
class Booking:
    def __init__(self, user: User, flight: Flight, status):
            self.__user: User = user
            timestamp = datetime.now()
            self.__booking_number = None
            self.__user_id: str = user.get_id()
            self.__flight: Flight = flight
            self.__purchase_date: str = timestamp.strftime("%a %d %b %H:%M")
            self.__price_paid = None
            self.__status: str = status
            self.__flight_seat = None

# To display data from a class object to users
    def __str__(self):
        return (f"# --------------- #\n"
                f"Booking Number: {self.__booking_number}\n"
                f"Status: {self.__status}\n"
                f"Purchased on: {self.__purchase_date}\n"
                f"Paid: ${self.__price_paid}\n"
                f"▸ Flight Details\n"
                f"Flight Number: {self.__flight.get_flight_number()}\n"
                f"Date of Flight: {self.__flight.get_flight_date()}\n"
                f"Origin: {self.__flight.get_origin()}\t"
                f"Destination: {self.__flight.get_destination()}\n"
                f"Departure Time: {self.__flight.get_departure_time()}\t"
                f"Arrival Time: {self.__flight.get_arrival_time()}\n"
                f"Seat: {self.__flight_seat}\n"
                )

    # To display data from a class object to programmers
    def __repr__(self):
        return (f"# --------------- #\n"
                  f"Booking Number: {self.__booking_number}\n"
                f"Status: {self.__status}\n"
                f"Purchased on: {self.__purchase_date}\n"
                f"Paid: ${self.__price_paid}\n"
                f"▸ Flight Details\n"
                f"Flight Number: {self.__flight.get_flight_number()}\n"
                f"Date of Flight: {self.__flight.get_flight_date()}\n"
                f"Origin: {self.__flight.get_origin()}\t"
                f"Destination: {self.__flight.get_destination()}\n"
                f"Departure Time: {self.__flight.get_departure_time()}\t"
                f"Arrival Time: {self.__flight.get_arrival_time()}\n"
                f"Seat: {self.__flight_seat}\n"
        )

    #Getters
    def get_booking_number(self):
        return self.__booking_number

    def get_flight_number(self):
        return self.__flight.get_flight_number()

    def get_purchase_date(self):
        return self.__purchase_date

    def get_price_paid(self):
        return self.__price_paid

    def get_user_id(self):
        return self.__user_id

    def get_first_name(self):
        return self.__user.get_first_name()

    def get_last_name(self):
        return self.__user.get_last_name()

    def get_points_by_flight(self):
        return self.__flight.get_points_by_flight()

    def get_status(self):
        return self.__status

    #Setters
    def set_booking_number(self, flight):
        self.__booking_number = f"B{flight}"

    def set_purchase_date(self, value):
        self.__purchase_date = value

    def set_price_paid(self, value):
        self.__price_paid = value

    def set_status(self, value):
        self.__status = value

    def set_flight_seat(self):
        self.__flight_seat = generate_flight_seat()

    def add_flight(self, value: Flight):
        self.__flight = value

# ------ END 📗 Booking Class --------- #

# ------ START 📗📗️ BOOKING MANAGER Class --------- #

class BookingManager:
    def __init__(self, name):
        self.__name = name
        self.__booking_list = []
        self.__total_bookings = 0

    #Getters
    def get_name(self):
        return self.__name

    def get_booking_list(self):
        return self.__booking_list

    def get_total_bookings(self):
        return self.__total_bookings

    def __str__(self):
        return (f"️️📗  {self.__name}   📗\n\t"
                f"Current bookings: {self.__total_bookings}\n")

    def display_booking_list(self):
        for booking in self.__booking_list:
            print(f"{booking.__str__()}")

    def add_booking(self, booking: Booking):
        self.__booking_list.append(booking)
        self.__total_bookings += 1

    def remove_booking(self, booking: Booking):
        self.__booking_list.remove(booking)
        self.__total_bookings -= 1


# ------ END 📗📗️ BOOKING MANAGER Class --------- #


#🙋 4 Customers added to have data to handle when the program starts

customer_list = UserManager("Customer Database") #Customer Collection
customer1 = User("CC", "Elle", "Doe", "test@t.com.au", "ElleD", "00000000000", None)
address1 = Address("000 William Street", "Perth", "WA", "6000", "Australia")
customer1.set_role(user_roles[0])
customer1.set_password('Abc123')
customer1.set_birth_date(date(1995, 5, 20))
customer1.set_id_fixed('C0f66')
customer1.set_address(address1)
customer_list.add_user(customer1)

customer2 = User("CC", "James", "Williams", "williams@t.com.au", "JD12", "111111", None)
address2 = Address("000 William Street", "Perth", "WA", "6000", "Australia")
customer2.set_role(user_roles[0])
customer2.set_password('Abc123')
customer2.set_birth_date(date(1999, 9, 16))
customer2.set_id_fixed('Cc618')
customer2.set_address(address2)
customer_list.add_user(customer2)

customer3 = User("CC", "Diana", "Spencer", "dspencer@example.com.au", "AAAA", "9999999999", None)
address3 = Address("5 Wilkinson Street", "Sydney", "NSW", "2011", "Australia")
customer3.set_role(user_roles[0])
customer3.set_password('Abc123')
customer3.set_birth_date(date(2003, 6, 21))
customer3.set_id_fixed('Cc621')
customer3.set_address(address3)
customer_list.add_user(customer3)

customer4 = User("CC", "Rob", "Dylan", "rdylan@example.com.au", "AAAA", "6666666666", None)
address4 = Address("15 Monroe Street", "Sydney", "NSW", "2009", "Australia")
customer4.set_role(user_roles[0])
customer4.set_password('Abc123')
customer4.set_birth_date(date(2001, 4, 18))
customer4.set_id_fixed('Cc622')
customer4.set_address(address4)
customer_list.add_user(customer4)

customer5 = User("CC", "Susan", "Deputy", "sdeputy@example.com.au", "AAAA", "5555555555", None)
address5 = Address("24 Frederick Street", "Canberra", "ACT", "2009", "Australia")
customer5.set_role(user_roles[0])
customer5.set_password('Abc123')
customer5.set_birth_date(date(1976, 2, 9))
customer5.set_id_fixed('Cc623')
customer5.set_address(address5)
customer_list.add_user(customer5)

#Travel Agent User
agent_list = UserManager("Agent Collection")
agent1 = User("AA", "Alan", "Doe", "abc@a.com.au", "JD12", "111111", None)
address0 = Address("000 William Street", "Perth", "WA", "6000", "Australia")
agent1.set_role(user_roles[1])
agent1.set_birth_date(date(1989, 1, 24))
agent1.set_password('Abc123')
agent1.set_id_fixed('Ac618')
agent1.set_address(address0)
agent_list.add_user(agent1)


all_user_list = UserManager("All Users") # to login validation purposes
all_user_list.add_user(customer1)
all_user_list.add_user(customer2)
all_user_list.add_user(customer3)
all_user_list.add_user(customer4)
all_user_list.add_user(customer5)
all_user_list.add_user(agent1)

#✈️ 6 Flights added
# 3 Past Date
available_flight_manager = FlightManager("Available Flights") # Available Flights Collection
all_flight_manager = FlightManager("All Flights") # All Flights Collection
flight1 = Flight(date(2024, 12, 10), 'Perth', 'Sydney', '9:25', '0:35', 489, 240, 9)
flight2 = Flight(date(2025, 1, 17), 'Sydney', 'Canberra', '8:13', '9:40', 112, 45, 4)
flight3 = Flight(date(2025, 4, 10), 'Canberra', 'Perth', '4:37', '7:56', 420, 220, 8)
flight1.set_flight_number()
flight2.set_flight_number()
flight3.set_flight_number()

all_flight_manager.add_flight(flight1)
all_flight_manager.add_flight(flight2)
all_flight_manager.add_flight(flight3)

# 3 Current Date
flight4 = Flight(date(2025, 6, 23), 'Perth', 'Bali', '9:25', '0:35', 280, 140, 12)
flight5 = Flight(date(2025, 8, 17), 'Bali', 'Perth', '4:13', '7:15', 280, 140, 2)
flight6 = Flight(date(2025, 12, 10), 'Perth', 'Broome', '4:37', '9:56', 420, 220, 4)
flight4.set_flight_number()
flight5.set_flight_number()
flight6.set_flight_number()

all_flight_manager.add_flight(flight4)
all_flight_manager.add_flight(flight5)
all_flight_manager.add_flight(flight6)

#📗 4 Bookings added
booking_list = BookingManager('Booking Collection')
booking1 = Booking(customer1, flight1, booking_status[0])
booking2 = Booking(customer1, flight2, booking_status[1])
booking3 = Booking(customer2, flight2,booking_status[1])
booking4 = Booking(customer2, flight3,booking_status[0])

# Adds 4 bookings to the Booking Collection (available from View Bookings option)
booking_list.add_booking(booking1)
booking_list.add_booking(booking2)
booking_list.add_booking(booking3)
booking_list.add_booking(booking4)

# Sets Booking number x 4 bookings
booking1.set_booking_number(flight1.get_flight_number())
booking2.set_booking_number(flight2.get_flight_number())
booking3.set_booking_number(flight2.get_flight_number())
booking4.set_booking_number(flight3.get_flight_number())

# Passes the price paid for these 4 flights to each booking record
booking1.set_price_paid(flight1.get_price())
booking2.set_price_paid(flight2.get_price())
booking3.set_price_paid(flight2.get_price())
booking4.set_price_paid(flight3.get_price())

# Sets flight seat for each booking x 4
booking1.set_flight_seat()
booking2.set_flight_seat()
booking3.set_flight_seat()
booking4.set_flight_seat()

# Adds bookings to User's flight history x 2 customers
customer1.add_flight_to_flight_history(flight1)
customer1.add_flight_to_flight_history(flight2)
customer2.add_flight_to_flight_history(flight2)
customer2.add_flight_to_flight_history(flight3)

# Adds bookings to User's booking list x 2 customers
customer1.add_booking_to_booking_list(flight1)
customer1.add_booking_to_booking_list(flight2)
customer2.add_booking_to_booking_list(flight2)
customer2.add_booking_to_booking_list(flight3)

# Sums reward points to this user
#Customer1
customer1_points = customer1.get_points()
flight1_points = flight1.get_points_by_flight()
flight2_points = flight2.get_points_by_flight()
customer1_updated_points = customer1_points + flight1_points + flight2_points
customer1.add_points(customer1_updated_points)

#Customer2
customer2_points = customer2.get_points()
flight3_points = flight3.get_points_by_flight()
customer2_updated_points = customer2_points + flight2_points + flight3_points
customer2.add_points(customer2_updated_points)

# Adds flight's price to the User's total spent amount
#Customer1
customer1_spent = customer1.get_total_spent()
flight1_price = flight1.get_price()
flight2_price = flight2.get_price()
customer1_updated_spent = customer1_spent + flight1_price + flight2_price
customer1.add_total_spent(customer1_updated_spent)

#Customer2
customer2_spent = customer2.get_total_spent()
flight3_price = flight3.get_price()
customer2_updated_spent = customer2_spent + flight2_price + flight3_price
customer2.add_total_spent(customer2_updated_spent)


def login():
    """Asks for email & password and checks if they match against records store in user_list"""
    print(f"Enter 'cancel' to quit.")

    while True:
        try:
            user_email = input('Enter your email: \n')
            if user_email.lower() == 'cancel':
                print("Login canceled.")
                return None

            # Checks if email exists
            user = None
            for u in all_user_list.get_user_list():
                if u.get_email().lower() == user_email.lower() and u.get_user_status() == 'Active':
                    user = u
                    break

            if not user:
                raise ValueError("Email not found.")

            break # at this point, email is OK. Now let's move to password loop

        except ValueError as e:
            print(f"❌ {e} Try again or type 'cancel' to quit.")

    while True:
        try:
            user_password = input('Enter your password: \n')
            if user_password.lower() == 'cancel':
                print("Login canceled.")
                return None

            # Check if hashed password matches
            if user.get_password() != hash_password(user_password):
                raise ValueError("Incorrect password.")

            print("✅ Login successful.\n")
            print("-"*20)
            print(f"Welcome {user.get_first_name()}!")
            return user

        except ValueError as e:
            print(f"❌ {e} Try again or type 'cancel' to quit.")

def login_with_arguments(test_email, test_password):
    """ONLY FOR UNIT TEST PURPOSE: Asks for email & password and checks if they match against records store in
    user_list"""
    # Checks if email exists
    for u in all_user_list.get_user_list():
        if u.get_email().lower() == test_email.lower():
            if u.get_password() == hash_password(test_password):
                return u
    return None

def welcome():
    """To welcome the user when starting the program. As Flight CRM, login is required to browse the site as
    customer or travel agent."""
    print("-" * 40)
    print("🌎✈️ Welcome to Traveliverse ✈️🌎\n"
          "Explore our offer of flights around Australia and beyond.\n\n"
          "Login to access or create a new account:\n")

def main():
    """Starts the program & Displays the login feature"""
    while True:
        print(f"1. Login\n"
              f"2. Create an account\n"
              f"0. Exit Program\n")
        user_choice = input("Select an option: ").strip()
        if user_choice == "1":
                user = login()
                if user is not None:
                    if user.get_role() == 'agent':
                        show_agent_menu()
                    else:
                        show_customer_menu(user)
        elif user_choice == "2":
                create_user_account()
        elif user_choice == "0":
            print("You have exited Traveliverse. See you next time!")
            break
        else:
            print("❌ Invalid option. Try again using from 0 to 2 to select an option.")

def show_agent_menu():
    """Displays the menu options for AGENTS"""
    while True:
        print(f"\nEnter an option:")
        print(f"🙋‍ Customers:\n"
              f"C1. View Customers\n"
              f"C2. Filter Customers by City Address\n"
              f"C3. Filter Customers by Age range\n"
              f"C4. Search a Customer\n"
              f"C5. Add Customer\n"
              f"C6. Delete Customer\n"
              f"C7. Export Customer Database\n\n"
              f"✈️ Flights:\n"
              f"F1. View Available Flights\n"
              f"F2. Search a Flight\n"
              f"F3. Register New Flight\n"
              f"F4. Update Flight Status\n"
              f"F5. Remove Flight\n"
              f"F6. View All Flights\n\n"
              f"0. Logout\n")
        user_choice = input("Select an option: ").strip().capitalize()
        if user_choice == "C1":
            show_all_customers() # Done
        elif user_choice == "C2":
            ask_city() # Done
        elif user_choice == "C3":
            ask_min_and_max_range()
        elif user_choice == "C4":
            show_customer_by_id() # Done
        elif user_choice == "C5":
            add_customer() # Done
        elif user_choice == "C6":
            remove_customer_by_id() # Done
        elif user_choice == "C7":
           export_customer_database() # Done
        elif user_choice == "F1":
            show_available_flights() # Done
        elif user_choice == "F2":
            show_flight_by_id() # Done
        elif user_choice == "F3":
            add_flight() # Done
        elif user_choice == "F4":
            update_flight_status() # Done
        elif user_choice == "F5":
            remove_flight_by_flight_number() # Done
        elif user_choice == "F6":
            show_all_flights() # Done
        elif user_choice == "0":
            print("✅ You have successfully logout.\n")
            welcome()
            break
        else:
            print("❌ Invalid option. Try again using C or F followed by numbers to select an option, or 0 to logout.")

# --- AGENT > START Functions for Customer Management --- #
def show_all_customers():
    """prints the list of User objects (subset Customers): total number of customers & display customer details"""
    print(customer_list)
    customer_list.display_user_list()

def filter_customers_by_city(city):
    """Retrieves a list of customers that match with a specific city given."""
    matching_customers = []

    for customer in customer_list.get_user_list():
        if customer.get_city().lower() == city.lower():
            matching_customers.append(customer)

    # to display the list of customers within the age range
    print(f"{len(matching_customers)} Customers live in {city.title()}:")
    if matching_customers:
        for i, customer in enumerate(matching_customers, start=1):
            print(f"{i}. {customer.get_first_name()} {customer.get_last_name()}")
    else:
        print("No customers found for this city.")

def ask_city():
    """Asks the user the city to do the filtering by city on customer_list"""
    while True:
        city = input("Enter city or cancel to quit: ").strip()

        if city.upper() == "CANCEL":
            print("✅ Filter by city task has been canceled.")
            return

        if not city:
            print("❌ City is required. It cannot be empty.")
            continue

        # Calling the other function to pass the user input for city as argument
        filter_customers_by_city(city)
        return

def filter_customers_by_age_range(min_age, max_age):
    """Retrieves a list of customers within a specific age range."""
    matching_customers = []

    for customer in customer_list.get_user_list():
        age = customer.get_age()
        if min_age <= age <= max_age:
            matching_customers.append(customer)

    # to display the list of customers within the age range
    print(f"{len(matching_customers)} Customers aged between {min_age} and {max_age}:")
    if matching_customers:
        for i, customer in enumerate(matching_customers, start=1):
            print(f"{i}. {customer.get_first_name()} {customer.get_last_name()} {customer.get_age()}")
    else:
        print("No customers found in this age range.")

def ask_min_and_max_range():
    """Asks the user the min_age and max_age to do the filtering by age range on customer_list"""
    try:
        min_age = int(input("Enter Minimum age: "))
        max_age = int(input("Enter Maximum age: "))
        if min_age > max_age:
            print("❌ Minimum age cannot be greater than maximum age.")
            return
        filter_customers_by_age_range(min_age, max_age)
    except ValueError:
        print("❌ Invalid option. Please enter valid number for age.")


def show_customer_by_id():
    """Checks a customer by its ID & retrieves the customer details"""
    while True:
        print("Enter Customer ID or Cancel: ")
        choice = input().upper().strip()

        if choice == "CANCEL":
            break

        for custUser in customer_list.get_user_list():
            if custUser.get_id().upper().strip() == choice:
                print(custUser)
                return

        print("❌ Invalid option. Please select a valid one.")


def add_customer():
    """Creates & Store on-fly a new customer user. Agents are added by Admin role (out of scope)"""
    print(f"▸ Create new customer user \n"
          f"Use this only to support users by phone they can't create accounts by themselves.")
    print(f"Enter 'cancel' to quit.")

    while True:
        try:
            new_email = input("Enter email: \n").strip()
            if new_email.lower() == 'cancel':
                print("Account creation canceled.")
                return None

            if not new_email:
                print("❌ Email is required. It cannot be empty.")
                continue

            # Checks if email exists
            email_exists = False
            for u in all_user_list.get_user_list():
                if u.get_email().lower() == new_email.lower():
                    email_exists = True
                    break

            if email_exists:
                raise ValueError("❌ Email is already used. Try a different one.")
            else:
                break  # at this point, email is OK.

        except ValueError as e:
            print(f"❌ {e} Try again or type 'cancel' to quit.")

    while True:
        new_password = input('Enter password: \n').strip()
        if new_password.lower() == 'cancel':
            print("Account creation canceled.")
            return None

        if not new_password:
            print(f"❌ Password is required. It cannot be empty.")
        else:
            break  # at this point, password is OK.

    print("Complete customer's profile.\n")
    print("▸ Personal Details")
    # First name
    new_first_name = input('First name: \n').strip()
    if new_first_name.lower() == 'cancel':
        print("Account creation canceled.")
        return None

    # Last name
    new_last_name = input('Last name: \n')
    if new_last_name.lower() == 'cancel':
        print("Account creation canceled.")
        return None

    # Date of Birth
    try:
        new_day = int(input("Birth day (1-31): \n").strip())
        new_month = int(input("Birth month (1-12): \n").strip())
        new_year = int(input("Birth year (e.g. 1980): \n").strip())
        birth_date = date(new_year, new_month, new_day)
    except ValueError:
        print("❌ Invalid date. Account creation canceled")
        return None

    # Phone Number
    try:
        new_phone_number = int(input("Phone number: \n").strip())
    except ValueError:
        print("❌ Invalid phone number. Account creation canceled")
        return None

    # Address
    print("▸ Address Details")
    street = input("Street address: \n").strip()
    if street.lower() == 'cancel':
        print("Account creation canceled.")
        return None

    city = input("City: \n").strip()
    if city.lower() == 'cancel':
        print("Account creation canceled.")
        return None

    state = input("State: \n").strip()
    if state.lower() == 'cancel':
        print("Account creation canceled.")
        return None

    zip_code = input("Zip Code: \n").strip()
    if zip_code.lower() == 'cancel':
        print("Account creation canceled.")
        return None

    country = input("Country: \n").strip()
    if country.lower() == 'cancel':
        print("Account creation canceled.")
        return None

    # Create User object (new customer)
    new_address = Address(street, city, state, zip_code, country)
    new_user = User(None, new_first_name, new_last_name, new_email, new_password, new_phone_number, birth_date)
    new_user.set_role('customer')
    new_user.set_password(new_password)
    new_user.set_birth_date(birth_date)
    new_user.set_id()
    new_user.set_address(new_address)

    # Adds User object (new customer) to the customer list
    customer_list.add_user(new_user)
    all_user_list.add_user(new_user)

    # Displays successful message
    print("✅ New customer account has been created successfully.\n")
    print("-" * 20)
    return new_user


def remove_customer_by_id():
    """Removes customer user by its ID from customer-list & Updates user_status as 'Deleted' in all_user_list"""
    user_selected = None
    while True:
        print("Enter Customer ID or Cancel: ")
        choice = input().upper().strip()

        if choice == "CANCEL":
            return None

        for custUser in customer_list.get_user_list():
            if custUser.get_id().upper().strip() == choice:
                user_selected = custUser
                break

        if user_selected:
            break

        print("❌ Invalid option. Please select a valid one.")

    print(f"Are you sure you want to delete account {user_selected.get_id()} for {user_selected.get_first_name()} {user_selected.get_last_name()}?\nEverything will be lost.\n")
    while True:
        try:
            choice = input("Enter 'delete' to delete your account or 'cancel' to quit. \n").strip()

            # Inputs 'cancel'
            if choice.lower() == 'cancel':
                print("Account deletion canceled.\n")
                return None

            # Input is empty
            if not choice:
                print("❌ Input is required. Try again.")
                continue

            # Inputs 'delete'
            if choice.lower() == 'delete':
                customer_list.remove_user(user_selected)
                user_selected.update_user_status() # Marks as Deleted in All users database
                print(f"✅ You've deleted account {user_selected.get_id()} successfully.\n")
                return None

        except ValueError as e:
            print(f"❌ {e} Try again or type 'cancel' to quit.")


def export_active_customers_db():
    """Exports CSV file with Active Customers"""
    while True:
        try:
            file_name_raw = input("Enter a name for the csv file or 'cancel' to quit. \n").strip()
            file_name = file_name_raw.replace(" ", "")  # to clean the name of the file
            # Inputs 'cancel'
            if file_name.lower() == 'cancel':
                print("Exporting CSV file canceled.\n")
                return None

            # Input is empty
            if not file_name:
                print("❌ Input is required. Try again.")
                continue
            break
        except ValueError as e:
            print(f"❌ {e} Try again or type 'cancel' to quit.")

    # Gets the list of Active Customer User objects
    data = customer_list.get_user_list()

    # Formats dataset as dictionary, so it can be exported as csv or json in the future. Also, easier to scale down or up
    # attributes
    dict_data = [{
        'ID': user.get_id(),
        'First Name': user.get_first_name(),
        'Last Name': user.get_last_name(),
        'Email': user.get_email(),
        'Phone Number': user.get_email(),
        'Role': user.get_role(),
        'Birth Date': user.get_dob(),
        'Age': user.get_age(),
        'Address': user.get_address(),
        'City': user.get_city(),
        'Reward Points': user.get_points(),
        'Reward Level': user.get_tag_level(),
        'VIP': user.get_vip_status(),
        'Total Spent': user.get_total_spent(),
        'Total Flights': len(user.get_flight_history()),
        'Total Bookings': len(user.get_booking_list())
    } for user in data]

    with open(f'./{file_name}.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=dict_data[0].keys())
        writer.writeheader()
        writer.writerows(dict_data)
    print(f"✅ {file_name}.csv has been created successfully.\n")
    return None

def export_all_customers_db():
    """Exports CSV file with All Users (Active & Deleted Customers + Agents)"""
    while True:
        try:
            file_name_raw = input("Enter a name for the csv file or 'cancel' to quit. \n").strip()
            file_name = file_name_raw.replace(" ", "")  # to clean the name of the file
            # Inputs 'cancel'
            if file_name.lower() == 'cancel':
                print("Exporting CSV file canceled.\n")
                return None

            # Input is empty
            if not file_name:
                print("❌ Input is required. Try again.")
                continue
            break
        except ValueError as e:
            print(f"❌ {e} Try again or type 'cancel' to quit.")

    # Gets the list of All User objects
    data = all_user_list.get_user_list()

    # Formats dataset as dictionary, so it can be exported as csv or json in the future. Also, easier to scale down or up
    # attributes
    dict_data = [{
        'ID': user.get_id(),
        'First Name': user.get_first_name(),
        'Last Name': user.get_last_name(),
        'Email': user.get_email(),
        'Phone Number': user.get_email(),
        'Role': user.get_role(),
        'User Status': user.get_user_status(),
        'Birth Date': user.get_dob(),
        'Age': user.get_age(),
        'Address': user.get_address(),
        'City': user.get_city(),
        'Reward Points': user.get_points(),
        'Reward Level': user.get_tag_level(),
        'VIP': user.get_vip_status(),
        'Total Spent': user.get_total_spent(),
        'Total Flights': len(user.get_flight_history()),
        'Total Bookings': len(user.get_booking_list())
    } for user in data]

    with open(f'./{file_name}.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=dict_data[0].keys())
        writer.writeheader()
        writer.writerows(dict_data)
    print(f"✅ {file_name}.csv has been created successfully.\n")
    return None

def export_customer_database():
    """Asks which database from the available ones an Agent wants to export from"""
    while True:
        try:
            print(f"Available databases to export:\n"
                  f"1. Active Customers\n"
                  f"2. All Users (includes deleted Customer accounts & Agent users)\n")
            user_choice = input("Select an option or type 'cancel' to quit: ").strip()
            if user_choice == "1":
                export_active_customers_db()
            elif user_choice == "2":
                export_all_customers_db()
            # Input is cancel
            elif user_choice.lower() == 'cancel':
                print("Exporting CSV file canceled.\n")
                return None
            # Input is empty
            if not user_choice:
                print("❌ Input is required. Try again.")
                continue
            break
        except ValueError as e:
            print(f"❌ {e} Try again or type 'cancel' to quit.")


# --- AGENT > END Functions for Customer Management --- #

# --- AGENT > START Functions for Flight Management --- #
def update_flights_date_status():
    """Sets each flight's date_status based on today's date"""
    today = date.today()
    for flight in all_flight_manager.get_flight_list():
        if flight.get_flight_date() < today:
            flight.set_date_status('Past')
            flight.set_seats_available(0)
        else:
            flight.set_date_status('Current')

def refresh_available_flights():
    """Updates the list of available flights based on current date & Confirmed flight_status"""
    available_flight_manager.clear_flight_list()
    for flight in all_flight_manager.get_flight_list():
        if flight.get_date_status() == 'Current' and flight.get_flight_status() == 'Confirmed':
            available_flight_manager.add_flight(flight)

def show_available_flights():
    """Prints the list of AVAILABLE Flight objects: total number of available flights & display flight details"""
    update_flights_date_status()
    refresh_available_flights()

    print(f"Available Flights: {len(available_flight_manager.get_flight_list())}")
    for flight in available_flight_manager.get_flight_list():
        print(flight)

def show_all_flights():
    """Prints the list of ALL Flight objects: total number of flights & display flight details"""
    update_flights_date_status()

    print(f"All Flights: {len(all_flight_manager.get_flight_list())}")
    for flight in all_flight_manager.get_flight_list():
        print(flight)


def show_flight_by_id():
    """Checks a flight by its ID & retrieves the flight details"""
    # Keeping available flights up to date
    update_flights_date_status()
    refresh_available_flights()
    while True:
        print("Enter Flight ID or Cancel: ")
        choice = input().strip()

        if choice.upper() == "CANCEL":
            break

        for flight in available_flight_manager.get_flight_list():
            if flight.get_flight_number().strip() == choice:
                total_bookings = []

                for booking in booking_list.get_booking_list():
                    if booking.get_flight_number() == choice:
                        total_bookings.append(booking)

                print(f"{flight}")
                print(f"Bookings: {len(total_bookings)}")
                for booking in total_bookings:
                    print(f"- {booking.get_booking_number()}: {booking.get_first_name()} {booking.get_last_name()}")
                return

        print("❌ Invalid option. Please select a valid one.")


def add_flight():
    """Creates a new object of class Flight & Adds it to the flight manager list"""
    global new_departure_time, new_arrival_time, new_price, new_points_by_flight, new_available_seats
    print(f"▸ Create a new flight")
    print(f"Enter 'cancel' to quit.")
    while True:
            try:
                # Flight Date
                print("Flight Date:")
                try:
                    new_day = int(input("Day (1-31): \n").strip())
                    new_month = int(input("Month (1-12): \n").strip())
                    new_year = int(input("Year (e.g. 2025): \n").strip())
                    new_flight_date = date(new_year, new_month, new_day)
                except ValueError:
                    print("❌ Invalid date. Flight creation canceled")
                    return None

                #Origin
                new_origin = input("Enter origin: \n").strip()
                if new_origin.lower() == 'cancel':
                    print("Flight creation canceled.")
                    return None

                # Flight_number Checker not needed because it's using generator id after.

                #Destination
                new_destination = input("Enter destination: \n").strip()
                if new_destination.lower() == 'cancel':
                    print("Flight creation canceled.")
                    return None
                if not new_destination:
                    print("❌ Destination is required. It cannot be empty.")
                    continue
                if not new_origin:
                    print("❌ Origin is required. It cannot be empty.")
                    continue

                # Departure Time
                new_departure_time = input("Departure Time (24-format, e.g. 9:45): \n").strip()
                if new_departure_time.lower() == 'cancel':
                    print("Flight creation canceled.")
                    return None
                if not new_departure_time:
                    print("❌ Departure Time is required. It cannot be empty.")
                    continue

                # Arrival Time
                new_arrival_time = input("Arrival Time (24-format, e.g. 9:45): \n").strip()
                if new_arrival_time.lower() == 'cancel':
                    print("Flight creation canceled.")
                    return None
                if not new_arrival_time:
                    print("❌ Arrival Time is required. It cannot be empty.")
                    continue

                # Price
                try:
                    new_price = float(input("Price (e.g. 128.25): \n").strip())
                except ValueError:
                    print("❌ Invalid Price value. Flight creation canceled")
                    return None

                # Points
                try:
                    new_points_by_flight = int(input("Reward Points (e.g. 120): \n").strip())
                except ValueError:
                    print("❌ Invalid Reward point value. Flight creation canceled")
                    return None

                # Available seats
                try:
                    new_available_seats = int(input("Available Seats: (e.g. 24): \n").strip())
                except ValueError:
                    print("❌ Invalid Seat value. Flight creation canceled")
                    return None

                #All inputs OK, exit the loop to create the new flight
                break

            except ValueError as e:
                print(f"❌ {e} Try again or type 'cancel' to quit.")

    # Create Flight object (new flight)
    new_flight = Flight(new_flight_date, new_origin.title(), new_destination.title(), new_departure_time, new_arrival_time, new_price, new_points_by_flight, new_available_seats)
    new_flight.set_flight_number()
    new_flight.set_flight_status("Confirmed") # it's set by default, but just in case

    #Flight added to All Flights Collection
    all_flight_manager.add_flight(new_flight)

    # Update date_status based on date_status of this new flight
    update_flights_date_status()
    # Refresh available flight list based on this new flight added
    refresh_available_flights()

    # Displays successful message
    print(f"✅ New flight {new_flight.get_flight_number()} has been created successfully.\n")
    print("-" * 20)
    return None

def update_flight_status():
    """Updates flight_status as Confirmed, Canceled or Completed. Once in Completed, cannot be changed."""
    # Keeping available flights up to date
    update_flights_date_status()
    refresh_available_flights()

    while True:
        print("Enter Flight ID or Cancel: ")
        choice = input().strip()

        if choice.upper() == "CANCEL":
            print("✅ You have canceled the flight status change task.\n")
            return

        flight = None
        for f in all_flight_manager.get_flight_list():
            if f.get_flight_number().strip() == choice:
                    flight = f
                    break
        if flight:
            print(f"Flight Found: {flight.get_flight_number()} | {flight.get_origin()} - {flight.get_destination()} | "
                  f"Current Status:"
                  f" {flight.get_flight_status()}")
            break #at this point: flight has been found and exiting from the current loop to go to the second one.
        else:
            print("❌ Invalid option. Please select a valid one.")


    current_status = flight.get_flight_status()
    #Time to update the flight status
    while True:
        print(f"Select an option to update the status for flight {flight.get_flight_number()} | Current status: {current_status}\n"
              f"1. Confirmed\n"
              f"2. Canceled\n"
              f"3. Completed\n"
              f"0. Cancel\n")
        user_choice = input("Select an option: ").strip()

        if user_choice == "0":
            print("✅ You have canceled the flight status change task.\n")
            return
        elif user_choice == "1":
            new_status = "Confirmed"
        elif user_choice == "2":
            new_status = "Canceled"
        elif user_choice == "3":
            if current_status == "Completed":
                print("⚠️ Completed flights cannot be updated.")
                continue
            new_status = "Completed"
        else:
            print("❌ Invalid option. Try again using from 1 to 3 to select an option, or 0 to quit.")
            continue

        # time to set the new status
        flight.set_flight_status(new_status)

        # Update bookings associated to this flight
        affected_bookings = 0
        for booking in booking_list.get_booking_list():
            if booking.get_flight_number() == flight.get_flight_number():
                # Booking status will change only is new status is different from current one
                if booking.get_status() != new_status:
                    booking.set_status(new_status)
                    affected_bookings += 1

        print(f"✅ You've updated the status successfully.\n"
              f"Flight {flight.get_flight_number()} status updated successfully to {flight.get_flight_status()}")
        print(f"{affected_bookings} bookings have been updated to match this flight status.")
        return

def remove_flight_by_flight_number():
    """Removes a flight by its flight number from flight-list & Updates flight_status as 'Deleted' in all_flight_list"""
    flight_selected = None
    while True:
        print("Enter Flight Number or Cancel: ")
        choice = input().upper().strip()

        if choice == "CANCEL":
            return None

        for flight in all_flight_manager.get_flight_list():
            if flight.get_flight_number().upper().strip() == choice:
                flight_selected = flight
                break

        if flight_selected:
            break

        print("❌ Invalid option. Please select a valid one.")

    print(
        f"Are you sure you want to delete flight {flight_selected.get_flight_number()}: {flight_selected.get_origin()}-{flight_selected.get_destination()} on {flight_selected.get_flight_date()}?\n⚠️ Everything will be lost. Issues on Customer's side may occur.\n")
    while True:
        try:
            choice = input("Enter 'delete' to delete your account or 'cancel' to quit. \n").strip()

            # Inputs 'cancel'
            if choice.lower() == 'cancel':
                print("Flight deletion canceled.\n")
                return None

            # Input is empty
            if not choice:
                print("❌ Input is required. Try again.")
                continue

            # Inputs 'delete'
            if choice.lower() == 'delete':
                flight_selected.set_flight_status('Canceled')
                available_flight_manager.remove_flight(flight_selected)
                print(f"✅ You've removed flight {flight_selected.get_flight_number()} from available flights successfully. Now it will be shown as Canceled for Customers.\n")
                return None

        except ValueError as e:
            print(f"❌ {e} Try again or type 'cancel' to quit.")

# --- AGENT > END Functions for Flight Management --- #

def show_customer_menu(user):
    """Displays the menu options for CUSTOMERS"""
    current_user = user
    while True:
        print(f"\nEnter an option:")
        print(f"1. View Available Flights\n"
              f"2. Book a Flight\n"
              f"3. View My Bookings\n"
              f"4. My Profile\n"
              f"5. Delete Account\n"
              f"0. Logout\n")
        user_choice = input("Select an option: ").strip()
        if user_choice == "1":
            show_available_flights() # Done
        elif user_choice == "2":
            book_flight(current_user) # Done
        elif user_choice == "3":
            display_booking_list_by_id(current_user) # Done
        elif user_choice == "4":
            show_customer_profile(current_user)
        elif user_choice == "5":
            remove_customer(current_user)
        elif user_choice == "0":
            print("✅ You have successfully logout.\n")
            welcome() # Done
            break
        else:
            print("❌ Invalid option. Try again using from 1 to 5 to select an option, or 0 to logout.")

# --- CUSTOMER > START Functions --- #
#show_available_flights() will be reused for both users

def book_flight(current_user):
    """prints the list of current books, add 1 book at a time through its ID based on user input. Displays Total Qty & $"""
    global user
    user = current_user
    flight_default = flight1
    # Create a Booking object
    current_booking = Booking(user, flight_default, 'Confirmed')

    # Keeping available flights up to date
    update_flights_date_status()
    refresh_available_flights()

    # Ask user input to select a flight by flight number
    print("Select a flight from the list by typing its Flight Number:")
    available_flights = available_flight_manager.get_flight_list()
    available_flight_manager.display_flight_list()

    choice = input().strip()

    for flight in available_flights:
        if flight.get_flight_number() == choice:
            if flight.get_seats_available() != 0:
                # Add that flight to the booking object
                current_booking.add_flight(flight)
                # Discount one seat available to the flight
                flight.set_seats_available((flight.get_seats_available() - 1))
                print(f"✅ You've booked the flight {flight.get_flight_number()} from {flight.get_origin()} to"
                      f" {flight.get_destination()}\n"
                      f"Total Paid: ${flight.get_price()}\n"
                      f"Reward Points Earned: {flight.get_points_by_flight()}\n")

                # Adds this booking to the Booking Collection (available from View Bookings option)
                booking_list.add_booking(current_booking)
                # Set Booking number
                current_booking.set_booking_number(flight.get_flight_number())
                # Pass the price paid for this flight to the booking record
                current_booking.set_price_paid(flight.get_price())
                # Set flight seat for this booking
                current_booking.set_flight_seat()

                # Adds this booking to User's booking list (flight history)
                user.add_flight_to_flight_history(flight)

                # Sums reward points to this user
                user_current_points = user.get_points()
                flight_points = flight.get_points_by_flight()
                user_updated_points = user_current_points + flight_points
                user.add_points(user_updated_points)

                # Adds flight's price to the User's total spent amount
                user_current_spent = user.get_total_spent()
                flight_price = flight.get_price()
                user_updated_spent = user_current_spent + flight_price
                user.add_total_spent(user_updated_spent)

                return
            else:
                print(
                    "🙏 We're sorry. We don't have more seats available for this flight. Try with a different flight or "
                    "click here to join the wait list.")
                return
    else:
        print("❌ Invalid Flight Number. Please try again.")

def display_booking_list_by_id(current_user):
    """prints the list of bookings/flights for the current user: total number of bookings & display booking details"""

    # Clear list of booking before appending the latest number of bookings for this user
    current_user.clear_booking_list()

    # Checks bookings from the list and append when they match with current user's id
    for booking in booking_list.get_booking_list():
        if current_user.get_id() == booking.get_user_id():
                    current_user.add_booking_to_booking_list(booking)

    # Prints the list of bookings that the logged user has
    print(f"You have {len(current_user.get_booking_list())} bookings:")
    for booking in current_user.get_booking_list():
        print(booking)


def show_customer_profile(current_user):
    """Displays all details available for a specified Customer"""
    # Keeping available flights up to date
    update_flights_date_status()
    refresh_available_flights()

    print(current_user.__str__())

def remove_customer(current_user):
    """Removes customer from customer list, marks user as Deleted in All user collection & removes the permission for login"""
    print("Are you sure you want to delete your account? Everything will be lost.\n")
    while True:
        try:
            choice = input("Enter 'delete' to delete your account or 'cancel' to quit. \n").strip()
            if choice.lower() == 'cancel':
                print("Account deletion canceled.\n")
                return None

            if not choice:
                print("❌ Input is required. Try again.")
                continue

            # Checks if email exists
            if choice.lower() == 'delete':
                customer_list.remove_user(current_user)
                current_user.update_user_status() # Marks as Deleted in All users database
                print("✅ You've deleted your account successfully.")
                return main()

        except ValueError as e:
                print(f"❌ {e} Try again or type 'cancel' to quit.")

# --- CUSTOMER > END Functions --- #


def create_user_account():
    """Creates & Store on-fly a new customer user. Agents are added by Admin role (out of scope)"""
    print(f"▸ Create your account ---")
    print(f"Enter 'cancel' to quit.")

    while True:
        try:
            new_email = input("Enter your email: \n").strip()
            if new_email.lower() == 'cancel':
                print("Account creation canceled.")
                return None

            if not new_email:
                print("❌ Email is required. It cannot be empty.")
                continue

            # Checks if email exists
            email_exists = False
            for u in all_user_list.get_user_list():
                if u.get_email().lower() == new_email.lower():
                    email_exists = True
                    break

            if email_exists:
                raise ValueError("❌ Email is already used. Try a different one.")
            else:
                break  # at this point, email is OK.

        except ValueError as e:
                print(f"❌ {e} Try again or type 'cancel' to quit.")

    while True:
            new_password = input('Enter your password: \n').strip()
            if new_password.lower() == 'cancel':
                print("Account creation canceled.")
                return None

            if not new_password:
                print(f"❌ Password is required. It cannot be empty.")
            else:
                break  # at this point, password is OK.

    print("Let's complete your profile.\nIt'll take 5-10 minutes.")
    print("▸ Personal Details")
    # First name
    new_first_name = input('Enter first name: \n').strip()
    if new_first_name.lower() == 'cancel':
        print("Account creation canceled.")
        return None

    # Last name
    new_last_name = input('Enter last name: \n')
    if new_last_name.lower() == 'cancel':
        print("Account creation canceled.")
        return None

    # Date of Birth
    try:
        new_day = int(input("Enter birth day (1-31): \n").strip())
        new_month = int(input("Enter birth month (1-12): \n").strip())
        new_year = int(input("Enter birth year (e.g. 1980): \n").strip())
        birth_date = date(new_year, new_month, new_day)
    except ValueError:
        print("❌ Invalid date. Account creation canceled")
        return None

    # Phone Number
    try:
        new_phone_number = int(input("Enter phone number: \n").strip())
    except ValueError:
        print("❌ Invalid phone number. Account creation canceled")
        return None

    # Address
    print("▸ Address Details")
    street = input("Street address: \n").strip()
    if street.lower() == 'cancel':
        print("Account creation canceled.")
        return None

    city = input("City: \n").strip()
    if city.lower() == 'cancel':
        print("Account creation canceled.")
        return None

    state = input("State: \n").strip()
    if state.lower() == 'cancel':
        print("Account creation canceled.")
        return None

    zip_code = input("Zip Code: \n").strip()
    if zip_code.lower() == 'cancel':
        print("Account creation canceled.")
        return None

    country = input("Country: \n").strip()
    if country.lower() == 'cancel':
        print("Account creation canceled.")
        return None

    # Create User object (new customer)
    new_address = Address(street, city, state, zip_code, country)
    new_user = User(None, new_first_name, new_last_name, new_email, new_password, new_phone_number, birth_date)
    new_user.set_role('customer')
    new_user.set_password(new_password)
    new_user.set_birth_date(birth_date)
    new_user.set_id()
    new_user.set_address(new_address)

    # Adds User object (new customer) to the customer list
    customer_list.add_user(new_user)
    all_user_list.add_user(new_user)

    # Displays successful message + New user logged in
    print("✅ Account has been created successfully.\n")
    print("-" * 20)
    print(f"Welcome {new_user.get_first_name().title()}!")
    if new_user.get_role() == 'agent':
        return show_agent_menu()
    else:
        return show_customer_menu(new_user)




# -------- START PROGRAM --------- #

welcome()
main()
# -------- END PROGRAM --------- #

# -------- START Unit Test  --------- #
#import unittest
class TestUserCreation(unittest.TestCase):
    def test_add_user_customer(self):
        """Unit Test #1: Checks user with role customer is created properly. Using User Class, setters & getters."""
        #1 Create User object
        user = User(
            id="",
            first_name="",
            last_name="",
            email="",
            password="",
            phone_number="",
            birth_date=date.today()
        )

        #2 Set user details using setters
        user.set_id_fixed("C000001")
        user.set_first_name("Leon")
        user.set_last_name("Albon")
        user.set_email("lalbol@example.com.au")
        user.set_password("aL123!")
        user.set_birth_date(date(1988, 9, 16))

        #3 Compare user details using getters
        self.assertEqual(user.get_id(), 'C000001', "Expected ID to be C000001")

class TestUserLogin(unittest.TestCase):
    """Unit Test #2: Checks login outcome: to get the user with OK email & OK password, to get None with OK email &
    WRONG password, and WRONG email & OK password."""
    #1 Clean user list & add testing user type agent
    def test_set_user(self):
        all_user_list._user_list = []
        all_user_list.add_user(agent1)

    #2 Test OK email & OK password -> outcome: user
    def test_login_correct_credentials(self):
        result = login_with_arguments("flor@sco.com.au", "Abc123")
        self.assertEqual(result.get_email(), agent1.get_email(), "Expected user")

    #3 Test WRONG email & OK password -> outcome: None
    def test_login_wrong_email(self):
        result = login_with_arguments("agent@email.com", "Abc123")
        self.assertIsNone(result, "Expected None")

    #4 Test OK email & WRONG password -> outcome: None
    def test_login_wrong_password(self):
        result = login_with_arguments(agent1.get_email(), "TUY123")
        self.assertIsNone(result, "Expected None")
# -------- END Unit Test  --------- #

# -------- START Run Unit Tests  --------- #
"""To check the Unit Tests for this project: 
. Comment the lines between # -------- PROGRAM --------- #
. Search this text '#import unittest' & Remove the '#'   
. Look at the lines below and remove the '#' from #if __name__ == '__main__': 
. and from #    unittest.main()
. Now you're able to run the unit tests 🙏
. Run the tests

Note: This has been the turn around that I found to have main script & unit tests running on the same file.
Thank you"""

#if __name__ == '__main__':  # Added to be able to run unit tests.
#    unittest.main()

# -------- END Run Unit Tests  --------- #


## End of the script - 1847863 F. Scolari KBS June 2025 TECH6100 Assessment 3

# References
# Cepalia A, (2024), Composition, Real Python, View on June 5 2025 <https://realpython.com/videos/composition/>
# Dedov F., (2022), Generate Unique IDs in Python (UUIDs), NeuralNine, View on June 5 2025 <https://youtu.be/2zsxlA0OPrY?si=Kq31Bxc6_evM_LGP>
# GeeksForGeeks, (2024), Writing CSV files in Python, GeeksForGeeks, View on June 7 2025 <https://www.geeksforgeeks.org/writing-csv-files-in-python/>
# GenAI, (2025), Design Model, Approach & Initial Pseudocode, ChatGPT, View on June 6 2025 <https://chatgpt.com/share/684141fa-ed3c-8010-9433-c88edb174aea>
# W3Schools, (2025), Python Random randrange() Method, W3Schools, View on June 5 2025 <https://www.w3schools.com/python/ref_random_randrange.asp>