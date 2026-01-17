"""
                                abs(number, /...)

parameters:
    number: int | float | complex
returns:
    The absolute value of the given number.

"""

import math


print("\n---------------- abs() ----------------")
print(abs(-5))
print(abs(-5.234))
print(abs(-3 - 4j))


"""         
                                all(iterable, /...)
parameters:
    iterable: Iterable (list, tuple, set, range, etc.)
returns:
    True if all elements in the iterable are true (or if the iterable is empty).
    False if at least one element is false.

"""
print("\n---------------- all() ----------------")
print(all([True, True, True]))
print(all([True, False, True]))
print(all([1, 2, "hello"]))
print(all([1, 2, 0]))
print(all([]))


"""         
                                any(iterable, /...)
parameters:
    iterable: Iterable (list, tuple, set, range, etc.)
returns:
    True if at least one element in the iterable is true.
    False if all elements are false (or if the iterable is empty).

"""
print("\n---------------- any() ----------------")
print(any([False, False, True]))
print(any([False, False, False]))
print(any([0, "", None, [], 5]))
print(any([0, "", None, []]))
print(any([]))


r"""         
                                ascii(object, /...)
parameters: 
    object: Any Python object.
returns:
    A string containing a printable representation of an object,
    escaping non-ASCII characters using \x, \u or \U escapes.

"""
print("\n---------------- ascii() ----------------")
print(ascii("Hello, world!"))
print(ascii("Café"))
print(ascii("你好，世界！"))
print(ascii([1, 2, 3, "Café", "你好"]))
print(ascii({"key": "value", "emoji": "😊"}))


"""                                
                                bin(number, /...)   
parameters:
    number: int
returns:
    A string representing the binary representation of the given integer.
    The string starts with the prefix '0b'.

"""
print("\n---------------- bin() ----------------")
print(bin(10))
print(bin(-10))
print(bin(0))
print(bin(255))
print(bin(-255))
print(bin(2**10))
print(bin(-1024))
print(bin(1_000_000))


"""                                bool(value=None, /...)
parameters:
    value: Any Python object.
returns:
    True if the given value is truthy.
    False if the given value is falsy or not provided.

"""
print("\n---------------- bool() ----------------")
print(bool(1))
print(bool(0))
print(bool("Hello"))
print(bool(""))
print(bool([1, 2, 3]))
print(bool([]))
print(bool({1: "a", 2: "b"}))
print(bool({}))
print(bool((1, 2)))
print(bool(()))


def bool_func1():
    pass


print(bool(bool_func1))
print(bool(bool_func1()))


def bool_func2():
    return True


print(bool(bool_func2))
print(bool(bool_func2()))


def bool_func3():
    return False


print(bool(bool_func3))
print(bool(bool_func3()))

print(bool(None))
print(bool())


"""             
                bytearray(source=b'')
                bytearray(source, encoding, errors='strict')

parameters:
    source: Optional
            if it is an integer, it specifies the size of the bytearray.
            if it is an iterable, it initializes the bytearray with the elements of the iterable which should be integers in the range 0-255.
            if it is a string, it encodes the string using the specified encoding.
    encoding: str (required if source is a string)
    errors: str (optional, default is 'strict')
returns:
    A mutable sequence of bytes.

mutatable: Yes
"""
print("\n---------------- bytearray() ----------------")
print(bytearray(5))
print(bytearray("Hello", "utf-8"))
print(bytearray([65, 66, 67, 68, 69]))
try:
    bytearray([65, 66, 300])  # This will raise a ValueError since 300 is out of range
except ValueError as error:
    print(f"Error: {error}")

bytearrray_1 = bytearray(b"Hello")
print(bytearrray_1)
bytearrray_1[0] = 74  # ASCII value of 'J'
print(bytearrray_1)


"""
                                bytes(source=b'')
                                bytes(source, encoding, errors='strict')
parameters:
    source: Optional
            if it is an integer, it specifies the size of the bytes object.
            if it is a string, it encodes the string using the specified encoding.
            if it is an iterable, it initializes the bytes object with the elements of the iterable which should be integers in the range 0-255.
    encoding: str (required if source is a string)
    errors: str (optional, default is 'strict') 
returns:
    An immutable sequence of bytes.
    
mutatable: No
"""
print("\n---------------- bytes() ----------------")
print(bytes(5))
print(bytes("Hello", "utf-8"))
print(bytes([65, 66, 67, 68, 69]))
try:
    bytes([65, 66, 300])  # This will raise a ValueError since 300 is out of range
except ValueError as error:
    print(f"Error: {error}")

bytes_1 = bytes(b"Hello")
print(bytes_1)
try:
    bytes_1[0] = 74  # This will raise a TypeError since bytes are immutable
except TypeError as error:
    print(f"Error: {error}")
print(bytes_1)


"""
                                callable(object, /...)  
parameters:
    object: Any Python object.
returns:
    True if the given object is callable (i.e., can be called as a function).
    False otherwise.

"""
print("\n---------------- callable() ----------------")


def callable_func():
    pass


print(callable(callable_func))
print(callable(42))
print(callable("Hello"))
print(callable([]))
print(callable({}))


class CallableClass:
    def __call__(self):
        pass


sample_instance = CallableClass()
print(callable(sample_instance))


class NonCallableClass:
    pass


non_callable_instance = NonCallableClass()
print(callable(non_callable_instance))


"""
                                chr(codepoint, /...)
parameters:
    codepoint: int, a Unicode code point. throw ValueError if the code point is out of range (0 to 0x10FFFF).
returns:
    A string representing the character corresponding to the given Unicode code point.

"""
print("\n---------------- chr() ----------------")
print(chr(65))
print(chr(97))
print(chr(8364))
print(chr(128512))

try:
    print(chr(0x110000))  # This will raise a ValueError since it's out of range
except ValueError as error:
    print(f"Error: {error}")


"""
                                complex(string, /...)
                                complex(number=0, /...)
                                complex(real=0, imag=0)
parameters:
    string: str (optional)
            A string representing a complex number.
    number: int | float | complex (optional)
            A real number to be converted to a complex number.
    real: int | float (optional)
            The real part of the complex number.
    imag: int | float (optional)
            The imaginary part of the complex number.
returns:
    A complex number.

"""
print("\n---------------- complex() ----------------")
print(complex("3+4j"))
print(complex("-2"))
print(complex("-1.5j"))
try:
    print(complex("3+4"))
    # print(complex("5 - 2j"))
    # print(complex("invalid"))
except ValueError as error:
    print(f"Error: {error}")

print(complex(5))

print(complex(real=2, imag=3))
print(complex(2.5, -1.5))

print(complex())


"""
                                delattr(object, name, /...)
parameters:
    object: Any Python object.
    name: str
          The name of the attribute to be deleted.
returns:
    None

"""
print("\n---------------- delattr() ----------------")


class DelAttrClass:
    def __init__(self):
        self.attribute1 = "value1"
        self.attribute2 = "value2"


delattr_instance = DelAttrClass()
print(delattr_instance.attribute1)
delattr(delattr_instance, "attribute1")
try:
    print(delattr_instance.attribute1)
except AttributeError as error:
    print(f"Error: {error}")
print(delattr_instance.attribute2)


"""
                                dir()
                                dir(object, /...)
parameters:
    object: Optional
            Any Python object.
returns:
    A list of names in the current local scope if no object is provided.
    A list of valid attributes for the given object if an object is provided.

"""
print("\n---------------- dir() ----------------")
print(dir())


class DirClass:
    def method1(self):
        pass

    def method2(self):
        pass


dir_instance = DirClass()
print(dir(dir_instance))


r"""                                divmod(a, b, /...)
parameters:
    a: int | float
    b: int | float
returns:
    returns (a // b, a % b) if a, b are integers.
    returns (math.floor(a / b), a % b) if a, b are floats.
    
note: 
    While the quotient value is calculated like math.floor(a / b), the data type differs.
    math.floor() returns an 'int', whereas divmod() (and //) with floats returns a 'float'.

"""
print("\n---------------- divmod() ----------------")
print(divmod(10, 3))
print(divmod(10.0, 3.0))
print(divmod(10.5, 3.2))
print(10.5 // 3.2)
print(math.floor(10.5 / 3.2))


"""
                                enumerate(iterable, start=0)
parameters:
    iterable: Iterable (list, tuple, set, range, etc.)
    start: int (optional, default is 0)
returns:
    An enumerate object that yields pairs of index and value from the given iterable,
    starting from the specified start index.

"""
print("\n---------------- enumerate() ----------------")

sample_list = ["a", "b", "c", "d"]
for index, value in enumerate(sample_list):
    print(index, value)

print("---- Starting from index 1 ----")
for index, value in enumerate(sample_list, start=1):
    print(index, value)

print("---- Starting from index '-2' ----")
for index, value in enumerate(sample_list, start=-2):
    print(index, value)


"""
                                eval(source, /, globals=None, locals=None)

parameters:
    source:  str | code object
             A single Python expression (e.g., "1 + 1", "x * 5", "my_list[0]").
             It CANNOT be a statement (like "x = 5" or "import os").
    globals: dict | None (Optional)
             The dictionary to use for global variables.
    locals:  mapping | None (Optional)
             The dictionary to use for local variables.

returns:
    The result of the evaluated expression.

warning:
    This executes arbitrary code. NEVER use this on user input (e.g., from a website form)
    without extreme strictness, or hackers can delete your files.
"""

print("\n---------------- eval() ----------------")

x = 10
print(eval("x + 5"))

print(eval("len('hello')"))

op = "*"
print(eval(f"10 {op} 5"))

try:
    eval("x = 50")  # Crash! Assignment is a statement, not an expression.
except SyntaxError as e:
    print(f"Error: {e}")


print(eval("x + 5", {"x": 20}, {"x": 50}))


"""
                                exec(source, /, globals=None, locals=None)

parameters:
    source:  str | code object
             A block of Python code (statements, loops, class defs, imports).
    globals: dict | None (Optional)
    locals:  mapping | None (Optional)

returns:
    None (It always returns None).

warning:
    Same security risk as eval(), but even more dangerous because it can import modules.
"""

print("\n---------------- exec() ----------------")

code_block = """
z = 10
for i in range(3):
    z += i
print('Inside exec, z is:', z)
"""

exec(code_block)
# Output: Inside exec, z is: 13

# 2. Variable persistence
# The variable 'z' created inside exec() is now available in our code!
# (Note: This behavior depends on how locals are passed, see below).
print(f"it could access z: {z}")  # Might print 13 depending on scope


"""
                                filter(function, iterable, /...)
parameters:
    function: function | None
              A function that tests each element of the iterable.
              If None, it defaults to the identity function (returns the element itself).
    iterable: Iterable (list, tuple, set, range, etc.)
returns:
    An iterator that yields elements from the iterable for which the function returns True. 

"""
print("\n---------------- filter() ----------------")


def is_even(n):
    return n % 2 == 0


numbers = [1, 2, 3, 4, 5, 6]
print(list(filter(is_even, numbers)))


print(list(filter(None, [0, 1, "", "Hello", [], [1, 2], None, True, False])))


"""                                float(value=0.0, /...)
parameters:
    value: int | float | str | bytes | bytearray (optional)
returns:
    A floating-point number constructed from the given value.
    
"""
print("\n---------------- float() ----------------")
print(float(5))
print(float(5.67))
print(float("3.14"))