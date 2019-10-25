#!/usr/bin/env python3


from queue import *


def test_shift():
	colors = Queue()
	colors.shift("Cadmium Orange")
	assert colors.count() == 1

	colors.shift("Carbazole Violet")
	assert colors.count() == 2

	assert colors.unshift() == "Cadmium Orange"
	assert colors.count() == 1

	assert colors.unshift() == "Carbazole Violet"
	assert colors.count() == 0
	
	
def test_dump():
	colors = Queue()
	colors.shift("Cadmium Orange")

	colors.dump("have Only 1")
	colors.shift("Carbazole Violet")
	colors.dump("have 2")

	


