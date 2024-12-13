import numpy as np

with open("Advent_of_Code_2024/12_Day/sample_data.txt", "r") as lists_data:
    data = []
    while True:
        line = lists_data.readline().strip('\n')
        if line:
            data.append([letter for letter in line])
        else:
            break

data_np = np.array(data)
print(data_np.shape)

def check_neighbours(cur_letter, index_row, index_col):
    # check left:
    if index_col - 1 >= 0:
        if data_np[index_row][index_col-1] == cur_letter and data_np[index_row][index_col-1] != '?':
            data_np[index_row, index_col-1] = '?'
            dic[number_of_fields].append([index_row, index_col-1])
            check_neighbours(cur_letter, index_row, index_col-1)

    # check right
    if index_col + 1 <  data_np.shape[1]:
        if data_np[index_row][index_col+1] == cur_letter and data_np[index_row][index_col+1] != '?':
            data_np[index_row, index_col+1] = '?'
            dic[number_of_fields].append([index_row, index_col+1])
            check_neighbours(cur_letter, index_row, index_col+1)

    # check up
    if index_row - 1 >= 0:
        if data_np[index_row - 1][index_col] == cur_letter and data_np[index_row-1][index_col] != '?':
            data_np[index_row - 1, index_col] = '?'
            dic[number_of_fields].append([index_row - 1, index_col])
            check_neighbours(cur_letter, index_row - 1, index_col)

    # down
    if index_row + 1 < data_np.shape[0]:
        if data_np[index_row + 1][index_col] == cur_letter and data_np[index_row+1][index_col] != '?':
            data_np[index_row + 1, index_col] = '?'
            dic[number_of_fields].append([index_row +1, index_col])
            check_neighbours(cur_letter, index_row + 1, index_col)

number_of_fields = 0
dic = {}
# i = row
for i in range(data_np.shape[0]):
    # j = column
    for j in range(data_np.shape[1]):
        cur_letter = data_np[i][j]
        if cur_letter != '?':
            data_np[i][j] = '?'
            number_of_fields += 1
            dic[number_of_fields] = [[i, j]]
            check_neighbours(cur_letter, i, j)

for row in data_np:
    print(row)

for key, value in dic.items():
    print(key, value)