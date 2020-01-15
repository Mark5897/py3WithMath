from fractions import Fraction

# Basic math example from python
exampleOne = 1 + 1 - 1 * 2 / 2
print("Basics: 1 + 1 - 1 * 2 / 2 = ", exampleOne)

# floor division
currentExample = 5 // 3
print("Floor Division: 5 // 3 = ", currentExample)

# floor division with neg
currentExample = 5 // -3
print("Floor Division Neg: 5 // -3 = ", currentExample)

# modulo operation
currentExample = 5 % 3
print("Modulo Op: 5 % 3 = ", currentExample)

# exponential operation
currentExample = 5 ** 2
print("Exponential Op: 5 ** 2 = ", currentExample)

# fractional exponential operation (can be used for square roots, cube roots, etc)
currentExample = 5 ** (1/2)
print("Fractional Exponential Op: 5 ** (1/2) = ", currentExample)

# use float() and int() to convert between the two types. 3.0 != 3
# built in fraction support by a python module.
fractionOne = Fraction(1, 2)
print(fractionOne)

# fraction example
fractionOne = Fraction(3, 4) + 1 + Fraction(1, 4)
print(type(fractionOne))
print("3/4 + 1 + 1/4 = ", fractionOne)

# complex number example, the letter j represents the i, the imaginary part.
# cannot use % or // operators with complex nums. complex has many methods available for different actions.
# the cmath module from the standard lib contains many methods as well.
complexNumA = 2 + 4j
complexNumB = complex(2, 4)
print(type(complexNumA), "  ", type(complexNumB))
print(complexNumA, " ", complexNumB)

# here are some input taking examples
userIn = input("Please enter a string: ")
print(userIn)

# how to handle exceptions in python
try:
    userIn = float(input("Enter a number: "))
except ValueError:
    print("Bad input, I caught this error!")

# quick example of using is_integer() method to filter the .0's from floating point numbers
print(5.5.is_integer())  # false
print(5.0.is_integer())  # true

# the range function and how it works (for loops)
for i in range(0, 4):
    print("value: ", i)


# method for printing the factors of a number
def factors_of_integer(num_a):
    for i_a in range(1, num_a+1):
        if (num_a % i_a) == 0:
            print(i_a)


# tests the above method
factors_of_integer(25)

# brief example of formatting in python
print("This string uses labels {0} and {1} thus {2}".format(1, 2, 3))


# method for printing out multiplication tables, up to 10 for an integer.
def multi_tables(num_b):
    for i_b in range(1, 11):
        print("{0} X {1} = {2}".format(num_b, i_b, (num_b * i_b)))


# tests the above method
multi_tables(50)

# using format to round a float to 2 decimals.
print("{0:.2f}".format(5.555555555))


# Temperature method, converts between Celsius and Fahrenheit.
def convert_fahrenheit(temp_a):
    celsius_a = (temp_a - 32) * (5/9)
    print(celsius_a)


# tests the above method
convert_fahrenheit(98.6)


# method for calculating the quadratic formula roots. form: ax**2 + bx + c = 0
def quadratic_formula_calc(a_quad, b_quad, c_quad):
    # The Quadratic formula roots are
    # x1 = (-b_quad + (b_quad**2 - 4 * a_quad * c_quad)**0.5) / 2 * a_quad
    # x1 = (-b_quad - (b_quad**2 - 4 * a_quad * c_quad)**0.5) / 2 * a_quad
    # can write a smaller version by letting d = (b_quad**2 - 4 * a_quad * c_quad)**0.5
    # first, calculate d.
    d_quad = (b_quad**2 - 4 * a_quad * c_quad)**0.5
    # then calculate each root.
    x1_quad = (-1 * b_quad + d_quad) / 2 * a_quad
    x2_quad = (-1 * b_quad - d_quad) / 2 * a_quad
    # print results
    print("The roots are: {0} and {1}".format(x1_quad, x2_quad))


# tests out method above for "real" roots.
quadratic_formula_calc(1, 2, 1)

# tests out method above for "imaginary" roots.
quadratic_formula_calc(1, 1, 1)
