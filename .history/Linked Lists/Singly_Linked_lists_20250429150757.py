
"""
#! Disadvantages of Linked Lists over arrays

#* Contains O(n) searching in all cases, even when sortd, unlike arrays which can have O(log n) binary search. 

#! Advantage.

#*Insertions and deletions are cheaper as we do not shift other elements during deletions and insertions. 

"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def __str__(self):
        return (str(self.data))

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __str__(self):
        if not self.head:
            return "Empty List"
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return " => ".join(nodes)
    
    def getSize(self):
        if not self.head:
            return 0
        size = 1
        current_node = self.head
        while current_node.next:
            size += 1
            current_node = current_node.next
        return size
    
    def __len__(self):
        return self.getSize()
    
    def addToHead(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
    
    def insert(self, value, pos):
        if (pos <= 0 or pos > len (self) + 1):
            raise IndexError("Invalid position!")
            return
        if (pos== len(self)+1):
            self.addToTail(value)
            return
        if (pos == 1):
            self.addToHead(value)
            return
        
        new_node = Node(value)
        current = self.head
        for _ in range(pos - 2):  # Stop at the node before insertion
            current = current.next
        new_node.next = current.next
        current.next = new_node
    
    def addToTail(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node
    
    def deleteFromHead(self):
        if not self.head:
            raise IndexError("List Empty!")
        if not self.head.next:
            self.head = self.tail = None
            return
        temp = self.head
        self.head = self.head.next
        temp.next = None  # Clean up reference

    def deleteFromTail(self):
        if not self.head:
            raise IndexError("List Empty!")
        if not self.head.next:
            self.head = self.tail = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None
        self.tail = current

    def delete(self, value):
        if not self.head:
            raise IndexError("List Empty!")
        if self.head.data == value:
            self.deleteFromHead()
            return
        current = self.head
        while current.next and current.next.data != value:
            current = current.next
        if not current.next:
            raise ValueError(f"{value} not in list!")
        to_delete = current.next
        current.next = to_delete.next
        to_delete.next = None
        if not current.next:
            self.tail = current



















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


# *------------SECOND ATTEMPT------------
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
#         print(my_str, "our head is :", self.head_node.value)


# # *--------WHITEBOARD ATTEMPT------
# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next


# class LinkedList:
#     def __init__(self, head=None):
#         self.head = head

#     def add_node(self, value, pos=0):
#         new_node = Node(value)
#         if pos == 0:
#             new_node.next = self.head
#             self.head = new_node
#         else:
#             counter = 1
#             current = self.head
#             while (counter < pos):
#                 current = current.next
#                 counter += 1
#             new_node.next = current.next
#             current.next = new_node

#     def delete_node(self, value):
#         if self.head.value == value:
#             temp = self.head.next
#             self.head.next = None
#             self.head = temp
#         else:
#             current = self.head
#             while (current.next.value != value):
#                 current = current.next
#             remove = current.next
#             current.next = remove.next
#             remove.next = None

#     def stringify(self):
#         my_str = ""
#         current = self.head
#         while (current):
#             my_str += str(current.value) + " => "
#             current = current.next
#         print(my_str, "the head node is: ", str(self.head.value))


# tail_node = Node(1000)
# fourth_node = Node(500, tail_node)
# third_node = Node(100, fourth_node)
# second_node = Node(20, third_node)
# first_node = Node(5, second_node)


# llist = LinkedList(first_node)

# llist.add_node(666, 0)
# llist.add_node(999, 3)

# llist.delete_node(666)
# llist.delete_node(1000)
# llist.delete_node(5)
# llist.add_node("akili", 3)

# llist.stringify()


# # * -----------Longer Implementation---------
# # Singly linked List

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

#     def get_value(self):
#         return self.value

#     def get_next(self):
#         return self.next

#     def set_next(self, new_next):
#         self.next = new_next

#     def __str__(self):
#         return str(self.value)


# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def add_to_head(self, value):
#         new_node = Node(value)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.set_next(self.head)
#             self.head = new_node

#     def add_to_tail(self, value):
#         new_node = Node(value)
#         if self.tail is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.set_next(new_node)
#             self.tail = new_node

#     def remove_head(self):
#         if self.head is None:
#             return None
#         else:
#             value = self.head.get_value()
#             self.head = self.head.get_next()
#             return value

#     def remove_tail(self):
#         if self.head is None:
#             return None
#         else:
#             current = self.head
#             while current.get_next() != self.tail:
#                 current = current.get_next()
#             value = self.tail.get_value()
#             current.set_next(None)
#             self.tail = current
#             return value

#     def contains(self, value):
#         if self.head is None:
#             return False
#         else:
#             current = self.head
#             while current is not None:
#                 if current.get_value() == value:
#                     return True
#                 current = current.get_next()
#             return False

#     def get_max(self):
#         if self.head is None:
#             return None
#         else:
#             current = self.head
#             max = self.head.get_value()
#             while current is not None:
#                 if current.get_value() > max:
#                     max = current.get_value()
#                 current = current.get_next()
#             return max

#     def get_min(self):
#         if self.head is None:
#             return None
#         else:
#             current = self.head
#             min = self.head.get_value()
#             while current is not None:
#                 if current.get_value() < min:
#                     min = current.get_value()
#                 current = current.get_next()
#             return min

#     def get_size(self):
#         if self.head is None:
#             return 0
#         else:
#             current = self.head
#             count = 0
#             while current is not None:
#                 count += 1
#                 current = current.get_next()
#             return count

#     def __str__(self):
#         if self.head is None:
#             return ''
#         else:
#             current = self.head
#             string = ''
#             while current is not None:
#                 string += str(current.get_value()) + ' '
#                 current = current.get_next()
#             return string

#     def __len__(self):
#         return self.get_size()

#     def __getitem__(self, index):
#         if self.head is None:
#             return None
#         else:
#             current = self.head
#             count = 0
#             while current is not None:
#                 if count == index:
#                     return current.get_value()
#                 current = current.get_next()
#                 count += 1
#             return None

#     def __setitem__(self, index, value):
#         if self.head is None:
#             return None
#         else:
#             current = self.head
#             count = 0
#             while current is not None:
#                 if count == index:
#                     current.set_value(value)
#                     return
#                 current = current.get_next()
#                 count += 1
#             return None

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
        
#     def __str__(self):
#         return str(self.data)


# class LinkedList:
#     def __init__(self):
#         self.head = None
        
#     def get_size(self):
#         if not self.head:
#             return 0
#         current = self.head
#         count = 1
#         while current.next:
#             count +=1
#             current = current.next
#         return count
    
#     def insert_node (self, value_to_insert, pos=None):
#        size = self.get_size
#        if (pos is not None) and ((pos>size) or (pos < o)):
#            print ("Position out of bounds")
#            return

#        elif (pos==0):
#            target = Node(value_to_insert)
#            if self.head is None:
#                self.head = target
#                return
#            else:
#                target.next = self.head
#                self.head = target
#                return
#        else:
#            target = Node(value_to_insert)
#            current = self.head
#            count = 1
#            while count < pos:
#                current = current.next
#                count +=1
#             new_next = current.next
#             current.next = target
#             target.next = new_next
#             class Node:
#                 def __init__(self, data):
#                     self.data = data
#                     self.next = None

#                 def __str__(self):
#                     return str(self.data)


#             class LinkedList:
#                 def __init__(self):
#                     self.head = None

#                 def insert_node(self, value_to_insert, pos=None):
#                     size = self.get_size()
#                     if (pos is not None) and ((pos > size) or (pos < 0)):
#                         print("Out of bounds!")
#                         return
#                     target = Node(value_to_insert)
#                     if pos is None:
#                         current = self.head
#                         if current is None:
#                             self.head = target
#                             return

#                 def delete_node(self, value_to_delete):
#                     if self.head.data == value_to_delete:
#                         self.head = self.head.next
#                         return
#                     current = self.head
#                     while current.next:
#                         if current.next.data == value_to_delete:
#                             to_delete = current.next
#                             current.next = current.next.next
#                             to_delete.next = None
#                             return
#                     return "Value not found"
                        
                    
                    
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

#     def __str__(self):
#         return str(self.data)


# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def insert_node(self, value_to_insert, pos=None):
#         size = self.get_size()
#         if (pos is not None) and ((pos > size) or (pos < 0)):
#             print("Out of bounds!")
#             return
#         target = Node(value_to_insert)
#         if pos is None:
#             current = self.head
#             if current is None:
#                 self.head = target
#                 return
#             else:
#                 while (current.next is not None):
#                     current = current.next
#                 current.next = target
#                 return

#         elif (pos == 0):
#             target.next = self.head
#             self.head = target
#             return
#         else:
#             count = 1
#             temp = self.head
#             while (count < pos):
#                 temp = temp.next
#                 count += 1
#             new_next = temp.next
#             temp.next = target
#             target.next = new_next
#             return

#     def delete_node(self, value_to_delete):
#         if (self.head.data == value_to_delete):
#             current = self.head
#             self.head = self.head.next
#             current.next = None
#             return
#         else:
#             current = self.head
#             while (current.next.data != value_to_delete):
#                 current = current.next
#                 if current.next == None:
#                     print("Value does not exist!")
#                     return
#             to_delete = current.next
#             new_next = to_delete.next
#             current.next = new_next
#             to_delete.next = None

#     def get_size(self):
#         if self.head == None:
#             return 0
#         counter = 0
#         current = self.head
#         while current:
#             counter += 1
#             current = current.next
#         return counter

#     def find_max(self):
#         if not self.head:
#             return -1
#         current = self.head
#         my_max = self.head.data
#         while current:
#             my_max = max(my_max, current.data)
#             current = current.next
#         return my_max

#     def find_min(self):
#         if not self.head:
#             return -1
#         current = self.head
#         my_min = self.head.data
#         while current:
#             my_min = min(my_min, current.data)
#             current = current.next
#         return my_min

#     def __str__(self) -> str:
#         my_str = ""
#         current = self.head
#         while current:
#             if not current.next:
#                 my_str += str(current.data)
#             else:
#                 my_str += str(current.data)+" => "
#             current = current.next
#         return f"{my_str} \n its size is {self.get_size()} \n The head is {self.head} \n The max value is {self.find_max()} \n The min value is {self.find_min()}"


myLinkedList = LinkedList()
myLinkedList.insert_node(1)
myLinkedList.insert_node(2)
myLinkedList.insert_node(3)
myLinkedList.insert_node(4, 0)
myLinkedList.insert_node(5, 2)
myLinkedList.insert_node(6, 4)
myLinkedList.insert_node(7, 32)


myLinkedList.delete_node(6)
myLinkedList.delete_node(55)

myLinkedList.insert_node(777, 4)


print(myLinkedList)
