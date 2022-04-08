import re


def add_time(start, duration):
  print(re.findall('\d+:\d+\s[AP]M', start))

  return 'incomplete'


print(add_time("11:06 PM", "2:02"))
