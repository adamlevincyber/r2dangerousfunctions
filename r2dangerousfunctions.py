#!/usr/bin/python3

import r2pipe

r = r2pipe.open('OpenBTS.bin')
r.cmd("aaa")

badFunctions = ["sym.imp.strcpy", "sym.imp.strcat", "sym.imp.strncpy", "sym.imp.sprintf", "sym.imp.vsprintf", "sym.imp.scanf", "sym.imp.sscanf", "sym.imp.gets", "sym.imp.atoi", "sym.imp.atof", "sym.imp.atol", "sym.imp.execve", "sym.imp.system", "sym.imp.popen"]

functions = r.cmdj("aflj")

for f in functions:
    if f['name'] in badFunctions:
        print("Found dangerous function @ 0x0{:x} {}()".format(f['offset'], f['name']))
        
        addr = f['offset']
        locations = r.cmdj('axtj ' + str(addr))
        
        for x in locations:
            print('          Called @ 0x{:x} by {}()'.format(x['from'], x['fcn_name']))

r.quit()        