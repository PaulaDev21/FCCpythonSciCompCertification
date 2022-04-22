from category import Category
from math import floor
import numpy as np

def create_spend_chart(categories):
    title = "Percentage spent by category"
    (names, percents) = prepare_data(categories)
    to_print = build_histogram(names, percents)
    to_print = title + '\n' + to_print
    return to_print

def prepare_data(categories):
    names = []
    percents = []
    total = 0
    for cat in categories:
        names.append([*cat.get_name()])
        current_withdraw = cat.get_withdraws()
        percents.append(current_withdraw)
        total += current_withdraw

    for i in range(0, len(percents)):
        percents[i] = floor(percents[i]*10/total)

    return (names, percents)


def build_histogram(names, percents):
    y_labels = build_labels_y()
    x_labels = build_labels_x(names)

    hist_body = build_histogram_body(percents, len(y_labels), y_labels)
    hist_body += build_horiz_line(len(names))
        
    return hist_body + x_labels


def build_horiz_line(quant_categories):
    x_line = '    --'
    while len(x_line) < 3*(quant_categories+1):
        x_line += '---'
    x_line + '--'
    return x_line


def build_labels_y():
    labels = []
    for perc in range(100, -10, -10):
        if perc == 0:
            labels.append('  ' + str(perc) + '|')
        elif perc == 100:
            labels.append(str(perc) + '|')
        else:
            labels.append(' ' + str(perc) + '|')
    return labels


def build_labels_x(names):

    big = 0
    for name in names:
        if len(name) > big:
            big = len(name)

    for name in names:
        while len(name) < big:
            name.append(' ')

    labels = ''
    for line in np.transpose(names):
        new_line = '  '.join(line)
        labels += '\n     ' + new_line + '  '

    return labels


def build_histogram_body(percents, scale, y_labels):
    body = build_histogram_core(percents, scale)
    return build_histogram_top(body, y_labels)


def build_histogram_top(body, y_labels):
    i = 0
    new_body = ''

    for h_line in np.transpose(body):
        new_line = ''.join(y_labels[i]) + ' ' + '  '.join([*h_line])
        new_body += new_line + '  \n'
        i += 1
    return new_body

def build_histogram_core(percents, scale):
    core = []
    for size in percents:
        col = []
        for i in range(1, scale-size):
            col.append(' ')
        while len(col) < scale:
            col.append('o')
        core.append(col)
    return core

def compare_results(output, manual):
    print(f"\nLen(output): {len(output)}")
    print(f"Len(manual): {len(manual)}\n")

    new_output = ''
    new_manual = ''
    for i in range(0,len(output)):
        
        # if (output[i] != manual[i]):
        #     print(f"i: {i}\noutuput = {ord(output[i])}({output[i]}) manual = {ord(manual[i])}({manual[i]})")
        #     print(f"output: {output[i-1]}")
        #     print(f"manual: {manual[i-1]}")
        #     count += 1
        #     if count == 10:
        if output[i] == ' ':
            new_output += '-'
        elif output[i] == '\n':
            new_output += '*\n'
        else:
            new_output += output[i]
    
    for i in range(0,len(manual)):
        if manual[i] == ' ':
            new_manual += '-'
        elif manual[i] == '\n':
            new_manual += '*\n'
        else:
            new_manual += manual[i]

    # for i in range(0,10):
    #     print(new_output[i] + ' <===> ' + new_manual[i])
    
    print(new_output, '\n', new_manual, len(new_output), len(new_manual))
    return
        





# =====================================
c = Category("Entertainment")
c.deposit(1000, "open account")
c.deposit(20, 'freela')
c.withdraw(195.78, 'party')

d = Category("Food")
c.transfer(500,d)
d.withdraw(128.40, "market")
d.withdraw(35.00, "bus")
e = Category("Clothes")
e.deposit(400, "new category")
e.withdraw(50, 'blouse')
e.withdraw(79, 'Pants')

# print(c)
# print(d)
# print(e)


# food = Category("Food")
# food.deposit(1000, "initial deposit")
# food.withdraw(10.15, "groceries")
# food.withdraw(15.89, "restaurant and more food for dessert")
# print(food.get_balance())
# clothing = Category("Clothing")
# food.transfer(50, clothing)
# clothing.withdraw(25.55)
# clothing.withdraw(100)
# auto = Category("Auto")
# auto.deposit(1000, "initial deposit")
# auto.withdraw(15)

# print(create_spend_chart([food, clothing, auto]))

goal = "Percentage spent by category\n100|          \n 90|        \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "


bis = Category('Business')
bis.deposit(100)

food = Category('Food')
food.deposit(100)
food.withdraw(70)

ent = Category('Entertainment')
ent.deposit(100)
ent.withdraw(20)

computed = create_spend_chart([bis, food, ent])
print("MINE: \n" + computed)
print("GOAL:\n" + goal)
compare_results(computed, goal)
