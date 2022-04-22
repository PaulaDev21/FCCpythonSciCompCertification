import copy
import random

from matplotlib import colors
# Consider using the modules imported above.


class Hat:
    def __init__(self,**kargs):
        self.contents=[]
        for color, quant in kargs.items():
            for i in range(0,quant):
                self.contents.append(color)
            
    def draw(self, quant_balls):
        if quant_balls > len(self.contents):
            return random.sample(self.contents, k=len(self.contents))
        return random.sample(self.contents, k=quant_balls)





# For this project, you will write a program to determine the approximate probability of drawing certain balls randomly from a hat.


# Next, create an experiment function in prob_calculator.py(not inside the Hat class). This function should accept the following arguments:

# hat: A hat object containing balls that should be copied inside the function.
# expected_balls: An object indicating the exact group of balls to attempt to draw from the hat for the experiment. For example, to determine the probability of drawing 2 blue balls and 1 red ball from the hat, set expected_balls to {"blue": 2, "red": 1}.
# num_balls_drawn: The number of balls to draw out of the hat in each experiment.
# num_experiments: The number of experiments to perform. (The more experiments performed, the more accurate the approximate probability will be.)
# The experiment function should return a probability.
