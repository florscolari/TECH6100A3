# TECH6100 Assessment 3 Florencia Scolari June 2025

NOTE: You'll find the unit tests below the script to run the program.
Please follow the instructions to activate them.
Thank you.

# Reward Program Conditions applied by the system:
A customer is VIP when more than 1200 are earned & more than 4 flights.
A customer is also Silver level when they have 0-1 flights, Premium when 2-4, and Black with 5 or more flights

# In scope:
- User management: Create new customer account, Delete customer account, ID creation, Read customer details (my profile),
    store deleted accounts for travel agent purposes, login for 2 roles (customer & agent), filter & show users
    by  age range, by id, by city they live in
- Flight management: Create & Delete flights, change status, Show available flights & show all flights, flight number creation
- Bookings: Create bookings, Show all bookings, show bookings by user_id, update status linked to flight status
- Program Rewards & VIP labels: tagging-user labels done by the program based on conditions above
# Reporting: Export Current Customer db and Export All Customer db, both in csv file.

# Out of scope:
# 1. Global command to cancel an ongoing task in some cases.
# 2. System creates Customer users by default. Agents are added by Admin role (out of scope)
# 3. When flight is removed from Agent's side, no notifications or Actions are taken on Customer's side
# 4. My bookings displays all bookings even they are Past date and Canceled. (No condition for no display past bookings has been set)
# 5. Reward points Qty is set by the agent when creating a new flight (not by any condition run by the system)
# 6. Some user inputs don't have full validation.
# 7. Although I have set __str__ & __repr__ for User, Flight & Booking, I've used __str__ in most cases instead of __repr__
# 8. No UD Operations for bookings from Customer side. Only Create & Read. Agent updates flight states and impacts on booking status.
