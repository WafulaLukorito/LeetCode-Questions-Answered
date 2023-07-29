
# *Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

# ?Time Complexity = O(N) ---- Single loop over container
# ? Space Complexity = O(1) ---- No external data structures are used

# *-----2 months later----------

# def container_most_water(arr):
#     max_area = 0
#     left = 0
#     right = len(arr) - 1

#     while (left < right):
#         curr_area = (min(arr[left], arr[right])) * (right - left)
#         max_area = max(max_area, curr_area)
#         if (arr[left]< arr[right]):
#             left+=1
#         else:
#             right -=1
#     return max_area


# #*----- Attempt 2--------------------------------

# def container_most_water(height):
#     left = 0
#     right = len(height) - 1
#     max_area = 0

#     while (left < right):
#         curr_area = (min(height[left], height[right]) * (right - left))
#         max_area = max(max_area, curr_area)

#         if (height[left] < height[right]):
#             left += 1
#         else:
#             right -= 1
#     return max_area


# #* Whiteboarding solution

def container_most_water(heights):
    left = 0
    right = len(heights) - 1
    max_area = 0

    while (left < right):
        current_area = (min(heights[left], heights[right]) * (right - left))
        max_area = (max(max_area, current_area))

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return max_area


height = [4, 3, 2, 1, 4]
height2 = [1, 8, 6, 2, 5, 4, 8, 3, 7]

result = container_most_water(height)
result2 = container_most_water(height2)

print(f"Area with most water among {height} is {result} square units big.\n")
print(f"Area with most water among {height2} is {result2} square units big.\n")
