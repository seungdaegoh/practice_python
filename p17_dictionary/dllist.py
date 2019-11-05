class DoubleLinkedListNode(object):
    def __init__(self, value, nxt, prev):
        self.value = value
        self.next = nxt
        self.prev = prev

    def __repr__(self):
        nval = self.next and self.next.value or None
        pval = self.prev and self.prev.value or None
        return f"[{self.value}, {repr(nval)}, {repr(pval)}]"


class DoubleLinkedList(object):

    def __init__(self):
        self.begin = None
        self.end = None
        self._cnt = 0


    def push(self, obj):
        """add item at end of list"""

        if (self.begin == None):
            add = DoubleLinkedListNode(obj, None, None)	

            self.begin = add
            self.end = add
            assert self.begin == self.end

        elif (self.begin == self.end):
            add = DoubleLinkedListNode(obj, None, self.end)

            self.end = add
            self.begin.next = add

            assert self.end.prev == self.begin

        else:
            add = DoubleLinkedListNode(obj, None, self.end)

            self.end.next = add
            self.end = add

        self._cnt += 1


    def pop(self):
        """remove last item of list and return it"""

        node = self.end

        if (node == None):
            return None

        if (node.prev):
            self.end = node.prev
            self.end.next = None

        else:
            self.begin = None
            self.end = None

        self._cnt -= 1
        return node.value

    def shift(self, obj):
        """ another name of 'push' but push front """

        if (self.begin == None):
            add = DoubleLinkedListNode(obj, None, None)

            self.begin = add
            self.end = add

        elif (self.begin == self.end):
            add = DoubleLinkedListNode(obj, self.begin, None)

            self.begin = add
            self.end.prev = add

            assert self.begin.next == self.end
            assert self.end.prev == self.begin

        else:
            add = DoubleLinkedListNode(obj, self.begin, None)

            self.begin.prev = add
            self.begin = add

    def unshift(self):
        """ remove first item of list and return it """

        node = self.begin

        if (node == None):
            return None

        if (node.next):
            self.begin = node.next
            self.begin.prev = None

        else:
            self.begin = None
            self.end = None

        return node.value

    def detach_node(self, node):
        """ take node and remove one which is same as the node """

        prv = node.prev
        nxt = node.next

        if (prv):
            prv.next = nxt
        if (nxt):
            nxt.prev = prv

    def remove(self, obj):
        """remove that is exactly match with """

        node = self.begin
        while (node):
            if (node.value == obj):
                break
            node = node.next

        self.detach_node(node)

        if (node == self.begin):
            self.begin = node.next
            return 0

        elif (node == self.end):
            self.end = node.prev
            return 2
        else:
            return 1

    def first(self):
        """ return first item """
        if (self.begin):
            return self.begin.value
        return None

    def last(self):
        """ return last item """
        if (self.end):
            return self.end.value
        return None

    def count(self):
        """ get count of items """
        return self._cnt


    def get(self, index):
        """ get index-item """

        idx = 0
        node = self.begin
        while (node):
            if (idx == index):
                break
            idx += 1
            node = node.next

        if (node):
            return node.value

        return None

    def dump(self, mark):
        """ print all list's item """

        print("[[ ", mark, " ]] ---> dump_____")

        print("  f->b")
        node = self.begin
        while (node):
            print("node_v=", node.value)

            assert node.next != node
            node = node.next

        print("_____dump\n")


    def _invariant(self):

        #print("  b->f")
        node = self.begin
        while (node):
            assert node.next != node
            node = node.next

        #print("  b->f")
        node = self.end
        while (node):
            assert node.prev != node
            node = node.prev

        if (self.begin):
            assert self.begin.prev == None

        if (self.end):
            assert self.end.next == None
