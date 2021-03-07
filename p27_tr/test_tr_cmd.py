import subprocess
import sys
import tr

def test_main():
    cmd = ["simply"]
    tr.main(cmd,  "abc", 'a')

def test_simply():
    cmd = ["simply"]
    assert (tr.main(cmd, "aaaabbbcccd", 'a-z') == "abcd" )
    assert (tr.main(cmd, "AAABBBCC", 'a-z') == "AAABBBCC")
    assert (tr.main(cmd, "aaabbbccAAABBBCC", 'A-Z') == "aaabbbccABC")
    assert (tr.main(cmd, "aaabbbccAAABBBCC", 'a-z') == "abcAAABBBCC")
    assert (tr.main(cmd, "Hi,   is   there    any things?", ' ') == "Hi, is there any things?")

def test_delete():
    cmd = ['delete']
    assert (tr.main(cmd, "aaabbbccdef", 'a-c') == 'def')
    assert (tr.main(cmd, "aaabbbccdeffgg", 'e-z') == 'aaabbbccd')

def test_translate():
    cmd = [ ] # Nothing
    assert (tr.main(cmd, "ABCDZZZ", 'A-Z',  'a-z') == 'abcdzzz')
    assert (tr.main(cmd, "abcdzzz", 'a-z', 'A-Z' ) == 'ABCDZZZ')
    assert (tr.main(cmd, "abcdzzzABCDZZZ", 'a-z', 'A-Z') == 'ABCDZZZABCDZZZ')
    assert (tr.main(cmd, "abcdzzzABCDZZZ", 'A-Z', 'a-z') == 'abcdzzzabcdzzz')
    assert (tr.main(cmd, "My\nUID is\n1004", '\n', ' ') == 'My UID is 1004')
    assert (tr.main(cmd, "My UID is 1004", ' ', ':') == 'My:UID:is:1004')


'''
def test_tr_1():
    exec = "python tr.py -s a-z"
    #exec = []
    #exec.append ( "python tr.py" )

    print( exec )

    input = "aaaabbbbccc"
    output = subprocess.run(exec,  stdout=subprocess.PIPE, stdin =input)
    #output = subprocess.Popen( exec, shell=True, stdout=subprocess.PIPE)
    #output = subprocess.check_output( exec, stdin =input )
    print(output)

'''




