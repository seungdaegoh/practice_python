
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
        if (self.root == None):
            self.root = BSTreeNode(None, None)

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
        parent = node
        # search
        while (node):
            if (node.key == key):
                if (parent == self.root):
                    self.root = self.del_node(node)
                elif (parent.left == node):
                    parent.left = self.del_node(node)
                elif (parent.right == node):
                    parent.right = self.del_node(node)
                return

            elif (node.key > key):
                parent = node
                node = node.left

            elif (node.key < key):
                parent = node
                node = node.right

            else:
                print("The key does not exist!")
                return


    
    def del_node(self, node):

        key = node.key
        lcnt = 0
        rcnt = 0
        ln = node.left
        rn = node.right

        if (ln):
            lcnt = self.count(ln)

        if (rn):
            rcnt = self.count(rn)

        """
        if (lcnt > rcnt):
            # replace current node as left node
            # add right node  to left node
        else:
            # replace current node as right node
            # add left node  to right node
        """

        if (lcnt > rcnt):
            node = ln 
            if (rcnt > 0):
                self.insert_node(node, rn)
        else:
            node = rn 
            if (lcnt > 0):
                self.insert_node(node, ln)
           
        print("____The key=", key, "deleted")

        return node


    def insert_node(self, node, inode):

        parent = node
        while (1):
            #print("__node__=", node)
            if (node == None):
                if (parent_left):
                    parent.left = inode
                else:
                    parent.right = inode
                break


            if (node.key > ind.key):
                parent = node
                parent_left = True
                node = node.left

            elif (node.key < ind.key):
                parent = node
                parent_left = False
                node = node.right

            else:
                print("Same Key !! Error")
                break




    def count(self, node = None):

        cnt = 0;
        if (node == None):
            node = self.root

        if (node == None):
            return 0

        if (node.left):
            cnt += self.count(node.left)

        if (node):
            cnt += 1

        if (node.right):
            cnt += self.count(node.right)

        return cnt;


    def list(self, node = None, msg = None):

        if (node == None):
            node = self.root

            if (msg):
                print(msg)

        if (node == None):
            return

        if (node.left):
            self.list(node.left)

        if (node):
            #print('\t' * (indent * 2), end='')
            print("node KEY=", node.key, "V=", node.value)

        if (node.right):
            self.list(node.right)


