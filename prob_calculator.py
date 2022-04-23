import copy
import random



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


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    if total_balls(expected_balls) > num_balls_drawn:
        print("Drawing too few balls, draw more")
        return 0 
    
    equal_expected=0

    for i in range(num_experiments):
        balls = hat.draw(num_balls_drawn)
        drawn_balls  = count_balls_by_color(balls)
        if contains(drawn_balls, expected_balls):
            equal_expected += 1
        
    return equal_expected/num_experiments

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

for i in range(6):
    n_exp = 10 ** (i + 1) 
    print(experiment(h, {"blue": 2, "red": 1}, 5, n_exp))
