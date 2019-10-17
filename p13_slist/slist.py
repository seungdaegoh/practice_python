#! /home/peter/anaconda3/bin/python3
#! /usr/bin/python3

class SingleLinkedListNode(object):
	def __init__(self, value, nxt):
		self.value = value
		self.next = nxt

	def __repr__(self):
		nval = self.next and self.next.value or None
		#return f"[{self.value}:{repr(nval)}]"
		return f"[{self.value}]"

class SingleLinkedList(object):


	def __init__(self):
		self.begin = None
		self.end = None
		self.cnt = 0


	def push(self, obj):
		"""add item at end of list"""

		self.cnt += 1
		add_obj = SingleLinkedListNode(obj, None)

		if (self.end) :
			self.end.next = add_obj

		self.end = add_obj;
		
		if (self.begin == None):
			self.begin = add_obj;



	def pop(self):
		"""remove last item of list and return it"""

		if (self.cnt == 0):
			#print("___pop return None")
			return None

		self.cnt -= 1
		chk = self.begin
		ret = self.end.value

		pre = None

		if (self.cnt == 0):
			self.begin = None
			self.end = None

		else :
			while (chk.next):
				pre = chk
				chk = chk.next


			self.end = pre
			self.end.next = None

		#print("__pop = ", ret)

		return ret
		

	def shift(self, obj):
		""" another name of 'push' """

		self.cnt += 1
		add_obj = SingleLinkedListNode(obj, self.begin)

		self.begin = add_obj;

		if (self.end == None) :
			self.end = add_obj


	def unshift(self):
		""" remove first item of list and return it """

		if (self.cnt == 0):
			return None

		self.cnt -= 1
		chk = self.begin
		ret = chk.value

		self.begin = chk.next

		return ret


	def remove(self, obj):
		"""remove that is exactly match with """  

		pre = None
		chk = self.begin

		while (chk):
			if (chk.value == obj):

				if (pre == None) :
					self.begin = chk.next
					return 0

				pre.next = chk.next
				return 2

			pre = chk
			chk = chk.next



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
		return self.cnt


	def get(self, index):
		""" get index-item """

		if (index >= self.cnt):
			return None
		if (index < 0):
			return None

		chk = self.begin
		while (index > 0):
			chk = chk.next
			index -= 1
		return chk.value

	def dump(self, mark):
		""" print all list's item """

		
		print("[[ ", mark , " ---> dump_____")
		chk = self.begin

		while (chk):
			print(chk)
			chk = chk.next
		print("_____dump ]]")


#my_item = SingleLinkedList(7, None)
#my_item = SingleLinkedList()
#print(my_item)
