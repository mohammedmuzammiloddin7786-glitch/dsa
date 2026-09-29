class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, data):
        if self.head == None:
            self.head = Node(data)
            self.size += 1
            return

        cN = self.head
        while cN.next is not None:
            cN = cN.next

        cN.next = Node(data)
        self.size += 1

    def traverse(self):
        if self.head == None:
            print()
            return

        cN = self.head
        while cN.next is not None:
            print(cN.data, end="->")
            cN = cN.next

        print(cN.data)

    def search(self, data):
        cN = self.head
        i = 0

        while cN is not None:
            if cN.data == data:
                print(f"element {data} is at {i} index")
                return

            i += 1
            cN = cN.next

        print("data is not found")

    def len(self):
        return self.size

    def delStart(self):
        if self.head is None:
            return

        self.head = self.head.next
        self.size -= 1

    def insAt(self, data, pos):
        if pos < 0 or pos > self.len():
            print("Invalid position")
            return

        if pos == 0:
            if self.head is None:
                self.head = Node(data)
                self.size += 1
                return
            else:
                obj = Node(data)
                obj.next = self.head
                self.head = obj
                self.size += 1
                return

        if pos == self.len():
            self.add(data)
            return

        cn = self.head
        ind = 0

        while cn.next is not None:
            if ind + 1 == pos:
                break

            cn = cn.next
            ind += 1

        obj = Node(data)
        obj.next = cn.next
        cn.next = obj
        self.size += 1

    def delAt(self, pos):
        if pos < 0 or pos >= self.len():
            print("Invalid position")
            return

        if pos == 0:
            self.head = self.head.next
            self.size -= 1
            return

        cn = self.head
        ind = 0

        while cn.next is not None:
            if ind + 1 == pos:
                break

            cn = cn.next
            ind += 1

        cn.next = cn.next.next
        self.size -= 1


l1 = linkedlist()

l1.add(10)
l1.add(20)
l1.add(30)
l1.add(40)

l1.traverse()

l1.search(10)

print(l1.len())

l1.delStart()
l1.traverse()

l1.insAt(50, 2)
l1.traverse()

l1.delAt(1)
l1.traverse()
