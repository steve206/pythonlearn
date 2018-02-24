"""Manipulating Strings.
docstrings

strings in python are just a list 
with individual characters elements
in the list.

As with other lists, the elements
(characters) can be referenced 
by their index number.
"""

def display(s):
	'''Display an argument value'''
	print(s)

display(display.__doc__)

display(r'C:\program files')
display('\nHello'+ 'Python')
display('Python in Easy Steps\n'[10:])
display('P'in 'Python')
display('p' in 'Python')

