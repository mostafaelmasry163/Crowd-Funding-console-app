
import pymongo
import re
import openpyxl

#data = {'fname':'user1', 'lname':'user1', 'email':'user1@user.gmail.com' , 'password':1234 , 'mobile': '01112220333'}
#crowdfund_collection.insert_one(data)

def user_Register (fname,lname,email,password,mobile):
    client = pymongo.MongoClient()
    crowdfund_database = client ["crowdfund_database"]
    crowdfund_collection = crowdfund_database ["crowdfund_user"]
    new_user = {
        'fname':fname,
        'lname':lname,
        'email':email,
        'password':password,
        'mobile':mobile
    }

    check_user ={
        'email':email
    }

    if not crowdfund_collection.find_one(check_user):
        return crowdfund_collection.insert_one(new_user)

    else:
        print ("Registeration failed;this email already used")
        return False

def get_user_fname():
    global fname
    fname = input ("Enter your First name:")
    if not fname or fname.isdecimal():
        print(">>>Please enter valid user name<<<")
        get_user_fname()
    else:
        get_user_lname()
    return

def get_user_lname():
    global lname
    lname = input ("Enter your Last name:")
    if not lname or lname.isdecimal():
        print(">>>Please enter valid user name<<<")
        get_user_lname()
    else:
        get_user_email()
    return

def get_user_email():
    regex_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    global email
    email = input ("Enter your Email:")
    if not (re.match(regex_email, email)):
        print (">>>Enter a valid Email<<<")
        get_user_email()
    else:
        get_user_password()
    return
def get_user_password():
    global password
    password = input ("Enter your Password:")  
    confirm_password =input("Confirm Password:")
    if confirm_password != password:
        print (">>>Password does not match<<<")
        get_user_password()
    else:
        get_user_mobile()
    return
def get_user_mobile():
    global mobile
    mobile = input ("Enter your Mobile phone:")
    if (isValid(mobile)):
        print ("---User Successfuly Added---")
        return
    else:
        print (">>>please add valid egyption phone number<<<")
        get_user_mobile()
    return

def isValid(s):
    Pattern = re.compile("(01)?[0-2][0-9]{8}")
    return Pattern.match(s)


get_user_fname()
#user_Register (fname,lname,email,password,mobile)

inv_file = openpyxl.load_workbook("users_data.xlsx")

