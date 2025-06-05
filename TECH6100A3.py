# TECH6100 Assessment 3 Florencia Scolari ID 1847863 June 2025
# Check the full project and references on the GitHub Public Repo #todo: add link to public repo
from multiprocessing.connection import address_type

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

#todo: Create User Class
# ------ START 🙋‍♀️ USER Classes --------- #
class User:
    def __init__(self, id, first_name, last_name, email, password, role, birth_date, address, city, t):
        self.__id : str = id
        self.__first_name : str = first_name
        self.__last_name : str = last_name
        self.__email : str = email
        self.__password : str = password
        self.__role : str = role            #'agent' or 'customer'
        self.__birth_date: str = birth_date # for age calculation / filtering
        self.__address: str = address
        self.__city: str = city
        self.__total_points: int = total_points #loyalty points accumulated
        self.__total_spent: float = 0.0 # total amount spent on flights
        self.__flight_history = []  #list of Flight objects as Purchased Flight History

    #To display data from a class object to users
    def __str__(self):
        order_list_str = "\n".join([f"- ID: {order.get_order_id()}\tItems: {order.get_total_items()}\tAmount: $"
                                    f"{order.get_total_amount()}\tDate:"
                                    f" {order.get_order_date()}"
                                    for order in self.__order_history])
        return (f"# --------------- #\n"
                f"Name: {self.__first_name.title()} {self.__last_name.title()}\n"
                f"Username: {self.__username}\n"
                f"Email: {self.__email}\n"
                f"Phone Number: {self.__phone_number}\n"
                f"Shipping Address: {self.__shipping_address}\n"
                f"Purchase History: {len(self.__order_history)} orders\n"
                f"{order_list_str}\n"
        )

    # To display data from a class object to programmers
    def __repr__(self):
        return (f"------\n"
                f"Name: {self.__first_name} : {type(self.__first_name)} + {self.__last_name} :"
                f" {type(self.__last_name)}\n"
                f"Username: {self.__username} : {type(self.__username)}\n"
                f"Password: {self.__password} : {type(self.__password)}\n"
                f"Phone Number: {self.__phone_number} : {type(self.__phone_number)}\n"
                f"Shipping Address: {self.__shipping_address} : {type(self.__shipping_address)}\n"
                f"Purchase History: {self.__order_history} : {type(self.__order_history)}"
        )










#todo: Create UserManager Class