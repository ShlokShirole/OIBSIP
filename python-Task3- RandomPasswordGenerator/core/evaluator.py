from constants import SYMBOLS, COLOR_WEAK, COLOR_MEDIUM, COLOR_STRONG

def evaluate_strength(password, use_upper, use_lower, use_digits, use_symbols):
    length = len(password)
    score = 0

    if length >= 12:
        score += 3
    elif length >= 8:
        score += 2
    elif length >= 6:
        score += 1

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in SYMBOLS for c in password)

    variety = sum([has_upper, has_lower, has_digit, has_symbol])
    enabled = sum([use_upper, use_lower, use_digits, use_symbols])

    if enabled > 0 and variety >= enabled:
        score += 2
    elif variety >= 3:
        score += 1

    if has_symbol:
        score += 1

    if score >= 6:
        return "STRONG", COLOR_STRONG
    elif score >= 4:
        return "MEDIUM", COLOR_MEDIUM
    else:
        return "WEAK", COLOR_WEAK
