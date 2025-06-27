def find_missing_number(nums):
    n = len(nums)+1
    expected_sum= n* (n+1) //2
    acttual_sum= sum(nums)

    return expected_sum - acttual_sum

a=[1,2,4,5,7,6,8,9]
print(find_missing_number(a))