"""
Registry Expressions
re is the regular expression module
re.compile method returns a 

pattern object

this object has a match() method. 
when match() compare succeeds,

**a match object is returned**

This object also has methods. start(),end() and group().

"""

from re import *
pattern = \
compile('(^|\s)[-a-z0-9_.]+@([-a-z-0-9]+\.)[a-z]{2,6}(\s|$)')
def get_address():
	address = input('enter your email address: ')
	is_valid = pattern.match(address)
	
	if is_valid:
		print('Valid Address:',is_valid.group())
	else:
		print('Invalid Address. Please Retry: \n')

get_address()
