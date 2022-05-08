
import re
start_end_same='^[a-zA-Z][a-zA-Z0-9]*[a-zA-Z]$'
having_white_space='^(.*\s+.*)+$'
no_white_space='^\s*\S+\s*$'    

string =""

re.findall(start_end_same,string)
re.findall(having_white_space,string)
re.findall(no_white_space,string)