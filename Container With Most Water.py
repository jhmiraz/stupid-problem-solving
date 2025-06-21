def maxArea(height):
    left= 0
    right= len(height)-1
    max_area=0

    while left < right:
        h= min(height[left], height[right])
        w= right-left
        max_area=max(max_area, h*w)

        if left< right:
            left+=1
        else:
            right -= 1

    return max_area


height_array= [1,8,6,2,5,4,8,3,7]
result= maxArea(height_array)
print(result)
