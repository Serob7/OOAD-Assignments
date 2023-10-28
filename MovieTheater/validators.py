from functools import wraps
import re


def not_empty_string(field_name, position):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            value = args[position]
            if isinstance(value, str) and value.strip():
                return func(*args, **kwargs)
            raise ValueError(f"{field_name} should not be empty or other than a string type")
        return wrapper
    return decorator

def positive_integer_checker(field_name, position):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            value = args[position]
            if not isinstance(value, int) and value < 0:
                raise ValueError(f"{field_name} should be positive integer")
            return func(*args, **kwargs)
        return wrapper
    return decorator

def positive_number_checker(field_name, position):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            value = args[position]
            if not isinstance(value, (int, float)) and (value < 0 or value > 10):
                raise ValueError(f"{field_name} should be positive integer or floating point number from 0 - 10")
            return func(*args, **kwargs)
        return wrapper
    return decorator

def email_checker(field_name, position):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            value = args[position]
            email_regex = r'^[a-zA-Z0-9_.+=-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
            if not re.match(email_regex, value):
                raise ValueError(f"Fill in valid email address in {field_name} field")
            return func(*args, **kwargs)
        return wrapper
    return decorator



