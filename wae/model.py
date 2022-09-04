from wae import input, output, helper

class Model:
	def __init__(self, config_loc):
		'''
			The model represents the engine and the 
			filesystem of the current project
		'''
		self._config_loc = config_loc # the location of wae_config.json
		self._repo = input.get_config(self._config_loc, "repo") # reads wae_config to properly prepare to load the project
		dep_mode = input.get_config(self._config_loc, "dep_mode")
		if dep_mode in ["rel", "release"]:
			self._ready = self._load_proj()
		if dep_mode in ["dev", "develop"]:
			self._ready = True

	def pull(self):
		if self._ready:
			input.pull_repo(self._repo)

	def load_index(self):
		if self._ready:
			return output.load_page("index.html")
		return "load_index failed: check output log"

	def _load_proj(self):
		'''
			perform environment checks and clone repository
		'''
		if output.read_cache("repo") == self._repo: # if working with the same project as last time
			self._ready = input.pull_repo(self._repo) # update local copy of project files
		else: # otherwise
			# clear static directory
			output.write_cache("repo", self._repo)
			self._ready = input.clone_repo(self._repo) # clone repo into filesystem