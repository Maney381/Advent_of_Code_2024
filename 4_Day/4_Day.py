with open("data.txt", "r") as lists_data:
    data = []
    while True:
        line = lists_data.readline().strip('\n')
        if line:
            data.append(line)
        else:
            break
    
    num_cols = len(data[0])
    num_rows = len(data)
    count = 0
    # Check in row
    for col_index in range(num_cols):
        for row_index in range(num_rows):
            if data[col_index][row_index] == 'X':
                # to the right
                if (row_index + 3 < num_rows):
                    if (data[col_index][row_index+1] == 'M') & (data[col_index][row_index+2] == 'A') & (data[col_index][row_index+3] == 'S'):
                        count +=1
                        #print(col_index, row_index)
                        #print('right')
                # to the left
                if (row_index > 2):
                    if (data[col_index][row_index-1] == 'M') & (data[col_index][row_index-2] == 'A') & (data[col_index][row_index-3] == 'S'):
                        count +=1
                        #print(col_index, row_index)
                        #print('left')

                # up
                if (col_index > 2):
                    if (data[col_index-1][row_index] == 'M') & (data[col_index-2][row_index] == 'A') & (data[col_index-3][row_index] == 'S'):
                        count +=1
                        #print(col_index, row_index)
                        #print('up')
                # down
                if (col_index + 3< num_cols):
                    if (data[col_index+1][row_index] == 'M') & (data[col_index+2][row_index] == 'A') & (data[col_index+3][row_index] == 'S'):
                        count +=1
                        #print(col_index, row_index)
                        #print('down')
                # down right
                if (col_index + 3 < num_cols) & (row_index + 3 < num_rows):
                    if (data[col_index+1][row_index+1] == 'M') & (data[col_index+2][row_index+2] == 'A') & (data[col_index+3][row_index+3] == 'S'):
                        count +=1
                        #print(col_index, row_index)
                        #print('down-right')
                # down left
                if (col_index + 3 < num_cols) & (row_index > 2):
                    if (data[col_index+1][row_index-1] == 'M') & (data[col_index+2][row_index-2] == 'A') & (data[col_index+3][row_index-3] == 'S'):
                        count +=1
                        #print(col_index, row_index)
                        #print('down-left')
                # up right
                if (col_index > 2) & (row_index + 3 < num_rows):
                    if (data[col_index-1][row_index+1] == 'M') & (data[col_index-2][row_index+2] == 'A') & (data[col_index-3][row_index+3] == 'S'):
                        count +=1
                        #print(col_index, row_index)
                        #print('up-right')
                # up left
                if (col_index > 2) & (row_index > 2):
                    if (data[col_index-1][row_index-1] == 'M') & (data[col_index-2][row_index-2] == 'A') & (data[col_index-3][row_index-3] == 'S'):
                        count +=1
                        #print(col_index, row_index) 
                        #print('up-left')


    print(count)

with open("data.txt", "r") as lists_data:
    data = []
    while True:
        line = lists_data.readline().strip('\n')
        if line:
            data.append(line)
        else:
            break
    
    num_cols = len(data[0])
    num_rows = len(data)
    count = 0
    # Check in row
    for col_index in range(1,num_cols-1):
        for row_index in range(1,num_rows-1):
            if data[col_index][row_index] == 'A':
                up_down = False
                down_up = False
                # MAS (up -> down)
                if (data[col_index -1][row_index-1] == 'M') & (data[col_index+1][row_index+1] == 'S'):
                    up_down = True

                # SAM (up -> down)
                if (data[col_index-1][row_index-1] == 'S') & (data[col_index+1][row_index+1] == 'M'):
                    up_down = True

                # MAS (down -> up)
                if (data[col_index-1][row_index+1] == 'M') & (data[col_index+1][row_index-1] == 'S'):
                    down_up = True

                # SAM (down -> up)
                if (data[col_index-1][row_index+1] == 'S') & (data[col_index+1][row_index-1] == 'M'):
                    down_up = True

                if up_down & down_up:
                    count += 1


    print(count)