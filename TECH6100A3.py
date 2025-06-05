# TECH6100 Assessment 3 Florencia Scolari ID 1847863 June 2025
# Check the full project and references on the GitHub Public Repo #todo: add link to public repo

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

#todo: Create User Class
# ------ START 🙋‍♀️ USER Classes --------- #
def generate_short_id():
    return uuid.uuid4().hex[:6]  # First 6 characters of the UUID

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


class User:
    def __init__(self, id, first_name, last_name, email, password, role, birth_date):
        self.__id : str = id
        self.__first_name : str = first_name
        self.__last_name : str = last_name
        self.__email : str = email
        self.__password : str = password
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

    def get_role(self):
        return self.__role

    def get_address(self):
        return self.__address

    def get_flight_history(self):
        return self.__flight_history

    # User Setters:
    def set_id(self):
        self.__id = generate_short_id()

    def set_first_name(self, value):
        self.__first_name = value

    def set_last_name(self, value):
        self.__last_name = value

    def set_email(self, value):
        self.__email = value

    def set_password(self, value):
        self.__password = hash_password(value)

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

# ------ END 🙋‍♀️ USER Classes --------- #









#todo: Create UserManager Class