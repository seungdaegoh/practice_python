#!/usr/bin/env python3

class DoubleLinkedListNode(object):
	def __init__(self, value, nxt, prev):
		self.value = value
		self.next = nxt
		self.prev = prev

	def __repr__(self):
		nval = self.next and self.next.value or None
		pval = self.prev and self.prev.value or None
		return f"[{self.value}, {repr(nval)}, {repr(pval)}]"



class DoubleLinkedList(object):


	def __init__(self):
		self.begin = None
		self.end = None


	def push(self, obj):
		"""add item at end of list"""

		if (self.begin == None):
			add = DoubleLinkedListNode(obj, None, None)	

			self.begin = add
			self.end = add

		elif (self.begin == self.end):
			add = DoubleLinkedListNode(obj, None, self.end)
			
			self.end.prev = add
			self.end = add

			self.begin.next = add

		else:
			add = DoubleLinkedListNode(obj, None, self.end)

			self.end.prev = add
			self.end = add



	def pop(self):
		"""remove last item of list and return it"""

		

	def shift(self, obj):
		""" another name of 'push' but push front """



	def unshift(self):
		""" remove first item of list and return it """


	def detach_node(self, node):
		""" take node and remove one which is same as the node """


	def remove(self, obj):
		"""remove that is exactly match with """  



	def first(self):
		""" return first item """
		if (self.begin):
			return self.begin.value
		return None


	def last(self):
		""" return last item """
		if (self.end):
			return self.end.value
		return None


	def count(self):
		""" get count of items """

		node = self.begin
		count = 0
		while (node):
			node = node.next
			count += 1

		return count


	def get(self, index):
		""" get index-item """



	def dump(self, mark):
		""" print all list's item """

		
		print("[[ ", mark , " ]] ---> dump_____")


		print("_____dump\n")


