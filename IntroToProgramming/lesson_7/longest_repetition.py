# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a 
# list, and returns the element in the list that has the most 
# consecutive repetitions. If there are multiple elements that 
# have the same number of longest repetitions, the result should 
# be the one that appears first. If the input list is empty, 
# it should return None.

def longest_repetition(items):
    if items:
        longest_val = None
        longest_cnt = None
        curr_item = items[0]
        count = 1
        
        
        if len(items) == 1:
            longest_val = items[0]
        else:
            for i in range(1, len(items)):
                if items[i] == curr_item:
                    count = count + 1
                    if i == len(items) - 1:
                        if longest_val == None:
                            longest_val = curr_item
                            longest_cnt = count
                        elif longest_cnt < count:
                            longest_val = curr_item
                            longest_cnt = count
                elif items[i] != curr_item:
                    if longest_val == None:
                        longest_val = curr_item
                        longest_cnt = count
                    elif longest_cnt < count:
                        longest_val = curr_item
                        longest_cnt = count
                    count = 1
                    curr_item = items[i]
        
        return longest_val
    else:
        return None



#For example,

print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
# 3

print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
# b

print longest_repetition([1,2,3,4,5])
# 1

print longest_repetition([])
# None

print longest_repetition([[1], [2, 2], [2, 2], [2, 2], [3, 3, 3]])

print longest_repetition([2, 2, 3, 3, 3])

print longest_repetition([2])


