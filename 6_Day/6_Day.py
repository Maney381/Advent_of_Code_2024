'''with open("data.txt", "r") as file_content:
    data = []
    while True:
        
        line = file_content.readline().strip('\n')
        if line:
            data.append([letter for letter in line])

        else:
            break
print(data)
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
            print(row_index, finish)
            if 0 > row_index:
                finish = True
                break
        row_index += 1

    # moves right
    if not finish:
        while data[row_index][col_index] != '#':
            data[row_index][col_index] = '0' # for visited
            col_index += 1
            print(col_index, finish)
            if col_index >= num_cols:
                finish = True
                break
        col_index -= 1

    # moves down
    if not finish:
        while data[row_index][col_index] != '#':
            data[row_index][col_index] = '0' # for visited
            row_index += 1
            print(row_index, finish)
            if row_index >= num_rows:
                finish = True
                break
        row_index -= 1

    # moves left
    if not finish:
        while data[row_index][col_index] != '#' and not finish:
            data[row_index][col_index] = '0' # for visited
            col_index -= 1
            print(col_index, finish)
            if col_index < 0:
                finish = True
                break
        col_index += 1

count = 0      
for row in data:
    for value in row:
        print(value)
        if value == '0':
            count += 1

print(count)

'''
with open("sample_data.txt", "r") as file_content:
    data = []
    while True:
        
        line = file_content.readline().strip('\n')
        if line:
            data.append([letter for letter in line])

        else:
            break
print(data)
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
            print(i, j)

            data[i][j] = '#'
            finish = False
            row_index, col_index = position_start_row, position_start_col
            while not finish:
                begin_row_index = row_index
                begin_col_index = col_index
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
                        #data[row_index][col_index] = '0' # for visited
                        row_index += 1
                        if row_index >= num_rows:
                            finish = True
                            break
                    row_index -= 1

                # moves left
                if not finish:
                    while data[row_index][col_index] != '#' and not finish:
                        #data[row_index][col_index] = '0' # for visited
                        col_index -= 1
                        if col_index < 0:
                            finish = True
                            break
                    col_index += 1
                
                if row_index == begin_row_index and col_index == begin_col_index:
                    count+=1
                    break
            for row in data:
                print(row)
            data[i][j] = '.'


print(count)
