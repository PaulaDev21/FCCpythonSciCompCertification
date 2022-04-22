from math import floor

from more_itertools import last
# Do NOT edit nor remove any existing code when testing or submitting
def my_function(input):
    # Place your code here
    digits = []
    for c_digit in input:
        digits.append(int(c_digit))
    return digits
        
print(my_function(90))
