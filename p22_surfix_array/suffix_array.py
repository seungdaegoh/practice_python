

class  suffix_array(object):

    def __init__(self, string):
        self.array = []

        n = len(string)
        for i in range(n):
            self.array.append( string[i:] )

        return


    def find_shortest(self, word):

        return None



    def find_longest(self, word):

        return



    def find_all(self, word):

        return
   

    def list(self, msg = None):

        print('-'*16, msg)

        for i in range(len(self.array)):
            print("array[", i, "] str=", self.array[i])



