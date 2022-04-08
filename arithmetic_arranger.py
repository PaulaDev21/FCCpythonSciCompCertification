import re

from numpy import arange

IN_BETWEEN_SPACE = "    "
MAX_QUESTIONS = 5
MAX_ERRORS = 5


def arithmetic_arranger(problems, print_result=False):
    if len(problems) > MAX_QUESTIONS:
        return "Error: Too many problems."

    (is_valid, errors) = valid(problems)

    if not is_valid:
        errors_str = ''
        for error in errors:
            errors_str += error
        return errors_str

    printing_data = extract_parts(problems)
    printing_data.append(print_result)

    stringToPrint = organize_printing(printing_data)

    return stringToPrint


def organize_printing(printing_data):
    (upper_numbers,
     lower_numbers,
     operators,
     print_result) = printing_data

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

        dashes_string += create_dashes_line(expression_space)
        upper_string += create_upper_line(upper_numbers[i], expression_space)
        lower_string += create_lower_line(lower_numbers[i],
                                          operators[i], expression_space)
        if (print_result):
            results_string += create_result_line(upper_numbers[i],
                                                 lower_numbers[i],
                                                 operators[i], expression_space)
    return join_lines(upper_string, lower_string, dashes_string, results_string, print_result)


def create_dashes_line(expression_space):
    new_dashes = ''
    for n in range(0, expression_space):
        new_dashes = new_dashes+'-'

    while len(new_dashes) < expression_space:
        new_dashes = ' ' + new_dashes
    return new_dashes + IN_BETWEEN_SPACE


def create_upper_line(upper_number, expression_space):
    while len(upper_number) < expression_space:
        upper_number = ' '+upper_number

    return upper_number + IN_BETWEEN_SPACE


def create_lower_line(lower_number, operator, expression_space):
    while len(lower_number) < expression_space - 2:
        lower_number = ' ' + lower_number
    new_lower = operator + ' ' + lower_number

    return new_lower + IN_BETWEEN_SPACE


def create_result_line(upper_number, lower_number, operator, expression_space):
    new_result = add_result(upper_number,
                            lower_number,
                            operator, expression_space)
    while len(new_result) < expression_space:
        new_result = ' ' + new_result

    return new_result


def join_lines(upper_string, lower_string, dashes_string, results_string, print_result):
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


def add_result(upper_number, lower_number, operator, expression_space):
    new_result = ''
    n1 = int(upper_number)

    n2 = re.findall('\s*(\d+)', lower_number)
    n2 = int(n2[0])

    if operator == '+':
        new_result += f'{n1 + n2}'
    else:
        new_result += f'{n1 - n2}'

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

    return [upper_numbers, lower_numbers, operators]


# ---------------------------VALIDATION FUNCTIONS-------------------------------
def valid(problems):
    error_messages = []
    found_error = False
    if (problems == [] or problems == None):
        error_messages.append(
            "No expressions found. Provide expressions for calculations\n")
        found_error = True
    else:
        found_error = False

    for problem in problems:

        found_error = detect_errors(problem, error_messages)
        if found_error:
            break

    if (found_error):
        return (False, error_messages)

    return (True, [])


def detect_errors(problem, errors):
    found_error = False

    parts = re.findall('\w+\s+|[+-]|\s+\w+', problem)
    if len(parts) < 3:
        errors.append("Error: Operator must be '+' or '-'.")
        found_error = True

    for part in parts:
        part = part.strip()
        if len(part) > 4:
            errors.append(
                "Error: Numbers cannot be more than four digits.")
            found_error = True

    if find_internal_errors(parts, errors) != []:
        found_error = True

    return found_error


def find_internal_errors(parts, errors):

    for elem in parts:
        if re.findall('[A-Za-z]', elem) != []:
            errors.append("Error: Numbers must only contain digits.")
        elif re.findall('[*/]', elem) != []:
            errors.append("Error: Operator must be '+' or '-'.")

    if len(errors) == MAX_ERRORS:
        return "Error: Too many errors."

    return errors


print(arithmetic_arranger(['98 + 35', '3801 - 2', '45 + 43', '123 + 49']))
