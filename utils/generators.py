# utils/generators.py
import random
import string


def generate_random_email(domain="@test.com"):
    random_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
    return random_name + domain

def generate_random_password(length=8):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))
