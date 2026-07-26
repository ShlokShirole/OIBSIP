import secrets
from constants import UPPER, LOWER, DIGITS, SYMBOLS

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    pool = ""
    if use_upper:
        pool += UPPER
    if use_lower:
        pool += LOWER
    if use_digits:
        pool += DIGITS
    if use_symbols:
        pool += SYMBOLS

    if not pool:
        pool = LOWER  # fallback

    return ''.join(secrets.choice(pool) for _ in range(length))
