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


#### TESTS SHOULD ALL BE TRUE ####
print("{0}\n should equal \n{1}\n {2}\n".format(remove_duplicates(['a', 'a', 'x', 'x', 'x', 'g', 't', 't']), [
      'a', 'x', 'g', 't'], remove_duplicates(['a', 'a', 'x', 'x', 'x', 'g', 't', 't']) == ['a', 'x', 'g', 't']))

print("{0}\n should equal \n{1}\n {2}\n".format(remove_duplicates(['c', 'c', 'd', 'd', 'e', 'e', 'f', 'a', 'a']), [
      'c', 'd', 'e', 'f', 'a'], remove_duplicates(['c', 'c', 'd', 'd', 'e', 'e', 'f', 'a', 'a']) == ['c', 'd', 'e', 'f', 'a']))

print("{0}\n should equal \n{1}\n {2}\n".format(remove_duplicates([13, 13, 13, 13, 13, 42]), [
      13, 42], remove_duplicates([13, 13, 13, 13, 13, 42]) == [13, 42]))
