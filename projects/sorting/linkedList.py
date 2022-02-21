class ListNode:
    def __init__(self):
        self.repr = ""
        return

def constructSingRepr(sll, Repr):
    if sll == None:
        return Repr
    Repr += str(sll.val) + ", "
    return constructSingRepr(sll.next, Repr)

class SingListNode(ListNode):
    def __init__(self, val=0, next=None):
        super().__init__()
        self.val = val
        self.next = next

    def __str__(self):
        if len(self.repr) == 0:
            self.repr = constructSingRepr(self, self.repr)
        return self.repr

class DoubListNode(ListNode):
    def __init__(self, val=0, next=None, prev=None):
        super().__init__()
        self.val = val
        self.next = next
        self.prev = prev


def constructLinkedList(contents, mode="single", circular=False, dummy=False):
    '''
    contents: list of nums
    mode: single, double
    circular: True, False
    dummy: True, False
    '''
    if mode == "single":
        Head = SingListNode(contents[0])
        prevNode = Head
        for i in range(1, len(contents)):
            newNode = SingListNode(val=contents[i])
            prevNode.next = newNode
            prevNode = newNode
    return Head
