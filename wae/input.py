import shutil
from wae import helper, os, json, output

# def login_with_github()

def clone_repo(repo):
    try:
        helper.cmd("rmdir static/* static/.*") # remove static folder contents
        helper.cmd("rmdir static") # remove static folder
        helper.cmd(f"git clone -b static {repo} static") # clone repo into static folder
        output.write_cache("repo", repo) # update cache
        return True
    except:
        print("could not clone repo")
        return False
	
def pull_repo(repo):
    helper.cmd(f"git pull {repo}")

# def download_from_store()

def store_uploaded_file(name, data):
    helper.write_file(name, data, "wb+")

def set_config(config_loc, key, value):
    data = helper.read_file(config_loc) # open config file
    config = json.loads(data) # parse json data
    config[key] = value # set key value
    helper.write_file(config_loc, json.dumps(config)) # apply to config file


def get_config(config_loc, key):
    data = helper.read_file(config_loc) # open config file
    config = json.loads(data) # parse json
    return config[key] # return key value
