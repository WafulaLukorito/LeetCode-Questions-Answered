
"""
#! Disadvantages of Linked Lists over arrays

#* Contains O(n) searching in all cases, even when sortd, unlike arrays which can have O(log n) binary search. 

#! Advantage.

#*Insertions and deletions are cheaper as we do not shift other elements during deletions and insertions. 

"""

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def printList(self):
#         temp = self.head
#         linked_list =""

#         while (temp):
#             linked_list+= str(temp.data) + " => "
#             temp = temp.next

#         print (linked_list)

#     def insertNode(self, value_to_insert, pos):
#         target = Node(value_to_insert)
#         if (pos ==0):
#             target.next = self.head
#             self.head = target
#             return
#         def getPrev(pos):
#             temp = self.head
#             count = 1
#             while (count < pos):
#                 temp = temp.next
#                 count += 1
#             return temp

#         prev = getPrev(pos)
#         nextNode = prev.next

#         prev.next = target
#         target.next = nextNode

#     def deleteNode(self, value_to_delete):
#         temp = self.head
#         if (temp is None):
#             return
#         if (temp.data == value_to_delete):
#             self.head = temp.next
#             temp = None
#             return
        
#         while(temp.next.data != value_to_delete):
#             temp = temp.next
#         target_node = temp.next
#         temp.next = target_node.next
#         target_node.next = None



# #Node structure: 5 => 1 => 3 => 7

# linked_list = LinkedList()
# linked_list.head = Node(5)

# second_node = Node(1)
# third_node = Node(3)
# tail_node = Node(7)

# linked_list.head.next = second_node
# second_node.next = third_node
# third_node.next = tail_node

# linked_list.insertNode(599,2)

# linked_list.deleteNode(1)

# LinkedList.printList(linked_list)


#*------------SECOND ATTEMPT------------
# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next_node = next

# class LinkedList:
#     def __init__(self, head_node=None):
#         self.head_node = head_node
    
#     def add_node(self, value, pos):
#         new_node = Node(value)
#         if (pos == 0):
#             new_node.next_node = self.head_node
#             self.head_node = new_node
#             return
#         else:
#             current = self.head_node
#             count = 1
#             while count < pos:
#                 current = current.next_node
#                 count += 1
#             prev_node = current
#             new_node.next_node = prev_node.next_node
#             prev_node.next_node = new_node

#     def delete_node(self, value):
#         if self.head_node.value == value:
#             self.head_node = self.head_node.next_node
#         else:
#             current = self.head_node
#             while (current.next_node.value != value):
#                 current = current.next_node
#             remove = current.next_node
#             current.next_node = remove.next_node
#             remove.next_node = None

#     def stringify(self):
#         current = self.head_node
#         my_str = ""
#         while current:
#             my_str += str(current.value) + " => "
#             current = current.next_node
#         print (my_str, "our head is :", self.head_node.value)


#*--------WHITEBOARD ATTEMPT------
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def Stringify(self):
        my_str = ""
        current = self.head

        while(current):
            my_str += str(current.value) + " => "
            current = current.next
        print(my_str, "head is:", self.head.value)


    def add_node(self, value, pos):
        new_node = Node(value)
        if (pos == 0):
            new_node.next = self.head
            self.head = new_node

        else:
            count = 1
            current = self.head
            while (count < pos):
                current = current.next
                count += 1

            new_node.next = current.next
            current.next = new_node


    def delete_node(self, value):
        if self.head.value == value:
            self.head = self.head.next
        else:

            current = self.head
            while(current.next.value != value):
                current = current.next

            remove = current.next
            current.next = remove.next
            remove.next = None






tail_node = Node(1000)
fourth_node = Node(500, tail_node)
third_node = Node(100, fourth_node)
second_node = Node(20, third_node)
first_node = Node(5, second_node)


llist = LinkedList(first_node)

llist.add_node(666,0)
llist.add_node(999,3)

llist.delete_node(666)
llist.delete_node(1000)
llist.delete_node(5)
llist.add_node("akili", 3)

llist.Stringify()