from random import choice, randint
from string import ascii_letters
import hashlib


def get_token():
    ALPHABET = ascii_letters + '1234567890!@#$%^*()!№;:'
    return ''.join([choice(ALPHABET) for _ in range(randint(10, 30))])


def make_password(password):
    return hashlib.md5(password.encode()).hexdigest()
