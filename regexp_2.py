import re

batRegex = re.compile(r'Bat(wo)?man') # Zero or one times
batRegex = re.compile(r'Bat(wo)*man') # Zero or more times
batRegex = re.compile(r'Bat(wo)+man') # One or more times
haRegex = re.compile(r'(Ha){3,5}') # Number of times of repitition