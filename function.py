############################################ function statement ###########################################
def greet(name="World"):
    # return "Hello, {}!".format(name)
    # return "Hello, {0}!".format(name)
    # return "Hello, {name}!".format(name=name)
    # return f"Hello, {name}!"
    return "Hello, " + name + "!"


print(greet("John"))
print(greet())

############################################# lambda function #############################################
add = lambda x, y: x + y

print(add(5, 3))


############################################## lexical clouser #############################################


def add_maker(base):
    return lambda x: x + base


add_five = add_maker(5)
add_ten = add_maker(10)

print(add_five(1))
print(add_ten(1))
