import os
cwd = os.getcwd()
name1 = os.path.dirname('C:\\Users\\jwilshire\\Documents\\GitHub\\Advanced-Python-Programming\\System-Tools\\text.txt')
name2 = os.path.dirname('/Users/jwilshire/Documents/GitHub/Advanced-Python-Programming/System-Tools/text.txt')
sep = os.sep  # the operating system specific directory seperator token
name3 = sep.join(['C:', 'Users', 'jwilshire', 'Documents', 'GitHub', 'Advanced-Python-Programming', 'System-Tools'])
name4 = os.path.join('Users', 'jwilshire', 'Documents', 'GitHub', 'Advanced-Python-Programming', 'System-Tools')
print(name1, name2, name4, sep ='\n')
print(cwd == name1)
print(cwd == name2)
print(cwd == name3)