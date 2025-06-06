# TECH6100 Assessment 3 Florencia Scolari ID 1847863 June 2025
# Check the full project and references on the GitHub Public Repo https://github.com/florscolari/TECH6100A3.git

# NOTE: You'll find the unit tests below the script to run the program. Thank you.

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
from datetime import date #to calculate dates/age

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

def calculate_age(dob):
    """Calculates age based on date of birth with an object of class date(yyyy, m, dd)"""
    today = date.today()
    age = today.year - dob.year
    return age

# Example birth date
#birth_date = date(1990, 5, 15)
#age = calculate_age(birth_date)
#todo: when ask for date of birth: ask for dob.day = input('day'), then dob.month = input('month'), then dob.year =
# input('year'). wrap all up as dob = date(dob.year, dob.month, dob.day)

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
        self.__birth_date: date = birth_date # for age calculation / filtering
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
        return (f"# --------------- #\n"
                f"Name: {self.__first_name.title()} {self.__last_name.title()}\n"
                f"Email: {self.__email}\n"
                f"Phone Number: {self.__phone_number}\n"
                f"Date of Birth: {self.__birth_date}\n"
                f"Address: {self.__address} {self.__city}\n"
                # f"Reward Points: {self.__total_points}"
                f"Flight History: {len(self.__flight_history)} flights\n"
                # f"{order_list_str}\n"
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
        """Generates unique IDs for flight numbers"""
        item_type = "flight"
        self.__flight_number = generate_short_id(item_type)

    def set_flight_number_fixed(self, value):
        """Hardcodes a fixed IDs for flight numbers... Only for populated data purposes"""
        self.__flight_number = value

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
#todo: Adjust FlightManager Class
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
                f"Current flights: {self.__total_flights}\n")

    def display_flight_list(self):
        for flight in self.__flight_list:
            print(f"{flight.__str__()}")

    def add_flight(self, flight: Flight):
        self.__flight_list.append(flight)
        self.__total_flights += 1

    def remove_flight(self, flight: Flight):
        self.__flight_list.remove(flight)
        self.__total_flights -= 1

# ------ END ✈️✈️ FLIGHT MANAGER Classes --------- #

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

# ------ START 📗📗️ BOOKING MANAGER Class --------- #
#todo: Adjust BookingManager Class
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


#🙋 2 Customers added to have data to handle when the program starts

customer_list = UserManager("Customer Collection")
agent_list = UserManager("Agent Collection")

customer1 = User("CC", "Elle", "Doe", "test@t.com.au", "ElleD", "00000000000", None, None)
address1 = Address("000 William Street", "Perth", "WA", "6000", "Australia")
customer1.set_role(user_roles[0])
customer1.set_password('Abc123')
customer1.set_birth_date(date(1995, 5, 20))
customer1.set_id_fixed('C0f66')
customer1.set_address(address1)
customer_list.add_user(customer1)

customer2 = User("CC", "James", "Williams", "williams@t.com.au", "JD12", "111111", None, None)
address2 = Address("000 William Street", "Perth", "WA", "6000", "Australia")
customer2.set_role(user_roles[0])
customer2.set_password('Abc123')
customer2.set_birth_date(date(1999, 9, 16))
customer2.set_id_fixed('Cc618')
customer2.set_address(address2)
customer_list.add_user(customer2)

agent1 = User("AA", "Flor", "Scolari", "flor@sco.com.au", "JD12", "111111", None, None)
address2 = Address("000 William Street", "Perth", "WA", "6000", "Australia")
agent1.set_role(user_roles[1])
agent1.set_birth_date(date(1989, 1, 24))
agent1.set_password('Abc123')
agent1.set_id_fixed('Ac618')
agent1.set_address(address2)
agent_list.add_user(agent1)



all_user_list = UserManager("All Users") # to login validation purposes
all_user_list.add_user(customer1)
all_user_list.add_user(customer2)
all_user_list.add_user(agent1)
#✈️ 3 Flights added
flight_list = FlightManager("Flight Collection")
flight1 = Flight('Perth', 'Sydney', '9:25', '0:35', 489, 240, 9)
flight2 = Flight('Sydney', 'Canberra', '8:13', '9:40', 112, 45, 4)
flight3 = Flight('Canberra', 'Perth', '4:37', '7:56', 420, 220, 8)
flight1.set_flight_number_fixed('F53e0')
flight2.set_flight_number_fixed('F53e1')
flight3.set_flight_number_fixed('F53e2')
flight_list.add_flight(flight1)
flight_list.add_flight(flight2)
flight_list.add_flight(flight3)

#📗 4 Bookings added
booking_list = BookingManager('Booking Collection')
booking1 = Booking(customer1.get_id(), flight1.get_flight_number(),booking_status[0])
booking2 = Booking(customer1.get_id(), flight2.get_flight_number(),booking_status[1])
booking3 = Booking(customer2.get_id(), flight2.get_flight_number(),booking_status[1])
booking4 = Booking(customer2.get_id(), flight3.get_flight_number(),booking_status[0])

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
                if u.get_email().lower() == user_email.lower():
                    user = u
                    break

            if not user:
                raise ValueError("Email not found.")

            user_password = input('Enter your password: \n')
            if user_password.lower() == 'cancel':
                print("Login canceled.")
                return None

            # Check if hashed password matches
            if user.get_password() != hash_password(user_password):
                raise ValueError("Incorrect password.")

            print("✅ Login successful.")
            return user

        except ValueError:
            print(f"❌ Try again or type 'cancel' to quit.")

def login_with_arguments(test_email, test_password):
    """ONLY FOR UNIT TEST PURPOSE: Asks for email & password and checks if they match against records store in
    user_list"""
    # Checks if email exists
    for u in all_user_list.get_user_list():
        if u.get_email().lower() == test_email.lower():
            if u.get_password() == hash_password(test_password):
                return u
    return None

#todo: to be continued here tomorrow morning
def show_agent_menu():
    print("Here the menu for agents will be shown.")

def show_customer_menu():
    print("Here the menu for customers will be shown.")

def create_user_account():
    print("Here the user account creation will be shown.")

def welcome():
    """To welcome the user when starting the program. As Flight CRM, login is required to browse the site as
    customer or travel agent."""
    print("-" * 40)
    print("🌎✈️ Welcome to Traveliverse ✈️🌎\n"
          "Explore our offer of flights around Australia and beyond.\n"
          "Login to access your account or create a new one\n")

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
                        show_customer_menu()
        elif user_choice == "2":
                create_user_account()
        elif user_choice == "0":
            print("You have exited Traveliverse. See you next time!")
            break
        else:
            print("❌ Invalid option. Try again using from 0 to 2 to select an option.")


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
            role="",
            birth_date=date.today()
        )

        #2 Set user details using setters
        user.set_id_fixed("C000001")
        user.set_first_name("Leon")
        user.set_last_name("Albon")
        user.set_email("lalbol@example.com.au")
        user.set_password("aL123!")
        user.set_role("customer")
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
