from config import *         #add config.py

def init():                  #make the init function
    global config            #make config accessible everywhere
    config = read_config()   #read the config (config.py)
