
class StackNode(object):

	def __init__(self, value, nxt):
		self.value = value
		self.next = nxt

	def __repr__(self):
		nval = self.next and self.next.value or None
		return f"[{self.value}:{repr(nval)}]"


class Stack(object):

	def __init__(self):
		self.top = None


	def push(self, obj):
		"""push new node to stack"""
		node = StackNode(obj, self.top)
		self.top = node



	def pop(self):
		"""pop one node of stack and return"""
		node = self.top
		if (node == None):
			return None
			
		self.top = self.top.next

		return node.value


	def top_node(self):
		"""get top node of stack"""

		if (self.top):
			return self.top.value

		return None


	def count(self):
		"""return count of all stack element"""
		count = 0
		node = self.top
		while (node):
			count += 1
			node = node.next
		return count


	def dump(self, mark="----"):
		"""debug function for showing all elements of all stack"""

		print("----", mark, "----")
		node = self.top

		while (node):
			print(node.value)
			node = node.next
		
		print("----------------\n")
