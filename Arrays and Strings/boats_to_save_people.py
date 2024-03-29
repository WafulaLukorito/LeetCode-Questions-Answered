
# * You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

# *Return the minimum number of boats to carry every given person.

# ? Time Complexity = O(N log N).... Sorting input array O(N log N), Looping over sorted array O(N)

# ? Space Complexity = O(N) .... People.sort() internally uses an algorithm that has O(N) space complexity


# * Attempt  2

# def boats_to_save_people(people, limit):
#     left = 0
#     boats = 0
#     right = len(people) - 1
#     while left <= right:
#         if left == right:
#             break
#         if people[left] + people[right] > limit:
#             boats += 1
#             right -= 1
#         else:
#             boats += 1
#             right

# def boats_to_save_people (people, limit):
#     left = 0
#     boats = 0
#     right = len(people)-1
#     while left <= right:
#         if left ==right:
#             boats += 1
#             break
#         if people[left] + people[right] > limit:
#             boats +=1
#             right -= 1
#         else:
#             boats+=1
#             right = -1
#             left += 1
#     return boats


# #*-------Whiteboarding-------
# def boats_to_save_people(people, limit):
#     left = 0
#     right = len(people) - 1
#     boats = 0

#     while (left <= right):
#         if left == right:
#             boats += 1
#             break
#         if people[left] + people[right] < limit:
#             left +=1
#         boats += 1
#         right -= 1
#     return boats

# people = [3,5,3,4]
# limit = 5

# result = boats_to_save_people(people, limit)
# print (f"The minimum number of boats to carry people {people} is {result}")

# def boats_to_save_people (people, limit):
#     people.sort()
#     left = 0
#     right = len(people) -1
#     boats = 0

#     while (left <= right):
#         if (left == right):
#             boats += 1
#             break

#         if (people[left] + people[right] <= limit):
#             left += 1
#             right -=1
#             boats+=1
#         else:
#             right -=1
#             boats+=1

#     return boats


# people = [3,5,3,4]
# limit = 5

# result = boats_to_save_people(people, limit)
# print (result)

# * Attempt 2

# def boats_to_save_people(people, limit):
#     people.sort()
#     left = 0
#     right = len(people) -1
#     boats = 0

#     while (left <= right):
#         if (left == right):
#             boats += 1
#             break

#         elif (people[left] + people[right] <= limit):
#             left += 1
#             right -1
#             boats+=1
#         else:
#             right -=1
#             boats+=1
#     return boats


# people = [3,5,3,4]
# limit = 5

# result = boats_to_save_people(people, limit)

# print (f"The minimum number of boats to carry people {people} is {result}")

# *Whiteboarding solution

# def boats_to_save_people(people,limit):
#     people.sort()
#     boats = 0
#     left = 0
#     right = len(people) - 1

#     while (left <= right):
#         if (left == right):
#             boats +=1
#             break

#         elif (people[left] + people [right] <= limit):
#             left +=1
#             right -= 1
#             boats +=1
#         else:
#             right -=1
#             boats +=1
#     return boats


# people = [3,5,3,4]
# limit = 5

# result = boats_to_save_people(people, limit)

# print (f"The number of boats required to save {people} people is {result}")


def boats_to_save_people(people, limit):
    people.sort()
    boats =0
    left=0
    right = len(people)-1
    
    while left <= right:
        if left == right:
            boats+=1
            return boats
        else:
            if people[left]+people[right] > limit:
                boats+=1
                right-=1
            else:
                boats+=1
                left+=1
                right-=1
    
    return boats


people = [3, 5, 3, 4]
limit = 5

result = boats_to_save_people(people, limit)
print(f"The minimum number of boats to save {people} people is {result}")
