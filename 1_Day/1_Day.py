import numpy as np
from collections import Counter

test_l1 = [3, 4, 2, 1, 3, 3]
test_l2 = [4, 3, 5, 3, 9, 3]

with open("data.txt", "r") as lists_data:
    l1 = []
    l2 = []
    for line in lists_data: 
        val1, val2 = line.split() 
        l1.append(int(val1))
        l2.append(int(val2))

def sum_of_distances_list(l1: list, l2:list) -> int:
    l1.sort()
    l2.sort()
    return sum(abs(np.array(l2) - np.array(l1)))

test_answer_1 = sum_of_distances_list(test_l1, test_l2)
print('Test question 2: {}'.format(test_answer_1))

answer_1 = sum_of_distances_list(l1, l2)
print('Answer question 1: {}'.format(answer_1))
# 1580061

# figure out exactly how often each number from the left list appears in the right list
def number_of_times_item_in_left_list_in_right_list(left_list: list, right_list: list) -> int:
    set_left_list = set(left_list)
    counter_left_list = Counter(left_list)
    counter_right_list = Counter(right_list)
    set_right_list = set(right_list)
    common_numbers = set_left_list & set_right_list
    return sum([number * (occurence * counter_left_list[number]) for number, occurence in counter_right_list.items() if number in common_numbers])

test_answer_2 = number_of_times_item_in_left_list_in_right_list(test_l1, test_l2)
print('Test question 2: {}'.format(test_answer_2))

answer_2 = number_of_times_item_in_left_list_in_right_list(l1, l2)
print('Answer question 2: {}'.format(answer_2))
# 23046913