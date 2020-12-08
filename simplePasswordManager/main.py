from user import User, add_user, get_user


# function for registration, check if user input is valid
def register(username, email, password, confirmPW):
    if username == "" or email == "" or password == "" or confirmPW == "":
        print("Input field was left empty!")
    elif len(username) > 30 or len(email) > 30 or len(password) > 30:
        print("Username, email and password can only be 30 characters long!")
    elif password != confirmPW:
        print("Entered passwords do not match!")
    else:
        add_user(username, email, password)
        print("Your registration was successful!")


# function for user logon, check if user exists and if password is correct
def login(username, password):
    if username == "" or password == "":
        print("Username or password is empty!")
    else:
        user = get_user(username)
        if not user:
            print("No user with this username found!")
        else:
            if user.password == password:
                print("Logged in successfully!")
            else:
                print("Wrong password!")


# Welcome message + user chooses between login and register
print("\nWelcome to Rueschy's simple password-manager! \nWould you like to SIGN-IN or to REGISTER yourself? \n ")
choice = input("Type 'login' or 'register' \n")

# check if user wants to login or register
if choice == "login":
    print("### LOGIN ### \n")
    username = input("Enter username: ")
    password = input("Enter password: ")
    login(username, password)
elif choice == "register":
    print("### REGISTRATION ### \n")
    username = input("Enter username: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    confirmPW = input("Enter password again: ")
    register(username, email, password, confirmPW)
else:
    print("Wrong input!")
