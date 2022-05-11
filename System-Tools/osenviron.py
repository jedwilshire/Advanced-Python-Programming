import os
#print(os.environ)  # too much information!  os.environ is a map
for key in os.environ:
    print(key)
print(os.environ['USERNAME'])
