import ast #add the ast library

def read_config(file="config.json"):    #make function read_config, with default file config.json
    global config                       #make config accessible everywhere
    f = open(file, "r")                 #open the config file for reading
    config = f.read()                   #read the file
    f.close()                           #close the file
    config = ast.literal_eval(config)   #convert config from string -> dict
    return config                       #return the dict config
