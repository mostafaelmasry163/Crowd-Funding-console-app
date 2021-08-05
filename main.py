# All modules imported here
from project_actions import Project
from register import User

# All objects created here ( user object - project object )
new_user = User()
new_project = Project()

# Registration or Login
while True:
    user_type = input("If you are a new user Enter 1  \n"
                      "If you are an old one Enter 2  \n"
                      "Type here :    ")

    if user_type == "1":
        new_user.Register_new_user()
        break
    elif user_type == "2":
        new_user.login()
        break
    else:
        print("invalid , try again")
################################################################

new_project.new_action(new_user.email)
while True:
    user_decision = input("Do you want to do another thing ? \n"
                          "Enter Y for yes \n"
                          "Enter N for No \n"
                          "Type here : ")
    if user_decision.upper() == "N":
        print("thanks for using our application")
        break
    elif user_decision.upper() == "Y":
        new_project.new_action(new_user.email)
    else:
        print("invalid, Try again")

