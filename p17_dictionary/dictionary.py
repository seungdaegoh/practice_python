from dllist import DoubleLinkedList

class Dictionary(object):
    def __init__(self, num_buckets=256):
        """Initializes a Map with the given number of buckets."""
        # save to init List
        # make buckets which has  List

        self.num_buckets = num_buckets
        self.map = DoubleLinkedList()
        for i in range(num_buckets):
            self.map.push(DoubleLinkedList())


    def hash_key(self, key):
        """Given a key this will create a number and then convert it to
        an index for the aMap's buckets."""
        # return HASH value that was made by key
        return hash(key) % self.num_buckets

    def get_bucket(self, key):
        """Given a key, find the bucket where it would go."""

        # return bucket index
        # using HASH

        idx = self.hash_key(key)
        bucket = self.map.get(idx)
        return bucket
        

    def get_slot(self, key, default=None):
        """
        Returns either the bucket and node for a slot, or None, None
        """
        #point out the bucket
         # bucket ok ?
         #  search bucket
         #   if find  return ( bucket, node)
         #  not found  return ( bucket, next-node)
         #
         # bucket not Ok
         #
        slot = self.get_bucket(key)

        s_num = slot.count()
        for i in range(s_num):

            val = slot.get(i)
            if (val[0] == key):
                return slot, val
                break;

        return slot, None


    def get(self, key, default=None):
        """Gets the value in a bucket for the given key, or the default."""
        # get node
        # return value  or   node ( node == None)
        slot, node = self.get_slot(key)
        if (node):
            return node[1]
        else:
            return default


    def set(self, key, value):
        """Sets the key to the value, replacing any existing value."""

        # get bucket, node
        #  if node ?   ( key was found)
        #   change value

        #  node == None ( do not have key)

        slot, node = self.get_slot(key)
        if (node):
            node[1] = value
        else:
            slot.push([key, value])
           


    def delete(self, key):
        """Deletes the given key from the Map."""
        # get bucket
        # search node
        # detach from List


        slot, val = self.get_slot(key)
        if (val):

            node = slot.begin
            while (node):
                if (node.value[0] == key):
                    print("will be Deleted ", node.value[0], node.value[1])
                    break
                node = node.next

            slot.detach_node(node)



    def list(self):
        """Prints out what's in the Map."""

        print("__________list of dictionary______")

        for i in range(self.num_buckets):
            bucket = self.map.get(i)

            cnt = bucket.count()
            for j in range(cnt):

                node = bucket.get(j)
                print("KEY=", node[0], "VALUE=", node[1])

