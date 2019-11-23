
class BSTreeNode(object):

    def __init__(self, key, value):
        #left, right
        self.key = key
        self.value  = value
        self.left = None
        self.right = None


    def __repr__ (self):
        return "BSTreeNode[L:{},R:{}, key={}, value={}".format(self.left != None, self.right != None, self.key, self.value)

class  BSTree(object):

    def __init__(self):
        self.root = BSTreeNode(None, None)

    def get(self, key):

        node = self.root

        #search
        while (node):
            if (node.key == key):
                break

            elif (node.key > key):
                node = node.left

            elif (node.key < key):
                node = node.right

            else:
                print("The key does not exist!")
                return None

        return node


    def set(self, key, value):
        node = self.root
        parent = node

        #search
        while (1):

            #print("__node__=", node)

            if (node == None):
                node = BSTreeNode(key, value)

                #print("__parent__=", parent)

                if (parent_left):
                    parent.left = node
                else:
                    parent.right = node
                break

            #add new key, value at node

            if (node.key == None):
                node.key = key
                node.value = value

                #print("set None key node by writing key, value=", value)
                break

            elif (node.key > key):
                parent = node
                parent_left = True
                node = node.left

            elif (node.key < key):
                parent = node
                parent_left = False
                node = node.right

            #if (node.key == key):
            else:
                node.value = value
                break




    def delete(self, key):
        node = self.root
        # search
        while (node):
            if (node.key == key):
                self.del_node(node)
                return

            elif (node.key > key):
                node = node.left

            elif (node.key < key):
                node = node.right

            else:
                print("The key does not exist!")
                return

    
    def del_node(self, node):
        print("TODO")
        print("The key=", node.key, "deleted")


    def list(self, node = None, msg = None):

        if (node == None):
            node = self.root

            if (msg):
                print(msg)
        

        if (node.left):
            self.list(node.left)

        if (node):
            #print('\t' * (indent * 2), end='')
            print("node KEY=", node.key, "V=", node.value)

        if (node.right):
            self.list(node.right)


