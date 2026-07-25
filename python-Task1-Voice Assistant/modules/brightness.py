import screen_brightness_control as sbc


def increase():
    current = sbc.get_brightness()[0]
    sbc.set_brightness(min(current + 10, 100))


def decrease():
    current = sbc.get_brightness()[0]
    sbc.set_brightness(max(current - 10, 0))


def set_brightness(value):
    sbc.set_brightness(value)


def get_brightness():
    return sbc.get_brightness()[0]
