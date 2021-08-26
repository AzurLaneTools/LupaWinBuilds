import sys

arch = sys.argv[1]

if arch == 'x86':
    print('Force 32 bit build')
    path = 'LuaJIT-2.1.0-beta3/src/Makefile'
    with open(path, 'r', -1, 'UTF8') as f:
        content = f.read()
    # Force a 32 bit build on a 64 bit OS.
    content = content.replace('CC= $(DEFAULT_CC)', 'CC= $(DEFAULT_CC) -m32')
    with open(path, 'w', -1, 'UTF8') as f:
        f.write(content)
