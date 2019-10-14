#! /home/peter/anaconda3/bin/python3
#! /usr/bin/python3


from slist import *

def test_push( ):
	colors = SingleLinkedList()
	colors.push("Pthalo Blue")
	assert colors.count() == 1
	colors.push("Ultramarine Blue")
	assert colors.count() == 2


def test_pop( ):
	colors = SingleLinkedList()
	colors.push("Magenta")
	colors.dump('')
	colors.push("Alizarin")
	colors.dump('')

	print(colors.pop())
	print(colors.pop())
	print(colors.pop())
#assert colors.pop() == "Alizarin"
	assert colors.pop() == "Magenta"
	assert colors.pop() == None

test_push()
test_pop()
