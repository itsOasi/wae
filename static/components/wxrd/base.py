class Base:
	'''
		basis for data structures
		should mostly be used for custom properties
	'''
	def __init__(self, id):
		self._id = id
		self._props = {}
		self._tags = []

	def get_id(self):
		return self._id
	
	def set_prop(self, key, value):
		# TODO: add type-checking for props that already exist
		self._props[key] = value
	
	def get_prop(self, key):
		return self._props[key]
	
	def add_tag(self, tag):
		self._tags.append(tag)
	
	def has_tag(self, tag):
		return bool(self._tags[tag])
	
	def del_tag(self, tag):
		del self._tags[tag]
	
	def __str__(self):
		return self.__repr__()
	
	def __repr__(self):
		return f"{self._props}"
		
	

class Component(Base):
	''' 
		basic component object to be derived from
		
		this is where specialized and advanced 
		functionality is created
	'''
	
	def __init__(self, id, comp_type):
		super().__init__(id)
		self._comp_type = comp_type
		self._parent = None
	
	def __str__(self):
		data = f"{self._id}\t{self._parent.get_name()}\t{self._props}"
		return data
	
	def __repr__(self):
		return self.__str__()
	
	def get_type(self):
		return self._comp_type
	
	def set_parent(self, entity):
		# TODO: block parent from being changed if it is already set
		self._parent = entity

class Entity(Base):
	'''
		building block of the model
		
		contains collections of data and components
	'''
	def __init__(self, id, name):
		super().__init__(id)
		self._name = name
		self._comps = {}
	
	# adds a new component
	def add_comp(self, key, id):
		self._comps[key] = id
	
	def has_comp(self, id):
		return bool(self._comps[id])
	
	def get_comp(self, key):
		return self._comps[key]
	
	def set_name(self, name):
		self._name = name
	
	def get_name(self):
		return self._name
	
	def __str__(self):
		return f"{self._id} {self._name} {self._props}"
		
	def __repr__(self):
		return self.__str__()
