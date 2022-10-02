import ast

def read_config(file="config.json"):
    global config
    f = open(file, "r")
    config = f.read()
    f.close()
    config = ast.literal_eval(config)
    return config
