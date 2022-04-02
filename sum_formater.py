import re

EXPRESSION_SPACE = 7
IN_BETWEEN_SPACE = "    "


def arithmetic_arranger(problems, print_result=False):
    if len(problems) > 5:
        print("Too many problems. Maximun allowed are 5")
        return

    if not valid(problems):
        return ''

    print("\nLet's learn arithmetic!\n")
    (upper_numbers, lower_numbers, operators) = extract_parts(problems)
    
    printing_data = [upper_numbers, lower_numbers, operators, print_result]
    stringsToPrint = organize_printing(printing_data)

    for line in stringsToPrint:
        print(line)


def organize_printing(printing_data):
    (upper_numbers, lower_numbers, operators, print_result) = printing_data
    upper_string=''
    lower_string=''
    dashes_string=''
    results_string=''
    for i in range(0,len(operators)):
        new_dashes = ''
        for n in range(0, len(upper_numbers[i])+1):
            new_dashes = new_dashes+'-'        

        while len(new_dashes) < EXPRESSION_SPACE:
            new_dashes = ' ' + new_dashes      
        dashes_string += new_dashes + IN_BETWEEN_SPACE 

        while len(upper_numbers[i]) < EXPRESSION_SPACE:
            upper_numbers[i] = ' '+upper_numbers[i]
        upper_string +=  upper_numbers[i] + IN_BETWEEN_SPACE
        
        lower_numbers[i] = operators[i] + ' ' + lower_numbers[i]
        
        while len(lower_numbers[i]) < EXPRESSION_SPACE:
            lower_numbers[i] = ' '+ lower_numbers[i]
        
        lower_string +=  lower_numbers[i] + IN_BETWEEN_SPACE

# IS THAT WORKING?
        if (print_result):
            n1 = int(upper_numbers[i])
            n2 = int(lower_numbers[i])

            if operators[i] == '+':
                results_string += n1 + n2
            else:
                results_string += n1 - n2
            
            while len(results_string) < EXPRESSION_SPACE:
                results_string = ' ' + results_string
            results_string += IN_BETWEEN_SPACE 

    return [upper_string, lower_string, dashes_string, results_string]


def extract_parts(problems):
    upper_numbers=[]
    lower_numbers=[]
    operators=[]
    for problem in problems:        
        parts = re.findall('\d+\s|[+-]|\s\d+',problem)
        if len(parts[0]) > len(parts[2]):
            upper_numbers.append(parts[0].strip())
            lower_numbers.append(parts[2].strip())
        else:
            upper_numbers.append(parts[2].strip())
            lower_numbers.append(parts[0].strip())
        operators.append(parts[1].strip())

    return (upper_numbers, lower_numbers, operators)   




#---------------------------VALIDATION FUNCTIONS-------------------------------
def valid(problems):
    error_messages=[]
    foundError=False
    for problem in problems:
        found = detect_errors(problem, error_messages)
        if (found):
            foundError = True
            continue
    
    if (foundError):
        for error in error_messages:
            print(error)
            return False

    return True


def detect_errors(problem, errors):
    badProblem = re.findall('[^\d+\-\s]', problem)
    if badProblem == []:
        parts = re.findall('\d+\s|[+\-]|\s\d+',problem)
        
        for part in parts:
            part = part.strip()
            if len(part) > 4:
                errors.append("Number should have a maximun of 4 digits.")
                return True            
        return False
    else:
        transcribe_errors(badProblem, errors)
        return True


def transcribe_errors(arr, errors): 
    if len(arr) == 5:
            return ["Too many errors! Are you sure you're using the right tool?"]

    for elem in arr:   

        if re.match('[A-Za-z]',elem):
            errors.append("Arithmetic expressons can't have letters.")
        elif re.match('[*/]', elem):
            errors.append("Not allowed operation, only + and - are valid.")
        else:
            errors.append("Your expression should have only numbers and + or - operators.")

    return errors



arithmetic_arranger(["32 + 169", "3801 - 2", "45 + 43", "1223 + 49"])