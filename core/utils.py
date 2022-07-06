from random import choice
import string
import validators

def is_valid_url(url: string):
    return validators.url(url)

def generate_short_id(num_of_chars: int):
    return ''.join(choice(string.ascii_letters+string.digits) for _ in range(num_of_chars))