import re


search_word = r"[A-Za-z]+[0-9]+"
print( re.match(search_word, "1234abc1234adb1234").span())


'''
m = re.match(r'.*BC?$',  "helloB").span()
print(m)
print( re.match(r"[A-Za-z][0-9]+", "A1234567BBBB12341234").span() )

print( re.match(r"[A-Za-z]+[0-9]+", "abc1234").span())
'''


