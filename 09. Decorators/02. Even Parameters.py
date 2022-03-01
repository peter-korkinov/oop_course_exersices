def even_parameters(func):
    def wrapper(*args):
        for i in args:
            if type(i) is not int or i % 2 != 0:
                return 'Please use only even numbers!'

        return func(*args)
    return wrapper

