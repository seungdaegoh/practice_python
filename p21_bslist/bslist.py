
class BSListNode(object):

    def __init__(self, key, value):
        self.key = key
        self.value  = value

    def __repr__ (self):
        return "BSListNode[key={}, value={}]".format(self.key, self.value)


class  BSList(object):

    def __init__(self):
        self.tbl = []
        self.cnt = 0
        return

    def get(self, key):

        tbl = self.tbl
        st_i = 0
        ed_i = self.cnt

        while (1):

            if (st_i < ed_i):
                mi = int((st_i + ed_i)/2)
                node = tbl[mi]
            else:
                return None

            if (node.key > key):
                ed_i = mi

            elif (node.key < key):
                st_i = mi + 1

            #if (node.key == key):
            else:
                return node

        return None



    def set(self, key, value):

        tbl = self.tbl
        st_i = 0
        ed_i = self.cnt

        while (1):

            if (st_i < ed_i):
                mi = int((st_i + ed_i)/2)
                node = tbl[mi]

            else:
                node = BSListNode(key, value)
                self.add_node(st_i, node)
                return

            if (node.key > key):
                ed_i = mi

            elif (node.key < key):
                st_i = mi + 1
                '''
                if (st_i == mi):
                    st_i += 1
                else:
                    st_i = mi
                '''

            else:
                node.value = value
                break




    def delete(self, key):
        tbl = self.tbl
        st_i = 0
        ed_i = self.cnt

        while (1):

            if (st_i < ed_i):
                mi = int((st_i + ed_i)/2)
                node = tbl[mi]

            else:
                print("Not found key [{}]".format(key))
                return

            if (node.key > key):
                ed_i = mi

            elif (node.key < key):
                if (st_i == mi):
                    st_i += 1
                else:
                    st_i = mi

            else:
                self.del_node(mi)
                break

        return
   

    def del_node(self, idx):
        self.cnt -= 1
        del self.tbl[idx]
        return


    def add_node(self, idx, node):
        self.cnt += 1
        self.tbl.insert(idx, node)


    def count(self):
        return self.cnt;


    def list(self, msg = None):

        print('-'*16, msg)

        for i in range(self.cnt):
            node = self.tbl[i]
            print("node[", i, "] KEY=", node.key, "V=", node.value)



