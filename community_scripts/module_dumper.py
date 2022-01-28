import sys, os, chat
chat.AppendChat(3,"[STMOD] - |cffffc700|H|h Module dumper: Try to dump modules.")
f = open('dumped_modules.txt','w')
modules_key = sys.modules.keys()
modules_dic = sys.modules
built_in = sys.builtin_module_names
for mod in modules_key:
    if mod not in built_in:
        print >>f,'\nModule:',str(mod), str('\n')
        funcs = dir(modules_dic.get(mod))
        for func in funcs:
            print >>f,str(func)
			
chat.AppendChat(3,"[STMOD] - |cffffc700|H|h Module dumper: dumped into path: " + str(os.path.realpath(f.name)))
f.close()
chat.AppendChat(3,"[STMOD] - |cffffc700|H|h Module dumper: Finished dumping modules.")
try:
	os.startfile("dumped_modules.txt")
except:
	pass
