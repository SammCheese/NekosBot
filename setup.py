import json, os

# Get config file.
current_dir = os.path.dirname(__file__)
with open(os.path.join(current_dir, 'config.json')) as config_file:  
    config = json.load(config_file)