import json


user_database = {}
product_database = {}


def get_user_database() -> dict:
    with open("userdatabase.json", "r") as user_file:
        user_database_string = user_file.read()
        final_user_database = json.loads(user_database_string)
        return final_user_database


def get_product_database() -> dict:
    with open("productdatabase.json", "r") as product_file:
        product_database_string = product_file.read()
        final_product_database = json.loads(product_database_string)
        return final_product_database