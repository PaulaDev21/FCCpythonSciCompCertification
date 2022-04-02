import re
import string

EXPRESSION_SPACE = 7
IN_BETWEEN_SPACE = "    "
MAX_QUESTIONS = 5
MAX_ERRORS = 5


def arithmetic_arranger(problems, print_result=False):
    if len(problems) > MAX_QUESTIONS:
        print(f"Too many expressions. Maximun allowed are {MAX_QUESTIONS}")
        return

    if not valid(problems):
        return

    print("\nLet's learn arithmetic!\n")
    (upper_numbers, lower_numbers, operators) = extract_parts(problems)

    printing_data = [upper_numbers, lower_numbers, operators, print_result]
    stringsToPrint = organize_printing(printing_data)

    for line in stringsToPrint:
        print(line)
    print()


def organize_printing(printing_data):
    (upper_numbers, lower_numbers, operators, print_result) = printing_data
    upper_string = ''
    lower_string = ''
    dashes_string = ''
    results_string = ''
    for i in range(0, len(operators)):
        new_dashes = ''
        for n in range(0, len(upper_numbers[i])+1):
            new_dashes = new_dashes+'-'

        while len(new_dashes) < EXPRESSION_SPACE:
            new_dashes = ' ' + new_dashes
        dashes_string += new_dashes + IN_BETWEEN_SPACE

        while len(upper_numbers[i]) < EXPRESSION_SPACE:
            upper_numbers[i] = ' '+upper_numbers[i]
        upper_string += upper_numbers[i] + IN_BETWEEN_SPACE

        lower_numbers[i] = operators[i] + ' ' + lower_numbers[i]

        while len(lower_numbers[i]) < EXPRESSION_SPACE:
            lower_numbers[i] = ' ' + lower_numbers[i]

        lower_string += lower_numbers[i] + IN_BETWEEN_SPACE

# IS THAT WORKING?
        if (print_result):
            new_result = ''
            n1 = int(upper_numbers[i])

            n2 = re.findall('\s(\d+)', lower_numbers[i])
            n2 = int(n2[0])

            if operators[i] == '+':
                new_result += str(n1 + n2)
            else:
                new_result += str(n1 - n2)

            while len(new_result) < EXPRESSION_SPACE:
                new_result = ' ' + new_result
            new_result += IN_BETWEEN_SPACE
            results_string += new_result

    return [upper_string, lower_string, dashes_string, results_string]


def extract_parts(problems):
    upper_numbers = []
    lower_numbers = []
    operators = []
    for problem in problems:
        parts = re.findall('\d+\s|[+-]|\s\d+', problem)
        if len(parts[0]) > len(parts[2]):
            upper_numbers.append(parts[0].strip())
            lower_numbers.append(parts[2].strip())
        else:
            upper_numbers.append(parts[2].strip())
            lower_numbers.append(parts[0].strip())
        operators.append(parts[1].strip())

    return (upper_numbers, lower_numbers, operators)


# ---------------------------VALIDATION FUNCTIONS-------------------------------
def valid(problems):
    error_messages = []
    if (problems == [] or problems == None):
        error_messages.append(
            "No expressions found. Provide expressions for calculations")
        found_error = True
    else:
        found_error = False

    for problem in problems:
        found = detect_errors(problem, error_messages)
        if (found):
            found_error = True
            continue

    if (found_error):
        for error in error_messages:
            print("----\n", error, "\n----")
            return False

    return True


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


#arithmetic_arranger(["32 + 169", "3801 - 2", "45 + 43", "1223 + 49"], True)
arithmetic_arranger(["50 + 30"], True)
