# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None

#     def __str__(self):
#         return str(self.data)


# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.size = 0

#     def __str__(self):
#         if self.head is None:
#             return "Empty"
#         else:
#             return str(self.head.data)

#     def add_first(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head.prev = new_node
#             self.head = new_node
#         self.size += 1

#     def add_last(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.prev = self.tail
#             self.tail.next = new_node
#             self.tail = new_node
#         self.size += 1

#     def add_at(self, data, index):
#         if index < 0 or index > self.size:
#             print("Index out of range")
#             return
#         new_node = Node(data)
#         if index == 0:
#             self.add_first(data)
#         elif index == self.size:
#             self.add_last(data)
#         else:
#             curr = self.head
#             for i in range(index):
#                 curr = curr.next
#             new_node.next = curr
#             new_node.prev = curr.prev
#             curr.prev.next = new_node
#             curr.prev = new_node
#             self.size += 1

#     def remove_first(self):
#         if self.head is None:
#             print("Empty")
#             return
#         else:
#             self.head = self.head.next
#             self.head.prev = None
#             self.size -= 1

#     def remove_last(self):
#         if self.head is None:
#             print("Empty")
#             return
#         else:
#             self.tail = self.tail.prev
#             self.tail.next = None
#             self.size -= 1
