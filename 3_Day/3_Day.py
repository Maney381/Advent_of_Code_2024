import regex as re

with open('data.txt', 'r') as data:
    result = 0
    data_all = data.read()
    pattern = r'mul(?:\()(\d{1,3},\d{1,3})(?:\))'
    test = re.findall(pattern, data_all)
    for match in test:
        num1, num2 = match.split(',')
        result += int(num1) * int(num2)

print('Answer to question 1: {}'.format(result))

with open('data.txt', 'r') as data:
    result = 0
    data_all = data.read()
    pattern = r'(mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\))'
    matches = re.findall(pattern, data_all)
    enable = True
    for match in matches:
        if match == "do()":
            enable = True
            continue
        if match == "don't()":
            enable = False
            continue
        if enable == True:
            pattern = r'(?:\()(\d{1,3},\d{1,3})(?:\))'
            num1, num2 = re.findall(pattern, match)[0].split(',')
            result += int(num1) * int(num2)

print('Answer to question 2: {}'.format(result))
