#!/usr/bin/env python3

class QueueNode(object):
	def __init__(self, value, nxt):
		self.value = value
		self.next = nxt

	def __repr__(self):
		nval = self.next and self.next.value or None
		return f"[{self.value}, {repr(nval)}]"



class Queue(object):

	def __init__(self):
		self.begin = None
		self.end = None


	def shift(self, obj):
		""" another name of 'push' but push front """

		prev_end = self.end
		self.end = QueueNode(obj, None)

		if (prev_end):
			prev_end.next = self.end
		else:
			self.begin = self.end

		self._invariant()


	def unshift(self):
		""" remove first item of list and return it """

		node = self.begin

		if (node == None):
			return None

		self.begin = node.next
			
		if (self.begin == None):
			self.end = None

		self._invariant()

		return node.value



	def count(self):
		""" get count of items """

		node = self.begin
		count = 0
		while (node):
			node = node.next
			count += 1

		return count



	def dump(self, mark):
		""" print all list's item """

		
		print("[[ ", mark , " ]] ---> dump_____")

		node = self.begin
		while (node):
			print("node_v=", node.value)

			assert node.next != node
			node = node.next


		print("_____dump\n")



	def _invariant(self):

		#print("  b->f")
		node = self.begin
		while (node):
			assert node.next != node
			node = node.next

		if (self.end):
			assert self.end.next == None

