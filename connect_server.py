# script to connect to aws server
import yaml
from colorama import Fore
from subprocess import call

data_path = "/Users/chen/lalamove/data/"

f = open(data_path + "server.yml")
o = yaml.load(f)

if len(o) == 1:
    selected_env = list(o.keys())[0]
else:
    selected_env = input(Fore.YELLOW + (',').join(list(o.keys())) + ": ", Fore.WHITE)
    if selected_env not in o:
        print(Fore.RED + "Too young")
        exit()

env = o[selected_env]
call(["itermocil", env['cert']])
exit()
