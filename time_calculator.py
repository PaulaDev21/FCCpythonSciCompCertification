import re


def add_time(start, duration):

    start_parts = re.findall('(\d+):', start)
    start_parts += re.findall(':(\d+)\s', start)
    start_parts += re.findall("[AP]M", start)

    duration_parts = re.findall('(\d+):', duration)
    duration_parts += re.findall(':(\d+)', duration)

    if start_parts[2] == 'PM':
        start_parts[0] = int(start_parts[0]) + 12
    start_parts.pop()

    summed = []
    for i in range(0, 2):
        start_parts[i] = int(start_parts[i])
        duration_parts[i] = int(duration_parts[i])
        summed.append(start_parts[i]+duration_parts[i])

    to_print = ''
    if summed[1] > 60:
        summed[0] += summed[1] / 60
        summed[1] = summed[1] % 60

    days = 0
    if summed[0] > 24:
        days = summed[0]/24
        summed[0] %= 24

    if summed[0] > 12:
        summed[0] -= 12
        to_print = " PM"
    else:
        to_print = " AM"

    return f'{summed[0]}' + ":" + f'{summed[1]}' + to_print + " (next day)"


print(add_time("11:06 PM", "2:02"))
