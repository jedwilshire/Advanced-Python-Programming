import sys
print(sys.platform, sys.version)
if sys.platform.startswith('win'):
    print('You are using windows os')
else:
    print('This is not a windows os')
while True:
    resp = input('?')
    if len(resp) > 0 and resp.upper()[0] == 'Q':
        sys.exit()