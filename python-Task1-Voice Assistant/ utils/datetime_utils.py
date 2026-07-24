import datetime


def get_time():
    """
    Return the current time.
    """
    return datetime.datetime.now().strftime("%I:%M %p")


def get_date():
    """
    Return the current date.
    """
    return datetime.datetime.now().strftime("%d %B %Y")
