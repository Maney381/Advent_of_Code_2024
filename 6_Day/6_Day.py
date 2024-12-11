with open("data.txt", "r") as file_content:
    data = []
    while True:
        
        line = file_content.readline().strip('\n')
        if line:
            data.append([letter for letter in line])

        else:
            break
num_rows = len(data)
num_cols = len(data[0])

#while True:
# Find the current position of '^'
def find_current_position(data):
    for row_index, row in enumerate(data):
        for col_index, val in enumerate(row):
            if val == '^':
                return row_index, col_index

# moves up
row_index, col_index = find_current_position(data)

def check_end(row_index, col_index):
    if row_index >= num_rows or row_index < 0 or col_index < 0 or col_index >= num_cols:
        return True
    else:
        return False

finish = False
while not finish:
    # moves up
    if not finish:
        while data[row_index][col_index] != '#':
            data[row_index][col_index] = '0' # for visited
            row_index -= 1
            if 0 > row_index:
                finish = True
                break
        row_index += 1

    # moves right
    if not finish:
        while data[row_index][col_index] != '#':
            data[row_index][col_index] = '0' # for visited
            col_index += 1
            if col_index >= num_cols:
                finish = True
                break
        col_index -= 1

    # moves down
    if not finish:
        while data[row_index][col_index] != '#':
            data[row_index][col_index] = '0' # for visited
            row_index += 1
            if row_index >= num_rows:
                finish = True
                break
        row_index -= 1

    # moves left
    if not finish:
        while data[row_index][col_index] != '#' and not finish:
            data[row_index][col_index] = '0' # for visited
            col_index -= 1
            if col_index < 0:
                finish = True
                break
        col_index += 1

count = 0      
for row in data:
    for value in row:
        if value == '0':
            count += 1

print(count)


with open("data.txt", "r") as file_content:
    data = []
    while True:
        
        line = file_content.readline().strip('\n')
        if line:
            data.append([letter for letter in line])

        else:
            break
num_rows = len(data)
num_cols = len(data[0])

# Find the current position of '^'
def find_current_position(data):
    for row_index, row in enumerate(data):
        for col_index, val in enumerate(row):
            if val == '^':
                return row_index, col_index

# moves up

position_start_row, position_start_col = find_current_position(data)

count = 0
for i in range(num_rows):
    for j in range(num_cols):
        if data[i][j] == '.':
            data[i][j] = '#'
            finish = False
            row_index, col_index = position_start_row, position_start_col
            row_col_index_list = []
            while not finish:
                row_col_index_list.append([row_index, col_index])
                # moves up
                if not finish:
                    while data[row_index][col_index] != '#':
                        #data[row_index][col_index] = '0' # for visited
                        row_index -= 1
                        if 0 > row_index:
                            finish = True
                            break
                    row_index += 1

                # moves right
                if not finish:
                    while data[row_index][col_index] != '#':
                        #data[row_index][col_index] = '0' # for visited
                        col_index += 1
                        if col_index >= num_cols:
                            finish = True
                            break
                    col_index -= 1

                # moves down
                if not finish:
                    while data[row_index][col_index] != '#':
                        row_index += 1
                        if row_index >= num_rows:
                            finish = True
                            break
                    row_index -= 1

                # moves left
                if not finish:
                    while data[row_index][col_index] != '#' and not finish:
                        col_index -= 1
                        if col_index < 0:
                            finish = True
                            break
                    col_index += 1
                if not finish and [row_index, col_index] in row_col_index_list:
                    count+=1
                    break

            data[i][j] = '.'
            

print(count)
