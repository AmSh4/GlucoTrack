import datetime

def get_current_timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

def validate_input(value, type_):
    if not value:
        raise ValueError("Field cannot be empty.")
    try:
        return type_(value)
    except ValueError:
        raise ValueError(f"Invalid value: {value}. Must be {type_.__name__}.")
