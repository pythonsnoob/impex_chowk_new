"""
#TODO: Add products
after the user has logged in, user should be able to add a product, when the product is added, it shoudl be added to a different data base. Design a emthod which tajes the followjng parameters: Product name, Product size, quanitty, quality and price. In theu ser database,

When the user logs in, they should have option to add or view products

If add
    Then take details and save in database
if view
    Then display the products of the user


# TODO: Read -> Importing from different files
"""

import json
from data_bases import get_user_database, get_product_database
from sign_up_process import signup
from login_process import login
from product_process import product_addition, product_view


if __name__ == '__main__':

    userdatabase = get_user_database()

    productdatabase = get_product_database()

    print('Would you like to signup / login?')
    userconfirmation=input()
    if userconfirmation == "login":
        print('Please provide you email: ')
        user_email = input()
        print('Please provide your password: ')
        user_password = input()
        login(email=user_email, password=user_password, user_database=userdatabase)

        print('Would you like to view or add products?')
        user_product_selection = input()

        if user_product_selection == 'view':
            print('You have the following products: ')
            products = product_view(
                product_database=productdatabase,
                email=user_email
            )

            print(products)

        else:
            print('Please provide the below details: ')
            print('What is the name of your product: ')

            product_name = input()
            print('Please provide the quality of your product, choose from high, medium or low')
            product_quality = input()
            print('How many products are available?')
            product_quantity = input()
            print('What is the price for your product?')
            product_price = input()

            product_addition(
                product_price=int(product_price),
                product_name=product_name,
                product_quality=product_quality,
                product_quantity=int(product_quantity),
                product_database=productdatabase,
                email=user_email
            )

            with open("productdatabase.json", "w") as database_for_products:
                json.dump(productdatabase, database_for_products)

    else:
        print('Please provide your name: ')
        username = input()
        print('Please provide your email address: ')
        user_email = input()
        print('Please input a password: ')
        userpass = input()
        signup(name=username, email=user_email, password=userpass, user_database=userdatabase)
        with open("userdatabase.json", "w") as database_for_users:
            json.dump(userdatabase, database_for_users)

