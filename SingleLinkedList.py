class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
class SLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
sg = SLinkedList()
node1=Node(1)
node2=Node(2)
sg.head=node1
sg.head.next=node2
sg.tail=node2
