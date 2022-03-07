import random


def get_product_id(product: str) -> str:
    product_id = product+get_rand_int()
    return product_id


def get_rand_int() -> str:
    pakistan = random.randint(1111, 9999)
    return str(pakistan)


def get_user_id(email: str) -> str:
    user_email_list = email.split('@')
    user_id = user_email_list[0]
    return user_id
