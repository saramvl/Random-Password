import random
import string

def generate_password():
    chars = string.ascii_lowercase + string.digits

    password = ""

    for i in range(8):
        password += random.choice(chars)

    return password
