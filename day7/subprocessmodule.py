import subprocess
from pprint import pprint
p=subprocess.check_output(["dir"],shell=True)
pprint(p)