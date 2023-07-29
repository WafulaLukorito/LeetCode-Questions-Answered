# * Codecademy
"""Write a function remove_duplicates() which has one parameter: dupe_list.

remove_duplicates() should return a list containing unique values in the same order as in dupe_list.
    """

# remove duplicates
# no time/space requirements
# return a list with duplicates removed

# * O(N) time and O(N) space complexity.
# def remove_duplicates(dupe_list):
#   unique = []
#   for num in dupe_list:
#     if num not in unique:
#       unique.append(num)
#   return (unique)


# def remove_duplicates(dupe_list):  #!In the same order!!Set is not ordered
#     return list(set(dupe_list))

def remove_duplicates(dupe_list):
    new_list = []
    for i in dupe_list:
        if i not in new_list:
            new_list.append(i)
    return new_list

def remove_duplicates(dupe_list):
    my_set= set(dupe_list)
    return list(my_set)

def remove_duplicates(dupe_list):
    return list(dict.fromkeys(dupe_list))

dupe_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
print(remove_duplicates(dupe_list))  # prints: [1, 2, 3, 4, 5, 6, 7]
"""
In this code, dict.fromkeys(dupe_list) creates a new dictionary where the keys are the elements of dupe_list, and the values are all set to None. Since dictionary keys must be unique, this has the effect of removing duplicates. Also, since dictionaries maintain insertion order as of Python 3.7, the order of the elements is preserved. Finally, list() is used to convert the keys of the dictionary back into a list.

The time complexity of this approach is O(n), where n is the number of elements in dupe_list. This is because each operation we're performing -- converting the list to a dictionary, and then converting the keys of the dictionary back to a list -- takes linear time. The space complexity is also O(n), as in the worst case we may need to store all n elements of dupe_list in the new list and dictionary.
"""

#### TESTS SHOULD ALL BE TRUE ####
print("{0}\n should equal \n{1}\n {2}\n".format(remove_duplicates(['a', 'a', 'x', 'x', 'x', 'g', 't', 't']), [
      'a', 'x', 'g', 't'], remove_duplicates(['a', 'a', 'x', 'x', 'x', 'g', 't', 't']) == ['a', 'x', 'g', 't']))

print("{0}\n should equal \n{1}\n {2}\n".format(remove_duplicates(['c', 'c', 'd', 'd', 'e', 'e', 'f', 'a', 'a']), [
      'c', 'd', 'e', 'f', 'a'], remove_duplicates(['c', 'c', 'd', 'd', 'e', 'e', 'f', 'a', 'a']) == ['c', 'd', 'e', 'f', 'a']))

print("{0}\n should equal \n{1}\n {2}\n".format(remove_duplicates([13, 13, 13, 13, 13, 42]), [
      13, 42], remove_duplicates([13, 13, 13, 13, 13, 42]) == [13, 42]))
