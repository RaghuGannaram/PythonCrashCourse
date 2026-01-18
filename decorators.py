def custom_decorator_1(func):
    def wrapper(*args, **kwargs):
        print("Custom Decorator 1: Before function call")
        result = func(*args, **kwargs)
        print("Custom Decorator 1: After function call")
        return result

    return wrapper


def custom_decorator_2(func):
    def wrapper(*args, **kwargs):
        print("Custom Decorator 2: Before function call")
        result = func(*args, **kwargs)
        print("Custom Decorator 2: After function call")
        return result

    return wrapper


@custom_decorator_1
@custom_decorator_2
def greet(name):
    print(f"Hello, {name}!")


greet("Alice")


def custom_logger(func):
    def wrapper(*args, **kwargs):
        print(
            f"Function '{func.__name__}' is about to be called with arguments: {args} and keyword arguments: {kwargs}"
        )
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' has been called and returned: {result}")
        return result

    return wrapper


@custom_logger
def add(a, b, /, c, d, *, e=10, f=20):
    return a + b + c + d + e + f


add(3, 5, 7, d=9, e=15, f=25)


# write a decorator example that describes the decorator arguments
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


@repeat(3)
def say_hello():
    print("Hello!")


say_hello()
