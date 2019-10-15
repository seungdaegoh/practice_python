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
	colors.push("Alizarin")
	colors.push("Top")

	print(colors.pop())

	assert colors.pop() == "Alizarin"
	assert colors.pop() == "Magenta"
	assert colors.pop() == None


def test_unshift():
	colors = SingleLinkedList()
	colors.push("Virdian")
	colors.push("Sap Green")
	colors.push("Van Dyke")
	assert colors.unshift() == "Virdian"
	assert colors.unshift() == "Sap Green"
	assert colors.unshift() == "Van Dyke"
	assert colors.unshift() == None


def test_shift():
	colors = SingleLinkedList()
	colors.shift("Cadmium Orange")
	assert colors.count() == 1

	colors.shift("Carbazole Violet")
	assert colors.count() == 2

	assert colors.pop() == "Cadmium Orange"
	assert colors.count() == 1
	assert colors.pop() == "Carbazole Violet"
	assert colors.count() == 0

def test_remove():
	colors = SingleLinkedList()

	colors.push("Cobalt")
	colors.push("Zinc White")
	colors.push("Nickle Yellow")
	colors.push("Perinone")

	assert colors.remove("Cobalt") == 0
	colors.dump("before perinone")
	assert colors.remove("Perinone") == 2
	colors.dump("after perinone")

	assert colors.remove("Nickle Yellow") == 2
	assert colors.remove("Zinc White") == 0




#test_push()
#test_pop()
#print("test unshift")
#test_unshift()

#print("test shift")
#test_shift()

print("test remove")
test_remove()
