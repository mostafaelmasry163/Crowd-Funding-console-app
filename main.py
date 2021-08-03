# All modules imported here
from project_actions import Project

# All objects created here ( user object - project object )
new_project = Project("new_user.email")

# Registration or Login
while True:
    user_type = input("If you are a new user Enter 1  \n"
                      "If you are an old one Enter 2  \n"
                      "Type here :    ")

    if user_type == "1":
        print("Registration")  # call Registeration fn
        print("Login")  # call login fn
        break
    elif user_type == "2":
        print("Login")  # call login fn
        break
    else:
        print("invalid , try again")
################################################################

new_project.new_action()
while True:
    user_decision = input("Do you want to do another thing ? \n"
                          "Enter Y for yes \n"
                          "Enter N for No \n"
                          "Type here : ")
    if user_decision == "N":
        print("thanks for using our application")
        break
    elif user_decision == "Y":
        new_project.new_action()
    else:
        print("invalid, Try again")

