def egg_count(display_value):
    return bin(int(display_value)).lstrip('0b').count('1')
