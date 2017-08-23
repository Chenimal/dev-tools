# a command line tool to easily select db to connect
import yaml
from colorama import Fore
from subprocess import call

# load config file
f = open("/Users/chen/lalamove/data/db.yml")
o = yaml.load(f)

# select environment
selected_env = input(Fore.GREEN + (',').join(list(o.keys())) + ": ")
if selected_env not in o:
    print(Fore.RED+ "Too young")
    exit()

projects = o[selected_env]
# if only one project, auto-select it
if len(projects) == 1:
    selected_project = list(projects.values())[0]
else:
    # select projects
    selected_project = input(Fore.GREEN + (',').join(list(projects.keys())) + ": ")
    if selected_project not in projects:
        print(Fore.RED+ "Too simple")
        exit()

cities = projects[selected_project]
# if only one city, run early
if len(cities) == 1:
	print(Fore.WHITE+"Connecting DB...")
	call(list(cities.values())[0].split(' '))
	exit()

# select city
selected_city = input(Fore.GREEN + (',').join(list(cities.keys())) + ": ")
if selected_city not in cities:
    print(Fore.RED+ "Some times naive")
    exit()

print(Fore.WHITE+"Connecting DB...")
call(cities[selected_city].split(' '))
exit()


