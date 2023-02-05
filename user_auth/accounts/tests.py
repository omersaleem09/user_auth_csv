from django.test import TestCase

# Create your tests here.



# def pivot(nums:list):
#     left_sum = 0
#     total = sum(nums)
#     for i, v in enumerate(nums):
#         # print(i,v)
#         right_sum = total - left_sum - v
#         print("rightsum",right_sum)
#         if right_sum == left_sum:
#             print("i",i)
#             return i
#         left_sum += v
#         print("leftsum",left_sum)
#     return -1

# print(pivot([1,7,3,6,5,6]))


# list_1 = ['a','b','c','d','d','d','e','a','b','f','g','g','h']

# dup = []

# for i in list_1:
#     if i not in dup:
#         dup.append(i)

# print(dup)


# num = (1,2,3,4,5,6)
# num_1 = list(num)

# sq_num = [i**2 for i in num_1]
# print(sq_num)

# from collections import Counter

# val = "aabbbccde"
# val_1 = sorted(val)
# val_2 = Counter(val_1)


# for k,v in val_2.most_common(3):
#     if v > 1:
#         print(k,v)



arr = [1,1,1,3,3,2,2]

sub_arr = []
for i in range(len(arr)):
    sub_arr.append(arr[i])

print(sub_arr)










