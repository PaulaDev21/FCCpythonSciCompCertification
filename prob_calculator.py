import copy as cp
import random

class Hat:
    def __init__(self,**kargs):
        self.contents=[]
        for color, quant in kargs.items():
            for i in range(0,quant):
                self.contents.append(color)
            
    def draw(self, quant_balls):        
        #random.shuffle(self.contents)        
        if quant_balls > len(self.contents):
            return self.contents
        my_sample = random.sample(self.contents,k=quant_balls)
        self.remove(my_sample)
        return my_sample
    
    def remove(self,sample):
        for color in sample:
            pos = self.contents.index(color)
            self.contents.pop(pos)

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    if len(expected_balls) > num_balls_drawn:
        print("Drawing too few balls, draw more units")
        return 0 
    
    got_it=0

    for i in range(num_experiments):
        new_hat = cp.deepcopy(hat)
        balls = new_hat.draw(num_balls_drawn)
        drawn_balls  = count_balls_by_color(balls)
        if contains(drawn_balls, expected_balls):
            got_it += 1
        
    return got_it/num_experiments

def total_balls(obj):
    total = 0
    for color in obj:
        total += obj[color] 
    return total


def count_balls_by_color(balls):
    content = {}
    for ball in balls:
        if ball in content.keys():
            content[ball] += 1
        else:
            content[ball] = 1
    return content

def contains(drawn_balls, expected_balls):
    if len(drawn_balls.keys()) < len(expected_balls.keys()):
        return False

    found_balls={}
    for color in expected_balls:
        if color in drawn_balls.keys():
            if drawn_balls[color] < expected_balls[color]:
                return False
            else:
                found_balls[color] = expected_balls[color]
        else:
            return False
    
    if found_balls == expected_balls:
        return True

    return False

#---------------------QUICK TEST---------------------------
h = Hat(blue=10, red=3, orange=8)

for i in range(4):
    n_exp = 10 ** (i + 1) 
    print(experiment(h, {'orange': 1, 'red': 1}, 10, n_exp))
