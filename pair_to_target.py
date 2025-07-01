def find_sum_pair_target(nums,target):

    seen=set()
    pairs=[]


    for i in nums:
        complement= target-i
        if complement in seen:
            pairs.append((complement,i))

        seen.add(i)
    return pairs

nums=[1,2,3,4,5]
target=6
print(find_sum_pair_target(nums,target))
