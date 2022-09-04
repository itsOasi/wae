from wae import helper, json

def load_page(page):
	return helper.read_file(page)

def log(msg):
	pass

def write_cache(key, value):
	try:
		data = helper.read_file("wae_cache.json") # get file contents
		cache = json.loads(data) # parse json
		cache[key] = value # set key value
		helper.write_file("wae_cache.json", json.dumps(cache)) # write to file
	except:
		_start_cache(key, value)

def read_cache(key):
    # open config file as json object
	try:
		data = helper.read_file("wae_cache.json")
		cache = json.loads(data)
		return cache[key]
	except:
		_start_cache(key, "")

def _start_cache(key, value):
		cache = {}
		cache[key] = value
		helper.write_file("wae_cache.json", json.dumps(cache))
		return cache[key]