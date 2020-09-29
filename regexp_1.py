import re
message = 'Call me 415-555-1011, or at 415-555-999'

phoneNumRegex = re.compile(r'\d\d\d\-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search(message)
print(mo.group())