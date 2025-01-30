
# program to check if the square root of a number entered is integer or not
def is_square(n):
    sqrt = n ** 0.5 
    return print(sqrt.real.is_integer())
is_square(0)