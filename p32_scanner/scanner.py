import re
import copy
from inspect import getmembers

#obj = object()

class Scanner(object):
    def __init__(self, tokens):
        print("__init__")
        self.re_pat = []
        self.out_tk = []
        for key_str, tok_str in tokens:
            print('k=', key_str)
            re_in = re.compile(key_str)
            self.re_pat.append( (re_in, tok_str) )

        print("______________")
        for v in self.re_pat:
            print(v)
        print("______________")


    def scan(self, line):
        print("in_line=", line)

        self.in_line = line

         #token_list = copy.deepcopy(self.re_pat)
        token_list = self.re_pat

        print("len token_list=", len(token_list))

        i = 0
        while (i < len(self.in_line)):
            token, word, end = self.match(i, token_list)

            assert token, "Failed to match line \"%s\"" %  word
            if token:
                i += end
                self.out_tk.append( (token, word, i, end))

            print("Len = ", len(token_list), len(self.re_pat))

        print("________________")

        for out_t in self.out_tk:
            print("out_t=", out_t)

        return len(self.out_tk)



    def match(self, i, token_list):

        start = self.in_line[i:]
        print("match", i, start)

        idx = 0
        for reexp, token in token_list:

            match = reexp.match(start)
            if (match):
                begin, end = match.span()
                 #del token_list[idx]
                return token, start[:end], end

            idx += 1


        return None, start, None

    def peek(self):
        print("peek")

    def push(self):
        print("push")


