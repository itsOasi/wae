import os
session_log = []

def log(msg, lvl=0):
    LOG = ["LOG: ", "WRN: ", "ERR: "]
    log_msg = LOG[lvl]+msg
    session_log.append(log_msg)
    return log_msg

def write_file(name, data, perms="w+"):
    # create file for writing to with perms
    f = open(name, perms)
    # write data to file
    f.write(data)
    # log to console for debugging
    log(f"wrote to {name}: {f.read()}")
    f.close()

def read_file(name, perms="r"):
    # create file for reading from
    f = open(name, perms)
    # write data to file
    data = f.read()
    # log to console for debugging
    log(f"read from {name}: {data}")
    f.close()
    return data

def cmd(str):
    os.system(str)
