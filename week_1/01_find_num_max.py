
#Find the max value in the list
#리스트 최대값 찾기

input = [3, 5, 6, 1, 2, 4]

def find_max_num(array):
    num_max = array[0]
    for num in array:
        if num > num_max:
            num_max  = num
    return num_max


# def find_max_num(array):
#     for num in array:
#         for compare_num in array:
#             if num < compare_num:
#                 break
#         else:
#                 return num

result = find_max_num(input)
print(result)





