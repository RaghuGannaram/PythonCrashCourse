"""
                                                                                True and False

Type:
    bool (Constant)
Values:
    True
    False
Use Cases:
    1. Represent truth values in logical operations and conditions.
    2. Control flow in conditional statements (if, while).
    3. Used in comparisons and boolean algebra.
"""

print("\n---------------- True and False ----------------")
print(True)
print(False)
print(type(True))
print(type(False))

print("\ntype conversion : boolean -> other types")
print(type(int(True)))
print(int(True))
print(int(False))
print(type(float(True)))
print(float(True))
print(float(False))
print(type(str(True)))
print(str(True))
print(str(False))


print("\nboolean conversion : other types -> boolean")
print(bool(0))
print(bool(1))
print(bool([]))
print(bool([1, 2, 3]))
print(bool(""))
print(bool("Hello"))
print(bool(None))

print("\noperating on boolean values")
print(True + False + True)
print(True * 10)
print(False - 5 + True)

try:
    print(True / False)
except Exception as error:
    print(f"Error: {error}")


"""
                                                                                        None    

Type:
    types.NoneType (Singleton)
Value:
    None
Use Cases:
    1. Default return value of functions that do not explicitly return anything.
    2. Represents the absence of a value or a null value.
    3. Used as a placeholder in function arguments or variable assignments.
"""
print("\n---------------- None ----------------")

print(None)
print(type(None))


print("\ntype conversion : None -> other types")
try:
    print(int(None))
except Exception as error:
    print(f"Error: {error}")
try:
    print(float(None))
except Exception as error:
    print(f"Error: {error}")
print(str(None))
print(bool(None))


"""
                                                                                    NotImplemented

Type:
    types.NotImplementedType (Singleton)
Returns:
    It is a return value, NOT an exception.
Use Case:
    Returned by magic methods (__eq__, __add__, etc.) to signal that 
    the operation is not supported for the given arguments.
"""
print("\n---------------- NotImplemented ----------------")


class Box:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        print("Box.__add__ called")
        # 1. If 'other' is a Box, we can add
        if isinstance(other, Box):
            return Box(self.value + other.value)

        # 2. If 'other' is an int, we can add
        if isinstance(other, int):
            return Box(self.value + other)

        # 3. If it's something else (like a string), we DON'T raise an error yet. We return NotImplemented to let the other object have a try.
        return NotImplemented

    def __radd__(self, other):
        print("Box.__radd__ called")
        # 1 This is called if "other + Box" happens and "other" gave up.
        return self.__add__(other)

    def __repr__(self):
        return f"Box({self.value})"


b = Box(10)

# Case 1: Box + Int (Box handles it)
print(b + 5, end="\n\n")

# Case 2: Int + Box (Int doesn't know 'Box', so it returns NotImplemented. Python then calls Box.__radd__, which handles it!)
print(10 + b, end="\n\n")

# Case 3: Box + String (Neither knows how to handle the other)
try:
    print(b + "Hello")
except TypeError as error:
    print(f"Error: {error}")

"""
                                                                                    Ellipsis

Type:
    types.EllipsisType (Singleton)
Value:
    ...
    Ellipsis
Use Cases:
    1. They are the exact same object.
    2. Using it as a placeholder in code (e.g., in function definitions or class bodies).
    3. The Assignment Rule: You can assign a new value to the name 'Ellipsis', but you cannot assign a new value to '...'.

"""
print("\n---------------- Ellipsis ----------------")

# 1. They are the exact same object
print(type(...))
print(type(Ellipsis))
print(... == Ellipsis)
print(... is Ellipsis)


# 2. Using it as a placeholder
def upcoming_feature_1():
    Ellipsis


def upcoming_feature_2(): ...


print(upcoming_feature_1())
print(upcoming_feature_2())

# 3. The Assignment Rule

# You CAN do this (not recommended):
Ellipsis = "I broke it"
print(Ellipsis)

# You CANNOT do this:
try:
    # ... = "New Value"  # SyntaxError: can't assign to Ellipsis, try-except block won't catch SyntaxError
    pass
except SyntaxError as error:
    print(f"Error: {error}")

print(type(...))
print(type(Ellipsis))
print(... == Ellipsis)
print(... is Ellipsis)


"""
                                                                                     __debug__

Type:
    bool (Constant)
Value:
    True (Default)
    False (if python started with -O flag)
Use:
    Determines if 'assert' statements are executed.
"""
print("\n---------------- __debug__ ----------------")

print(f"Debug Mode is: {__debug__}")

# This block only runs if optimization is OFF
if __debug__:
    print("Code is running in normal mode (slower, safer).")
else:
    print("Code is running in optimized mode (faster, assertions removed).")

# The assert test
try:
    assert 1 == 2, "Math is broken!"
    print("Assertion was IGNORED (Optimized Mode)")
except AssertionError:
    print("Assertion was CAUGHT (Debug Mode)")


"""
                                quit(code=None) / exit(code=None)

Type:
    _sitebuiltins.Quitter
Purpose:
    To close the interactive Python shell easily.
Returns:
    Raises SystemExit exception.
Warning:
    Do NOT use in production code. Use sys.exit() instead.
"""

# Interactive Shell Behavior:
# >>> quit
# Use quit() or Ctrl-Z plus Return to exit

# >>> quit()
# (The shell closes)

print("\n\n\n---------------- quit() / exit() ----------------")
try:
    # quit()
    pass
except SystemExit as error:
    print(f"SystemExit through quit(), caught with code: {error.code}")

try:
    # exit(1)
    pass
except SystemExit as error:
    print(f"SystemExit through exit(), caught with code: {error.code}")


"""
                                help(object)

Type:
    _sitebuiltins._Helper
Purpose:
    Access the built-in documentation system.
"""
# Interactive Shell:
# >>> help
# Type help() for interactive help, or help(object) for help about object.

# >>> help(len)
# Help on built-in function len in module builtins:
# len(obj, /)
#     Return the number of items in a container.
print("\n\n\n---------------- help() ----------------")
print(help)
help(len)

"""
                                copyright / credits / license

Type:
    _sitebuiltins._Printer
Purpose:
    Display legal info about the Python interpreter.
"""

# >>> copyright
# Copyright (c) 2001-2023 Python Software Foundation.
# All Rights Reserved.

# >>> license()
# (Opens a pager showing the full generic Python license)

print("\n\n\n----------------credits----------------")
print(credits)
print("\n----------------copyright----------------")
print(copyright)
print("\n----------------license----------------")
print(license)
# interactive viewer that blocks the script until you

