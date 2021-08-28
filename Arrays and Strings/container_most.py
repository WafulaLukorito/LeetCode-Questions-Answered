



def container_most(height):
    left = 0
    right = len(height) -1 
    max_area = 0
    
    while (left < right):
        current_area = min (height[left], height[right]) * (right - left)
        max_area = max (max_area, current_area)

        if (height[left] < height[right]):
            left +=1
        else:
            right -=1
    
    return max_area




height = [1,8,6,2,5,4,8,3,7] #49

result = container_most(height)

print (f"From the heights {height}, the maximum container is {result} square units.")