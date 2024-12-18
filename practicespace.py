print("Welcome to my python practice space")

# Syntax for printing a string of text
print("I love Python!")


# Syntax for printing numeric values
print(360)
print(32*45)


# Syntax for printing the value of a variable
value = 8*6
print(value)


# Multiplication, division, addition, and subtraction
print(3*8/2+5-1)
 
# Exponents
print(4**6) # Syntax means 4 to the power of 6
print(4**2) # To square a number
print(4**3) # To cube a number
print(4**0.5) # To find the square root of a number

# To calculate how many different possible combinations can be
# formed using a set of "x" characters with each character in "x"
# having "y" number of possible values, you will need to use an 
# exponent for the calculation:
x = 4
y = 26
print(y**x)

# Assignment of values to the variables:
years = 10
weeks_in_a_year = 52
# This variable is assigned an arithmetic calculation:
weeks_in_a_decade = years * weeks_in_a_year
# Prints the calculation stored in the "weeks_in_a_decade" variable:
print(weeks_in_a_decade)

def to_celsius(x):
   '''Convert Fahrenheit to Celsius'''
   return (x-32) * 5/9
to_celsius(75)

number = -4
if number > 0:
   print('Number is positive.')
elif number == 0:
   print('Number is zero.')
else:
   print('Number is negative.')

print(7+8.5)
print("a"+"b"+"c")
print("This " + "is " + "pretty " + "neat!")
base = 6
height = 3
area = (base*height)/2
print("The area of the triangle is: " + str(area)) 

total = 2048 + ___ + ___ + ___ + ___
files = ___
average = total / files
print("___" + str(___))

total = 2048 + 97658 + 4357 + 125 + 8
files = 5
average = total / files
print("The average size is:" + str(average))

import typing
# Define a variable of type str
z: str = "Hello, world!"
# Define a variable of type int
x: int = 10
# Define a variable of type float
y: float = 1.23
# Define a variable of type list
list_of_numbers: typing.List[int] = [1, 2, 3]
# Define a variable of type tuple
tuple_of_numbers: typing.Tuple[int, int, int] = (1, 2, 3)
# Define a variable of type dict
dictionary: typing.Dict[str, int] = {"key1": 1, "key2": 2}
# Define a variable of type set
set_of_numbers: typing.Set[int] = {1, 2, 3}

# The following lines assign the variable to the left of the = 
# assignment operator with the values and arithmetic expressions 
# on the right side of the = assignment operator.
hotel_room = 100
tax = hotel_room * 0.08
total = hotel_room + tax
room_guests = 4
share_per_person = total/room_guests


# This line outputs the result of the final calculation stored
# in the variable "share_per_person"
print("Each person needs to pay: " + str(share_per_person)) # change a data type

Each person needs to pay: 27.0

The following 5 lines assign strings to a list of variables.
salutation = "Dr."
first_name = "Prisha"
middle_name = "Jai"
last_name = "Agarwal"
suffix = "Ph.D."
 
print(salutation + " " + first_name + " " + middle_name + " " + last_name + ", " + suffix) 
# The comma as a string ", " adds the conventional use of a comma plus a 
# space to separate the last name from the suffix.
 
# Alternatively, you could use commas in place of the + connector:
print(salutation, first_name, middle_name, last_name,",", suffix)
# However, you will find that this produces a space before a comma within a string.
Dr. Prisha Jai Agarwal, Ph.D.
Dr. Prisha Jai Agarwal , Ph.D.


