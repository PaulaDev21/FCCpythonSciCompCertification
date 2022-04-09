# This entrypoint file to be used in development. 
from time_calculator import add_time
from unittest import main


print(add_time("11:06 PM", "2:02"))


# Run unit tests automatically
main(module='test_time', exit=False)
