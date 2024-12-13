with open("data.txt", "r") as lists_data:
    ordering = []
    while True:
        line = lists_data.readline().strip('\n')
        if line:
            ordering.append(line)
        else:
            break
    page_numbers = []
    while True:
        line = lists_data.readline().strip('\n')
        if line:
            page_numbers.append([int(x) for x in line.split(',')])
        else:
            break


    first_second_dic = dict()

    for order in ordering:
        first, second = order.split('|')
        if int(first) not in first_second_dic:
            first_second_dic[int(first)] = [int(second)]
        else:
            first_second_dic[int(first)].append(int(second))
    

    count = 0
    for page in page_numbers:
        correct_order = True

        for first in range(len(page)-1):
            for second in range(first +1, len(page)):
                if page[second] in first_second_dic:
                    if page[first] in first_second_dic.get(page[second]):
                        correct_order = False
                        break
            if correct_order == False:
                break
        if correct_order:
            print('p')
            count += page[int(len(page)/2)]
    
    print(count)

    ## Part 2
print('Part 2:')


with open("data.txt", "r") as lists_data:
    ordering = []
    while True:
        line = lists_data.readline().strip('\n')
        if line:
            ordering.append(line)
        else:
            break
    page_numbers = []
    while True:
        line = lists_data.readline().strip('\n')
        if line:
            page_numbers.append([int(x) for x in line.split(',')])
        else:
            break


    first_second_dic = dict()

    for order in ordering:
        first, second = order.split('|')
        if int(first) not in first_second_dic:
            first_second_dic[int(first)] = [int(second)]
        else:
            first_second_dic[int(first)].append(int(second))
    

    count = 0
    for page in page_numbers:
        correct_order = True
        
        for first in range(len(page)-1):
            for second in range(first +1, len(page)):
                if page[second] in first_second_dic:
                    if page[first] in first_second_dic.get(page[second]):
                        correct_order = False
                        break
            if correct_order == False:
                break
        if correct_order == False:
            while not correct_order:
                count_wrong = 0
                for first in range(len(page)-1):
                    for second in range(first +1, len(page)):
                        if page[second] in first_second_dic:
                            if page[first] in first_second_dic.get(page[second]):
                                count_wrong += 1
                                old_num = page[first]
                                page[first] = page[second]
                                page[second] = old_num
                if count_wrong == 0:
                    correct_order = True

            count += page[int(len(page)/2)]
    
    print(count)

