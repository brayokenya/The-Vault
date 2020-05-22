# start
from user import User


def displayMenu():
    status = input("Are you registered user? y/n? \tPress q to quit::").lower()
    if status == "y":
        login()
    elif status == "n":
        register()


def register():
    username = input("Enter username: ")
    password = input("Enter password: ")
    password2 = input("Confirm password: ")

    # validation
    if password == password2:
        # print("Password did not match!!!!")
        # password = input("Enter password")
        # password2 = input("Confirm password")
        # create user
        user = User(username, password)
        user.save_user
        print(f"Welcome {username}! You're now registered")
    else:
        print("Something went wrong. Please try again.")


def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    user = User(username, password)
    if user is not None:
        user.login
        print(f"Welcome {username}! You're now Logged In")
    else:
        print("Invalid Username or Password.")


displayMenu()


# def newUser():
#     createLogin = input("Create login name: ")

#     if createLogin in users:
#         print("\nLogin name already exist!\n")
#     else:
#         createPassw = input("Create password: ")
#         users[createLogin] = createPassw
#         print("\nUser created\n")
#         print(oldUser())


# def oldUser():
#     login = input("Enter login name: ")
#     passw = input("Enter password: ")

#     if login in users and users[login] == passw:
#         print("\nLogin successful!\n")

#     else:
#         print("\nUser doesn't exist or wrong password!\n")


# while status != "q":
#     displayMenu()

# end
