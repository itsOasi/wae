import components
import random
import json

class Model(components.base.Entity):
	def __init__(self, name):
		super().__init__("Mod000000", name)
		# all entities available for loading
		self._archive = {}
		# all currently loaded entities
		self._entities = {}
		# a view is a collection of entities, components, and media
		self._views = {}
		# locations of all media dependencies
		self._media = {
			"audio":{},
			"images":{},
			"video":{},
			"shaders":{}
		}
	
	# adds views to the model
	def import_view(self, view_loc):
		# loads view from json file and adds it to view
		view = {}
		# self._views[view.name] = view
	
	def load_view(self, view):
		pass
		
	# generates a random number with a given prefix
	def gen_id(self, prefix):
		return prefix + str(random.randint(111111, 999999))
	
	# instantiates an archived entity
	def load_entity(self, arc_id):
		print(f"Loading entity: {arc_id}")
		arc_ent = self._archive[arc_id]
		entity = self.get_entity(self.add_entity(arc_ent.get_name))
		return entity.get_id()
	
	# creates and immediately adds an entity to the model
	def add_entity(self, name):
		ent_id = self.gen_id("ENT")
		print(f"Adding entity: {ent_id}:{name}")
		self._entities[ent_id] = components.base.Entity(ent_id, name)
		return ent_id
	
	# archives an entity to be later instantiated into the model
	def arc_entity(self, name):
		ent_id = self.gen_id("ARC")
		print(f"Archiving entity: {ent_id}:{name}")
		self._archive[name] = components.base.Entity(ent_id, name)
		return ent_id
		
		
	def get_entity(self, id):
		return self._entities[id]
	
	# adds comp to model and adds comp id to entity comps
	def add_comp(self, comp, entity):
		print(f"Adding component {comp.get_id()} to {entity.get_name()}")
		# creates table for comp type if it doesnt already exist
		if not comp.get_type() in self._comps:
			self._comps[comp.get_type()] = {}
		self._comps[comp.get_type()][comp.get_id()] = comp
		entity.add_comp(comp.get_type(), comp.get_id())
		comp.set_parent(entity)

	def get_comp(self, comp_type, comp_id):
		return self._comps[comp_type][comp_id]
	
	# prints an overview of active system level properties, entities and components
	def peek(self):
		data = ""
		data += "OVERVIEW\n"
		data += f"id:\t  name:{' ' * (len(self._name)-4)}props:\n"
		data += f"{self}\n"
		data += "\nENTITIES:\n"
		data += "  id:\t  name:\tprops:\n"
		for ent in self._entities:
			data += f"  {self._entities[ent]}\n"
		data += "\nCOMPONENTS:\n"
		for comp_type in self._comps:
			data+=f"{comp_type}\n"
			data += "  id:\tparent:\t props:\n"
			for comp in self._comps[comp_type]:
				data += f"  {self._comps[comp_type][comp]}\n"
		return data
	
	# returns the entire model as json; informationally equivalent to peek()
	def freeze(self):
		data = ""
		# TODO: return a json string detailing active entities and components
		return data