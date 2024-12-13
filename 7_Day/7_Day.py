with open('sample_data.txt') as file:
    calculations = []
    while True:
        line = file.readline().strip('\n')
        if line:
            result, numbers = line.split(':')
            numbers = numbers.strip().split(' ')
            calculations.append([int(result)] + [int(number) for number in numbers])
        else:
            break

for calculation in calculations:
    pass

operators = ['+', '*']
test_numbers = calculations[0]
test_result = test_numbers[0]
test_numbers = test_numbers[1:]
for i in range(1,len(test_numbers)**2+1):
    result = ''
    for j in range(1,len(test_numbers)+1):
        print(i,'%',j,i // j)
        if i // j % i == 0:
            result += operators[0]
        else:
            result += operators[1]
    print(result)

print(5//2)
#4
print(2%8//2)
#0