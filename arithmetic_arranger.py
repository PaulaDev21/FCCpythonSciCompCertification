import re
from unittest import result

# EXPRESSION_SPACE = 5
IN_BETWEEN_SPACE = "    "
MAX_QUESTIONS = 5
MAX_ERRORS = 5


def arithmetic_arranger(problems, print_result=False):
    if len(problems) > MAX_QUESTIONS:
        return "Too many expressions. Maximun allowed are + MAX_QUESTIONS"

    (is_valid, errors) = valid(problems)

    if not is_valid:
        return errors

    (upper_numbers, lower_numbers, operators) = extract_parts(problems)

    printing_data = [upper_numbers, lower_numbers, operators, print_result]
    stringsToPrint = organize_printing(printing_data)

    return stringsToPrint


def organize_printing(printing_data):
    (upper_numbers, lower_numbers, operators, print_result) = printing_data
    upper_string = ''
    lower_string = ''
    dashes_string = ''
    results_string = ''

    for i in range(0, len(operators)):
        expression_space = 0
        if len(upper_numbers[i]) > len(lower_numbers[i]):
            expression_space = len(upper_numbers[i]) + 2
        else:
            expression_space = len(lower_numbers[i]) + 2

        new_dashes = ''
        for n in range(0, expression_space):
            new_dashes = new_dashes+'-'

        while len(new_dashes) < expression_space:
            new_dashes = ' ' + new_dashes
        dashes_string += new_dashes + IN_BETWEEN_SPACE

        while len(upper_numbers[i]) < expression_space:
            upper_numbers[i] = ' '+upper_numbers[i]

        upper_string += upper_numbers[i] + IN_BETWEEN_SPACE

        while len(lower_numbers[i]) < expression_space - 2:
            lower_numbers[i] = ' ' + lower_numbers[i]
        new_lower = operators[i] + ' ' + lower_numbers[i]

        lower_string += new_lower + IN_BETWEEN_SPACE

        if (print_result):
            new_result = add_result(upper_numbers[i],
                                    lower_numbers[i],
                                    operators[i])
            while len(new_result) < expression_space:
                new_result = ' ' + new_result
            new_result += IN_BETWEEN_SPACE

    upper_string = upper_string.rstrip() + '\n'
    lower_string = lower_string.rstrip() + '\n'
    if print_result:
        dashes_string = dashes_string.rstrip() + '\n'
        results_string = results_string.rstrip()
    else:
        dashes_string = dashes_string.rstrip()

    to_print = upper_string + lower_string + dashes_string
    if print_result:
        to_print += results_string

    return to_print


def add_result(upper_number, lower_number, operator):
    new_result = ''
    n1 = int(upper_number)

    n2 = re.findall('\s(\d+)', lower_number)
    n2 = int(n2[0])

    if operator == '+':
        new_result += str(n1 + n2)
    else:
        new_result += str(n1 - n2)

    while len(new_result) < expression_space:
        new_result = ' ' + new_result
    new_result += IN_BETWEEN_SPACE

    return new_result


def extract_parts(problems):
    upper_numbers = []
    lower_numbers = []
    operators = []
    for problem in problems:
        parts = re.findall('\d+\s|[+-]|\s\d+', problem)

        upper_numbers.append(parts[0].strip())
        lower_numbers.append(parts[2].strip())

        operators.append(parts[1].strip())

    return (upper_numbers, lower_numbers, operators)


# ---------------------------VALIDATION FUNCTIONS-------------------------------
def valid(problems):
    error_messages = []
    if (problems == [] or problems == None):
        error_messages.append(
            "No expressions found. Provide expressions for calculations\n")
        found_error = True
    else:
        found_error = False

    for problem in problems:
        found = detect_errors(problem, error_messages)
        if (found):
            found_error = True
            continue

    if (found_error):
        return (False, error_messages)

    return (True, [])


def detect_errors(problem, errors):
    found_error = False
    if type(problem) != type(''):
        errors.append(
            "Bad formatting error. Only positive numbers are allowed")
        found_error = True
    else:
        badProblem = re.findall('[^\d+\-\s]', problem)

        if badProblem == []:
            parts = re.findall('\d+\s+|[+-]|\s+\d+', problem)
            if len(parts) < 3:
                errors.append('Expression should have spaces around operator')
                found_error = True
            for part in parts:
                part = part.strip()
                if len(part) > 4:
                    errors.append("Number should have a maximun of 4 digits.")
                    found_error = True
                elif len(part) < 1:
                    errors.append(
                        "Expression should be formated as: number operator number")
            if found_error:
                transcribe_errors(badProblem, errors)

        else:
            errors.append(
                "Expression bad formating. Try 34 + 192, for example")
            transcribe_errors(badProblem, errors)
            found_error = True
    return found_error


def transcribe_errors(arr, errors):
    if len(arr) == MAX_ERRORS:
        return ["Too many errors! Are you sure you're using the right tool?"]

    for elem in arr:

        if re.match('[A-Za-z]', elem):
            errors.append("Arithmetic expressons can't have letters.")
        elif re.match('[*/]', elem):
            errors.append("Not allowed operation, only + and - are valid.")
        else:
            errors.append(
                "Your expression should have only numbers and + or - operators.")

    return errors


# arithmetic_arranger(["32 + 169", "3801 - 2", "45 + 43", "1223 + 49"], True)
str = arithmetic_arranger(['3801 - 2', '123 + 49'])

print(str)
