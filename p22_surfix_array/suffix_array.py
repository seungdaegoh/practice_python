

class  suffix_array(object):

    def __init__(self, string):
        self.array = []

        n = len(string)
        for i in range(n):
            self.array.append( string[i:] )

        return


    def find_shortest(self, word):

        w_len = len(word)
        for i in range(len(self.array) -1 , -1, -1):
            if (word == self.array[i][:w_len]):
                return self.array[i]

        return None



    def find_longest(self, word):

        w_len = len(word)
        for i in range(len(self.array)):
            if (word == self.array[i][:w_len]):
                return self.array[i]

        return None



    def find_all(self, word):

        fw = []
        w_len = len(word)
        for i in range(len(self.array)):
            if (word == self.array[i][:w_len]):
                #print("__SEARCHED_WORD:", self.array[i])
                fw.append( self.array[i] )

        if (len(fw) > 0):
            return fw
        else:
            return None
  


    def list(self, msg = None):

        print('-'*16, msg)

        for i in range(len(self.array)):
            print("array[", i, "] str=", self.array[i])



