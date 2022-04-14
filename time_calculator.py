import re
import math
from zmq import NULL

WEEKDAYS = ["Sunday", "Monday", "Tuesday",
            "Wednesday", "Thursday", "Friday", "Saturday"]


def add_time(start, duration, weekday=NULL):

    (start_parts, duration_parts) = find_values(start, duration)
    (summed, days) = summing_times(start_parts, duration_parts)
    return print_new_time(summed, days, weekday)


def print_new_time(summed, days, weekday):

    to_print = set_am_pm(summed)
    set_minutes(summed)

    to_print = f'{summed[0]}' + ":" + f'{summed[1]}' + to_print

    if weekday != NULL:
        position = WEEKDAYS.index(weekday.capitalize())
        position += days
        position %= 7
        to_print += f', {WEEKDAYS[position]}'

    if (days == 1):
        to_print += ' (next day)'
    elif days > 1:
        to_print += f' ({days} days later)'

    return to_print


def set_minutes(summed):
    if summed[1] == 0:
        summed[1] = '00'
    elif summed[1] < 10:
        summed[1] = '0'+f'{summed[1]}'


def set_am_pm(summed):
    if summed[0] > 12:
        summed[0] -= 12
        to_print = " PM"
    elif summed[0] == 12:
        to_print = " PM"
    else:
        to_print = " AM"
        if summed[0] == 0:
            summed[0] = '12'

    return to_print


def find_values(start, duration):
    start_parts = re.findall('(\d+):', start)
    start_parts += re.findall(':(\d+)\s', start)
    start_parts += re.findall("[AP]M", start)

    duration_parts = re.findall('(\d+):', duration)
    duration_parts += re.findall(':(\d+)', duration)

    return (start_parts, duration_parts)


def set_universal_time(start_parts):
    if start_parts[2] == 'PM':
        if start_parts[0] != 12:
            start_parts[0] = int(start_parts[0]) + 12


def summing_times(start_parts, duration_parts):
    set_universal_time(start_parts)
    summed = []
    for i in range(0, 2):
        start_parts[i] = int(start_parts[i])
        duration_parts[i] = int(duration_parts[i])
        summed.append(start_parts[i]+duration_parts[i])

    if summed[1] > 60:
        summed[0] += math.trunc(summed[1] / 60)
        summed[1] = summed[1] % 60

    days = 0
    if summed[0] > 24:
        days = math.trunc(summed[0]/24)
        summed[0] = summed[0] % 24


    return (summed, days)


print(add_time("11:40 AM", "0:25"))
