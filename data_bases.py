import json


user_database = {}



def get_user_database() -> dict:
    try:
        with open("userdatabase.json", "r") as user_file:
            user_database_string = user_file.read()
            final_user_database = json.loads(user_database_string)
            return final_user_database
    except FileNotFoundError:
        with open("userdatabase.json", "w") as database_for_users:
            json.dump({}, database_for_users)
