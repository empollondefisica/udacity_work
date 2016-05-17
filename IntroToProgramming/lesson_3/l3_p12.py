def numbers_in_lists(string):
    compare_num = -1
    sup_list = []
    sub_list = []
    in_sub = False
    for index in range(0, len(string)):
        num = int(string[index])
        
        if not sup_list:        
            sup_list.append(num)
            compare_num = num
        elif num <= compare_num:
            sub_list.append(num)
            if index == len(string) - 1:
                sup_list.append(sub_list)
                sub_list = []
        elif num > compare_num:
            compare_num = num
            if sub_list:
                sup_list.append(sub_list)
                sub_list = []
            sup_list.append(num)
    
    
    print sup_list
    return sup_list



#testcases
string = '543987'
result = [5,[4,3],9,[8,7]]
print repr(string), numbers_in_lists(string) == result
string= '987654321'
result = [9,[8,7,6,5,4,3,2,1]]
print repr(string), numbers_in_lists(string) == result
string = '455532123266'
result = [4, 5, [5, 5, 3, 2, 1, 2, 3, 2], 6, [6]]
print repr(string), numbers_in_lists(string) == result
string = '123456789'
result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print repr(string), numbers_in_lists(string) == result

