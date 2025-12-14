def get_round(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return round(result)
    return wrapper

def check_parameters(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        for arg in args[1:]:
            if arg <= 0:
                raise ValueError("Value cannot be < or = 0")
        for arg in kwargs.values():
            if arg <= 0:
                raise ValueError("Value cannot be < or = 0")
        return result
    return wrapper