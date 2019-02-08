# When to use p/p.link/p.link.link in the while condition during traversal
"""
1. p - None - while p in not None
2. p - Last node - while p.link is not None
3. p - Second last node - while p.link.link is not None
"""
# code difference between delete_after and delete_before

"""
_var - better to not use them outside function however nothing is stopping you from doing so
__var - name mangling occurs to keep variables/functions with same names under different classes separately
__var__ - Language specific functions/variables that should never be invented
var_ - used by convention to avoid conflicts with python keywords
"""

class Node:
    def __init__(self, value):
        self.info = value
        self.link = None


class SingleLinkedList:
    def __init__(self):
        self.start = None

    def display_list(self):
        if self.start is None:
            print("List is empty")
            return
        else:
            print("List is : ")
            p = self.start
            while p is not None:
                print(p.info, " ", end='')
                p = p.link
            print()

    def count_nodes(self):
        p = self.start
        n = 0
        while p is not None:
            n += 1
            p = p.link
        print("Number of nodes in the list = ", n)
    
    def search(self, x):
        position = 1
        p = self.start
        while p is not None:
            if p.info == x:
                print(x, " is at position ", position)
                return True
            position += 1
            p = p.link
        else:
            print(x, " was not found in the list")
            return False

    def insert_in_beginning(self, data):
        temp = Node(data)
        temp.link = self.start
        self.start = temp

    def insert_at_end(self, data):
        temp = Node(data)

        if self.start is None:
            self.start = temp
            return

        p = self.start
        while p.link is not None:
            p = p.link
        p.link = temp

    def create_list(self):
        n = int(input("Enter the number of nodes : "))
        if n == 0:
            return
        for i in range(n):
            data = int(input("Enter the element to be inserted : "))
            self.insert_at_end(data)

    def insert_after(self, data, x):
        p = self.start
        while p is not None:
            if p.info == x:
                break
            p = p.link

        if p is None:
            print(x, "was not present in the list")
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp

    def insert_before(self, data, x):
        p = self.start

        if p is None:
            print("List is empty")
            return

        if x == p.info:
            temp = Node(data)
            temp.link = p
            self.start = temp
            return

        while p.link is not None:
            if p.link.info == x:
                break
            p = p.link

        if p.link is None:
            print(x, "was not found in the list")
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp

    def insert_at_position(self, data, k):
        p = self.start

        if k == 1:
            temp = Node(data)
            temp.link = p
            self.start = temp
            return

        i = 1
        while i<k-1 and p is not None:
            p = p.link
            i += 1

        if p is None:
            print("You can insert only upto position ", i)
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp

    def delete_node(self, x):
        if self.start is None:
            print("List is empty")
            return

        if self.start.info == x:
            self.start = self.start.link
            return

        p = self.start

        while p.link is not None:
            if p.link.info == x:
                break
            p = p.link

        if p.link is None:
            print("Element ", x, "was not found in the list")
        else:
            p.link = p.link.link

    def delete_first_node(self):
        if self.start is None:
            return
        
        self.start = self.start.link

    def delete_last_node(self):
        if self.start is None:
            return

        if self.start.link is None:
            self.start = None
            return

        p = self.start
        while p.link.link is not None:
            p = p.link

        p.link = None

    def reverse_list(self):
        p = self.start
        prev = None

        while p is not None:
            next = p.link
            p.link = prev
            prev = p
            p = next
        self.start = prev

    def bubble_sort_exdata(self):
        end = None

        while end != self.start.link:
            p = self.start
            while p.link != end:
                q = p.link
                if p.info > q.info:
                    p.info, q.info = q.info, p.info
                p = p.link
            end = p

    def bubble_sort_exlinks(self):
        end = None

        while end != self.start.link:
            r = p = self.start
            while p.link != end:
                q = p.link
                if p.info > q.info:
                    p.link = q.link
                    q.link = p
                    if p != self.start:
                        r.link = q
                    else:
                        self.start = q
                    p,q = q,p
                r = p
                p = p.link
            end = p

    def has_cycle(self):
        pass

    def find_cycle(self):
        pass

    def remove_cycle(self):
        pass

    def insert_cycle(self, x):
        pass

    def merge1(self, list2):
        merge_list = SingleLinkedList()
        merge_list.start = self._merge1(self.start, list2.start)
        return merge_list

    def _merge1(self, p1, p2):
        if p1.info <= p2.info:
            startM = Node(p1.info)
            p1 = p1.link
        else:
            startM = Node(p2.info)
            p2 = p2.link

        pM = startM

        while p1 is not None and p2 is not None:
            if p1.info <= p2.info:
                pM.link = Node(p1.info)
                p1 = p1.link
            else:
                pM.link = Node(p2.info)
                p2 = p2.link
            pM = pM.link

        while p1 is not None:
            pM.link = Node(p1.info)
            p1 = p1.link
            pM = pM.link

        while p2 is not None:
            pM.link = Node(p2.info)
            p2 = p2.link
            pM = pM.link

        return startM

    def merge2(self, list2):
        merge_list = SingleLinkedList()
        merge_list.start = self._merge2(self.start, list2.start)
        return merge_list

    def _merge2(self, p1, p2):
        if p1.info <= p2.info:
            startM = p1
            p1 = p1.link
        else:
            startM = p2
            p2 = p2.link

        pM = startM

        while p1 is not None and p2 is not None:
            if p1.info <= p2.info:
                pM.link = p1
                p1 = p1.link
                pM = pM.link
            else:
                pM.link = p2
                p2 = p2.link
                pM = pM.link

        if p1 is None:
            pM.link = p2
        else:
            pM.link = p1

        return startM

    def merge_sort(self):
        pass

    def _merge_sort_rec(self, listStart):
        pass

    def _divide_list(self, p):
        pass

###############################################################################

list = SingleLinkedList()

list.create_list()

while True:
    print("1. Display list")
    print("2. Count the number of nodes")
    print("3. Search for an element")
    print("4. Insert in empty list/Insert in beginning of the list")
    print("5. Insert a node at the end of the list")
    print("6. Insert a node after a specified node")
    print("7. Insert a node before a specified node")
    print("8. Insert a node at a given position")
    print("9. Delete first node")
    print("10. Delete last node")
    print("11. Delete any node")
    print("12. Reverse the list")
    print("13. Bubble sort by exchanging data")
    print("14. Bubble sort by exhanging links")
    print("15. Merge sort")
    print("16. Insert cycle")
    print("17. Detect cycle")
    print("18. Remove cycle")
    print("19. Quit")

    option = int(input("Enter your choice : "))

    if option == 1:
        list.display_list()
    elif option == 2:
        list.count_nodes()
    elif option == 3:
        data = int(input("Enter the element to be searched : "))
        list.search(data)
    elif option == 4:
        data = int(input("Enter the element to be inserted : "))
        list.insert_in_beginning(data)
    elif option == 5:
        data = int(input("Enter the element to be inserted : "))
        list.insert_at_end(data)
    elif option == 6:
        data = int(input("Enter the element to be inserted : "))
        x = int(input("Enter the element after which to insert : "))
        list.insert_after(data, x)
    elif option == 7:
        data = int(input("Enter the element to be inserted : "))
        x = int(input("Enter the element before which to insert : "))
        list.insert_before(data, x)
    elif option == 8:
        data = int(input("Enter the element to be inserted : "))
        k = int(input("Enter the position at which to insert : "))
        list.insert_at_position(data, k)
    elif option == 9:
        list.delete_first_node()
    elif option == 10:
        list.delete_last_node()
    elif option == 11:
        data = int(input("Enter the element to be deleted : "))
        list.delete_node(data)
    elif option == 12:
        list.reverse_list()
    elif option == 13:
        list.bubble_sort_exdata()
    elif option == 14:
        list.bubble_sort_exlinks()
    elif option == 15:
        list.merge_sort()
    elif option == 16:
        data = int(input("Enter the element at which the cycle has to be inserted : "))
        list.insert_cycle(data)
    elif option == 17:
        if list.has_cycle():
            print("List has a cycle")
        else:
            print("List doesn't have a cycle")
    elif option == 18:
        list.remove_cycle()
    elif option == 19:
        break
    else:
        print("Wrong option")

    print()

"""
# Run merge1 and merge2 functions:
list1 = SingleLinkedList()
list1.create_list()

list2 = SingleLinkedList()
list2.create_list()

list1.bubble_sort_exdata()
list2.bubble_sort_exdata()

list1.display_list()
list2.display_list()

list3 = list1.merge1(list2)
list3.display_list()

list3 = list1.merge2(list2)
list3.display_list()
"""
    
