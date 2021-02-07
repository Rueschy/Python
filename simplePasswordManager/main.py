from user import User, add_user, get_user
from item import Item, add_item, get_item, get_all_items
import bcrypt


# function for registration, check if user input is valid
def register(username, email, password, confirmPW):
    if username == "" or email == "" or password == "" or confirmPW == "":
        print("Input field was left empty!")
    elif len(username) > 30 or len(email) > 30 or len(password) > 30:
        print("Username, email and password can only be 30 characters long!")
    elif password != confirmPW:
        print("Entered passwords do not match!")
    else:
        password = password.encode("utf-8")
        hashed = bcrypt.hashpw(password, bcrypt.gensalt(rounds=15))
        add_user(username, email, hashed)
        print("\nYour registration was successful!")


# function for user logon, check if user exists and if password is correct
def login(username, password):
    if username == "" or password == "":
        print("Username or password is empty!")
        return False
    else:
        user = get_user(username)
        if not user:
            print("\nNo user with this username found!")
            return False
        else:
            password = password.encode("utf-8")
            if bcrypt.checkpw(password, user.password):
                print("\nLogged in successfully!")
                return True
            else:
                print("Wrong password!")
                return False


# function to add a new item to the database
def add(item_name, item_username, item_password):
    if item_name == "" or item_username == "" or item_password == "":
        print("Name, username or password is empty!")
        return False
    else:
        add_item(item_name, item_username, item_password)
        print("\n Item added successfully!\n")


# Welcome message + user chooses between login and register
print("\nWelcome to Rueschy's simple password-manager! \nWould you like to SIGN-IN or to REGISTER yourself? \n ")
choice = input("Type 'login' or 'register' \n")

# check if user wants to login
if choice == "login":
    print("### LOGIN ### \n")
    username = input("Enter username: ")
    password = input("Enter password: ")
    success = login(username, password)

    # if login was successful, the user can show all saved items, show a specific item,
    # add/delete/update an item or exit the program
    if success:
        while True:
            print("### Welcome " + username + "! ###\n")
            choice = input("Select an option: \n <show all> \n <show> \n <add> \n <delete> \n <update> \n <exit> \n")

            if choice == "show all":
                print("### Showing all items! ###\n")
                pass

            elif choice == "show":
                print("### Showing item! ###\n")
                pass

            elif choice == "add":
                print("### Add new item! ###\n")
                item_name = input("Enter item name: ")
                item_username = input("Enter username: ")
                item_password = input("Enter password: ")
                add(item_name, item_username, item_password)

            elif choice == "delete":
                print("### Deleting item! ###\n")
                pass

            elif choice == "exit":
                print("Exiting the program!\n")
                break

# check if user wants to register
elif choice == "register":
    print("### REGISTRATION ### \n")
    username = input("Enter username: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    confirmPW = input("Enter password again: ")
    register(username, email, password, confirmPW)
    print("\nThank you for your registration! Please restart the program to continue! \n")
else:
    print("Wrong input!")
