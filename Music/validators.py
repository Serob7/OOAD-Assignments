from functools import wraps


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


def positive_number_checker(field_name, position):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            value = args[position]
            if not isinstance(value, (int, float)) and value < 0:
                raise ValueError(f"{field_name} should be positive integer or floating point number")
            return func(*args, **kwargs)
        return wrapper
    return decorator




