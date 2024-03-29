"""For our first problem, we would like to “rotate” a list, or move elements forward in a list by a number of spaces, k.

Elements at the greatest index will “wrap around” to the beginning of the list."""
# rotate list
# no time/space requirements
# return "rotated" version of input list


def rotate(arr, n):
    n = n%len(arr)
    part1 = arr[-n:]
    part2 = arr[:-n]
    return part1+part2

#*------One Solution---------------- O(N) space create new lists
# def rotate(my_list, num_rotations):
#   places_moved= num_rotations % len(my_list)
#   part_1 = my_list[-places_moved:]
#   part_2 = my_list[:-places_moved]
#   new_list=part_1 + part_2
#   return new_list

#*-------Another Solution-----  O(N) space. Shifting places
# def rotate(my_list, num_rotations):
#   for i in range (num_rotations):
#     my_list.insert(0, my_list.pop())
#   return my_list

#*-----ROTATE BACKWARD CONSTANT SPACE SOLUTION
"""Given a list and a positive integer, return the same list “rotated” a number of times that match the input integer. This time, we’ll rotate the list backward and use O(1) space."""

def rev (rev_list, low, high):
    while low < high:
        rev_list[low], rev_list[high] = rev_list[high], rev_list[low]
        high-= 1
        low += 1
    return rev_list

def rotate(my_list, num_rotations):
    #Reverse first part
    rev(my_list, 0, num_rotations-1)
    
    #Reverse second part
    rev (my_list, num_rotations, len(my_list)-1)
    
    #Reverse All
    rev (my_list, 0, len(my_list)-1)
    
    return my_list



####* first partTESTS SHOULD ALL BE TRUE ####
# print("{0}\n should equal \n{1}\n {2}\n".format(rotate(['a', 'b', 'c', 'd', 'e', 'f'], 1), ['f', 'a', 'b', 'c', 'd', 'e'], rotate(['a', 'b', 'c', 'd', 'e', 'f'], 1) == ['f', 'a', 'b', 'c', 'd', 'e']))

# print("{0}\n should equal \n{1}\n {2}\n".format(rotate(['a', 'b', 'c', 'd', 'e', 'f'], 2), ['e', 'f', 'a', 'b', 'c', 'd'], rotate(['a', 'b', 'c', 'd', 'e', 'f'], 2) == ['e', 'f', 'a', 'b', 'c', 'd']))

# print("{0}\n should equal \n{1}\n {2}\n".format(rotate(['a', 'b', 'c', 'd', 'e', 'f'], 3), ['d', 'e', 'f', 'a', 'b', 'c'], rotate(['a', 'b', 'c', 'd', 'e', 'f'], 3) == ['d', 'e', 'f', 'a', 'b', 'c']))

# print("{0}\n should equal \n{1}\n {2}\n".format(rotate(['a', 'b', 'c', 'd', 'e', 'f'], 4), ['c', 'd', 'e', 'f', 'a', 'b'], rotate(['a', 'b', 'c', 'd', 'e', 'f'], 4) == ['c', 'd', 'e', 'f', 'a', 'b']))

####*Second Part TESTS SHOULD ALL BE TRUE ####
print("{0}\n should equal \n{1}\n {2}\n".format(rotate(['a', 'b', 'c', 'd', 'e', 'f'], 1), ['b', 'c', 'd', 'e', 'f', 'a'], rotate(['a', 'b', 'c', 'd', 'e', 'f'], 1) == ['b', 'c', 'd', 'e', 'f', 'a']))

print("{0}\n should equal \n{1}\n {2}\n".format(rotate(['a', 'b', 'c', 'd', 'e', 'f'], 2), ['c', 'd', 'e', 'f', 'a', 'b'], rotate(['a', 'b', 'c', 'd', 'e', 'f'], 2) == ['c', 'd', 'e', 'f', 'a', 'b']))

print("{0}\n should equal \n{1}\n {2}\n".format(rotate(['a', 'b', 'c', 'd', 'e', 'f'], 3), ['d', 'e', 'f', 'a', 'b', 'c'], rotate(['a', 'b', 'c', 'd', 'e', 'f'], 3) == ['d', 'e', 'f', 'a', 'b', 'c']))

print("{0}\n should equal \n{1}\n {2}\n".format(rotate(['a', 'b', 'c', 'd', 'e', 'f'], 4), ['e', 'f', 'a', 'b', 'c', 'd'], rotate(['a', 'b', 'c', 'd', 'e', 'f'], 4) == ['e', 'f', 'a', 'b', 'c', 'd']))