
class SingleLinkedListNode(object):
	def __init__(self, value, nxt):
		self.value = value
		self.next = nxt

	def __repr__(self):
		nval = self.next and self.next.value or None
		#return f"[{self.value}:{repr(nval)}]"
		return f"{self.value}"

class SingleLinkedList(object):


	def __init__(self):
		self.begin = None
		self.end = None
		self.cnt = 0


	def push(self, obj):
		"""add item at end of list"""

		self.cnt += 1
		add_obj = SingleLinkedListNode(obj, self.end)

		if (self.end) :
			self.end.next = add_obj

		self.end = add_obj;
		
		if (self.begin == None):
			self.begin = add_obj;



	def pop(self):
		"""remove last item of list and return it"""

		self.cnt -= 1
		chk = self.begin
		ret = self.end.value

		while (chk.next != self.end):
			chk = chk.next

		self.end = chk
		chk.next = None

		return ret
		

	def shift(self, obj):

		""" another name of 'push' """

	def unshift(self):
		""" remove first item of list and return it """


	def remove(self, obj):
		"""remove that is exactly match with """

	def first(self):
		""" return first item """

	def last(self):
		""" return last item """


	def count(self):
		""" get count of items """
		return self.cnt


	def get(self, index):
		""" get index-item """

	def dump(self, mark):
		""" print all list's item """

		print("[[dump_____")
		chk = self.begin

		while (chk):
			print(chk)
			chk = chk.next
		print("_____dump ]]")


#my_item = SingleLinkedList(7, None)
#my_item = SingleLinkedList()
#print(my_item)
