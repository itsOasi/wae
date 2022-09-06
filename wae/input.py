import shutil
from wae import helper, os, json, output

# def login_with_github()

def clear_project():
    print(helper.log("clearing static directory"))
    try:
        helper.cmd("echo y | rmdir /s static") # remove static folder contents
    except:
        print(helper.log("error clearing directory", 1))

def clone_repo(repo):
    print(helper.log(f"cloning from {repo}"))
    try:
        clear_project()
        helper.cmd(f"git clone -b static {repo} static") # clone repo into static folder
        output.write_cache("repo", repo) # update cache
        return True
    except:
        print(helper.log("could not clone repo", 2))
        return False
	
def pull_repo(repo):
    print(helper.log(f"pulling from {repo}"))
    try:
        clear_project()
        helper.cmd(f"git pull {repo}")
        return True
    except:
        print(helper.log("could not pull repo", 2))
        return False

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
