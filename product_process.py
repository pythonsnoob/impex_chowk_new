from utils import get_user_id, get_product_id
from typing import List


def product_addition(
        product_price: int,
        product_name: str,
        product_quality: str,
        product_quantity: int,
        email: str,
        product_database: dict
) -> None:

    print('You are now adding a new product!')

    product_id = get_product_id(product_name)
    product_info = {
        "product_name": product_name,
        "product_price": product_price,
        "product_quality": product_quality,
        "product_quantity": product_quantity
    }
    if email in product_database:
        product_database[email][product_id] = product_info
    else:
        product_id_data = {
            product_id: product_info
        }
        product_database[email] = product_id_data


def product_view(product_database: dict, email: str) -> List[dict]:
    user_id = get_user_id(email)
    if user_id in product_database:
        return product_database[user_id]
    else:
        print('You do not have any products.')
