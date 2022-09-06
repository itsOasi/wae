from wae import input, output, helper

class Model:
	def __init__(self, config_loc):
		'''
			The model represents the engine and the 
			filesystem of the current project
		'''
		self._config_loc = config_loc # the location of wae_config.json
		self._repo = input.get_config(self._config_loc, "repo") # reads wae_config to properly prepare to load the project
		self._ready = self._load_proj()

	def pull(self):
		input.pull_repo(self._repo)

	def load_index(self):
		if self._ready:
			return output.load_page("index.html")
		else: 
			return helper.log("could not load index: not ready", 2)

	def _load_proj(self):
		'''
			perform environment checks and clone repository
		'''
		print(helper.log("loading project"))
		dep_mode = input.get_config(self._config_loc, "dep_mode")
		if dep_mode in ["rel", "release"]:
			output.write_cache("repo", self._repo)
			return input.clone_repo(self._repo) # clone repo into filesystem
		if dep_mode in ["dev", "develop"]:
			if output.read_cache("repo") == self._repo: # if working with the same project as last time
				return input.pull_repo(self._repo) # update local copy of project files
			else: # otherwise
				return input.clone_repo(self._repo) # clone repo into filesystem

			