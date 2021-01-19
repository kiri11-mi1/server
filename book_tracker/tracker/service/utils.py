from random import choice, randint
from string import ascii_letters

def get_token():
    ALPHABET = ascii_letters + '1234567890!@#$%^*()!№;:'
    return ''.join([choice(ALPHABET) for _ in range(randint(10, 30))])
