class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        print("Executed Node constructor")

class LinkedList:
    def __init__(self):
        self.head = None
        print("Executed ll constructor")

    def print(self):
        if self.head == None:
            print("The linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)


    def insert_at_beginning(self,data):
        node = Node(data, self.head)
        self.head = node





if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(10)
    ll.print()