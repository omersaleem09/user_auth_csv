from django.test import TestCase

# Create your tests here.



def pivot(nums:list):
    left_sum = 0
    total = sum(nums)
    for i, v in enumerate(nums):
        # print(i,v)
        right_sum = total - left_sum - v
        print("rightsum",right_sum)
        if right_sum == left_sum:
            print("i",i)
            return i
        left_sum += v
        print("leftsum",left_sum)
    return -1

print(pivot([1,7,3,6,5,6]))
