import math

#Question 1-----------------------------------------------------------------------
# Use double precision, calculate the resulting values (format to 5 decimal places)
binarystr = "0100000001111110101110010000000000000000000000000000000000000000"

def bintofloat (binarystr):
    s = int(binarystr[0])
    c = 0
    f = 0
    for i in range(1, 12):
        c += int(binarystr[i]) * pow(2,(11-i))

    for i in range(12, 63):
        f += int(binarystr[i]) * pow(0.5, (i-11))

    output = (-1)**s * 2**(c-1023) * (1+f)
    return output

print(bintofloat(binarystr))
print()

#Question 2----------------------------------------------
#Repeat exercise 1 using three-digit chopping arithmetic

Val = bintofloat(binarystr)

ChopVal = float(math.floor(Val))

print(ChopVal)
print()

#Question 3----------------------------------------------
# Repeat question 1 using three-digit rounding arithmetic

RoundVal = Val + 0.0005
RoundVal = float(round(RoundVal))

print(RoundVal)
print()

# Question 4-------------------------------------------------------------------------------------------
# Compute the absolute and relative error with the exact value form question 1 and its 3 digit rounding
abs_error = abs(Val - RoundVal)

rel_error = abs_error / Val

print(abs_error)
print(rel_error)
print()


# Question 5-------------------------------------------------------------------
# What is the minimum number of terms needed to computer f(1) with error <10^-4?

def series_error():

    def infinite_series(x, k: int):
        return ((-1) ** k) * ((x ** k) / (k ** 3))

    minimum_error = .0001
    iteration_counter = 1

    while abs(infinite_series(1, iteration_counter)) > minimum_error:
        iteration_counter += 1

    iteration_counter = iteration_counter - 1
    print(iteration_counter, "\n")

series_error()

# Question 6 ---------------------------------------------------------------------
# Determine the number of iterations necessary to solve f(x) = x^3 + 4x^2 - 10 = 0
# with accuracy 10^-4 using a = -4 and b = 7.

#      a) Using the bisection method


def bisection(left: float, right: float, given_function: str):
    x = left
    intial_left = eval(given_function)
    x = right
    intial_right = eval(given_function)

    if intial_left * intial_right >= 0:
        print("Invalid inputs. Not on opposite sides of the function")
        return

    tolerance: float = .0001
    diff: float = right - left

    max_iterations = 20
    iteration_counter = 0

    while (diff >= tolerance and iteration_counter <= 20):
        iteration_counter += 1

        mid_point = (left + right) / 2
        x = mid_point
        evaluated_midpoint = eval(given_function)

        if evaluated_midpoint == 0.0:
            break


    x = left
    evaluated_left_point = eval(given_function)

    first_conditional: bool = evaluated_left_point < 0 and evaluated_midpoint > 0
    second_conditional: bool = evaluated_left_point > 0 and evaluated_midpoint < 0

    if first_conditional or second_conditional:
        right = mid_point

    else:
        left = mid_point

    diff = abs(right - left)
    return (iteration_counter)

left = -4
right = 7
function_string = "x**3 - (4*(x**2)) - 10"

print(bisection(left, right, function_string))

#      b) Using the newton raphson method

def custom_derivative(value):
    return (3 * value* value) - (2 * value)

def newton_raphson(initial_approximation: float, tolerance: float, sequence: str):
    # remember this is an iteration based approach...
    iteration_counter = 0
    # finds f
    x = initial_approximation
    f = eval(sequence)
    # finds f'
    f_prime = custom_derivative(initial_approximation)

    approximation: float = f / f_prime
    while (abs(approximation) >= tolerance):
        # finds f
        x = initial_approximation
        f = eval(sequence)
        # finds f'
        f_prime = custom_derivative(initial_approximation)
        # division operation
        approximation = f / f_prime
        # subtraction property
        initial_approximation -= approximation
        iteration_counter += 1
    return (iteration_counter)

initial_approximation: float = 7
tolerance: float = .0001
sequence: str = "x**3 + (4*(x**2)) - 10"
print(newton_raphson(initial_approximation, tolerance, sequence))