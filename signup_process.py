def signup(name: str, email: str, password: str, user_database: dict) -> None:

    if email in user_database:
        print('Error: You already have an account registered with this email!')
        exit()

    else:
        user_database[email] = {
            "name": name,
            "email": email,
            "password": password
        }
        print('you are signing up')