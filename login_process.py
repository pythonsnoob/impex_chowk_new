def login(email: str, password: str, user_database: dict, incorrect_pass_count: int = 1) -> None:

    if email in user_database:
        user_contents = user_database[email]
        user_password = user_contents['password']
        if user_password == password:
            print('You have successfully logged in')
            print('you are logging in')
        else:
            print(incorrect_pass_count)
            if incorrect_pass_count < 3:
                print('Incorrect password, please try again')
                print("Please input your password again")
                trying_again_password = input()
                login(email=email, password=trying_again_password, user_database=user_database,incorrect_pass_count=incorrect_pass_count+1)
            else:
                print('You have entered too many incorrect passwords, you are locked out.')