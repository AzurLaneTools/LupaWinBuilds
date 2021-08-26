import sys
import lupa

arch = sys.argv[1]

lua = lupa.LuaRuntime()
lua.execute('require("test-%s")' % arch)
