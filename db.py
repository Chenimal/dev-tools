# a command line tool to easily select db to connect
import yaml
from subprocess import call

# load config file
f = open("/Users/chen/lalamove/data/db.yml")
o = yaml.load(f)

# select environment
selected_env = input(o.keys())
if selected_env not in o:
    print("Too simple")
    exit()

# select projects
selected_project = input(o[selected_env].keys())
if selected_project not in o[selected_env]:
    print("Sometimes naive")
    exit()

# select city
selected_city = input(o[selected_env][selected_project].keys())
if selected_city not in o[selected_env][selected_project]:
    print("Naive")
    exit()

call(o[selected_env][selected_project][selected_city].split(' '))



