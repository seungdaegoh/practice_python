import subprocess
import sys
import tr

def test_tr_cmd():
    exec = "python tr.py -s a-z < testin.txt"
    print( exec )
    output = subprocess.run(exec,  stdout=subprocess.PIPE)
    print(output)


def test_main():
    cmd = ["simply"]
    tr.main(cmd,  "abc", 'a')

def test_str_append():
    r_str = tr.get_append_str("a-g")
    assert("abcdefg" == r_str)

def test_simply():
    cmd = ["simply"]
    assert (tr.main(cmd, "aaaa", 'a') == 'a')
    assert (tr.main(cmd, "aaaabbbcccd", 'a-z') == "abcd" )
    assert (tr.main(cmd, "AAABBBCC", 'a-z') == "AAABBBCC")
    assert (tr.main(cmd, "aaabbbccAAABBBCC", 'A-Z') == "aaabbbccABC")
    assert (tr.main(cmd, "aaabbbccAAABBBCC", 'a-z') == "abcAAABBBCC")
    assert (tr.main(cmd, "Hi,   is   there    any things?", ' ') == "Hi, is there any things?")

def test_delete():
    cmd = ['delete']
    assert (tr.main(cmd, "aaaab", 'a') == 'b')
    assert (tr.main(cmd, "aaabbbccdef", 'a-c') == 'def')
    assert (tr.main(cmd, "aaabbbccdeffgg", 'c-z') == 'aaabbb')


def test_error_condition_cmd():
    cmd = ["simply", "delete"]
    assert ("Error" in (tr.main(cmd, "aaabbbccdef", 'a-c')) )

    cmd = ["simply"]
    assert ("Error" in (tr.main(cmd, "aaabbbccdef", 'a-c',  'A-Z')) )

    cmd = ["delete"]
    assert ("Error" in (tr.main(cmd, "aaabbbccdef", 'a-c',  'A-Z')) )



def test_translate():
    cmd = [ ] # Nothing
    assert (tr.main(cmd, "ABC", 'A-Z') == None)  # Error Condition : SET2 is empty

    assert (tr.main(cmd, "ABC", 'A-Z', 'a-c') == None) #catch error, because its len is different
    
    assert (tr.main(cmd, "ABCDZZZ", 'A-Z',  'a-z') == 'abcdzzz')
    assert (tr.main(cmd, "abcdzzz", 'a-z', 'A-Z' ) == 'ABCDZZZ')
    assert (tr.main(cmd, "abcdzzzABCDZZZ", 'a-z', 'A-Z') == 'ABCDZZZABCDZZZ')
    assert (tr.main(cmd, "abcdzzzABCDZZZ", 'A-Z', 'a-z') == 'abcdzzzabcdzzz')
    assert (tr.main(cmd, "My\nUID is\n1004", '\n', ' ') == 'My UID is 1004')
    assert (tr.main(cmd, "My UID is 1004", ' ', ':') == 'My:UID:is:1004')






