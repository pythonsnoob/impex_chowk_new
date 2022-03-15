

import json
from signup_process import signup
from login_process import login
from data_bases import get_user_database

if __name__ == '__main__':

    userdatabase = get_user_database()

    print('Would you like to signup or login?')
    userconfirmation=input()
    if userconfirmation == "signup":

        print('Please provide your name: ')
        username = input()
        print('Please provide your email address: ')
        user_email = input()
        print('Please input a password: ')
        userpass = input()
        signup(name=username, email=user_email, password=userpass, user_database=userdatabase)
        with open("userdatabase.json", "w") as database_for_users:
            json.dump(userdatabase, database_for_users)
    else:
        print('Please provide you email: ')
        user_email = input()
        print('Please provide your password: ')
        user_password = input()
        login(email=user_email, password=user_password, user_database=userdatabase)
