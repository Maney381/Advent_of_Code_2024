from functools import cache


with open("data.txt", "r") as lists_data:
    data = []
    while True:
        line = lists_data.readline()#
        if line:
            data.append([int(num) for num in line.split(' ')])
        else:
            break

data = data[0]
print(data)

@cache
def rules(num):
    str_num = str(num)
    n = len(str_num)
    if num == 0:
        return [1]
    elif n % 2 == 0:
        left_num = str_num[0:int(n/2)]
        right_num = str_num[int(n/2):n]
        return [int(left_num), int(right_num)]
    else:
        return [num * 2024]

#rule_dic = {}

for j in range(75):
    print(j)
    new_data = []
    for i in range(len(data)):
        cur_num = data[i]
        #if cur_num in rule_dic:
        #    new_nums = rule_dic[cur_num]
        #else:
        new_nums = rules(cur_num)
        #rule_dic[cur_num] = new_nums
        
        for new_num in new_nums:
            new_data.append(new_num)
    data = new_data

print(len(data))