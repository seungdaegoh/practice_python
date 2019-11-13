from dllist import DoubleLinkedList

class Dictionary(object):
    def __init__(self, num_buckets=256):
        """Initializes a Map with the given number of buckets."""
        # save to init List
        # make buckets which has  List

    def hash_key(self, key):
        """Given a key this will create a number and then convert it to
        an index for the aMap's buckets."""
        # return HASH value that was made by key

    def get_bucket(self, key):
        """Given a key, find the bucket where it would go."""

        # return bucket index
        # using HASH

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


    def get(self, key, default=None):
        """Gets the value in a bucket for the given key, or the default."""
        # get node
        # return value  or   node ( node == None)

    def set(self, key, value):
        """Sets the key to the value, replacing any existing value."""

        # get bucket, node
        #  if node ?   ( key was found)
        #   change value

        #  node == None ( do not have key)


    def delete(self, key):
        """Deletes the given key from the Map."""
        # get bucket
        # search node
        # detach from List

    def list(self):
        """Prints out what's in the Map."""
