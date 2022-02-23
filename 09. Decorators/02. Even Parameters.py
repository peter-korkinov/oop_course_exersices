def even_parameters(func):
    def wrapper(*args):
        for i in args:
            try:
                i = int(i)
            except ValueError:
                return 'Please use only even numbers!'

            if i % 2 != 0:
                return 'Please use only even numbers!'

        return func(*args)
    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add('Peter', 1))
