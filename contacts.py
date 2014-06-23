import sys
import os
import pickle as p

if len(sys.argv) < 2:
	print("No action!")
	sys.exit()

filename = "contacts.txt"
action = sys.argv[1]
dict = {}
print(action)
if action == "add":	
	name = sys.argv[2][:]
	info = sys.argv[3:]
	if os.path.isfile(filename):
		fd = open(filename, "rb")
		dict = p.load(fd)
		fd.close()
		
		dict[name] = info
		fd = open(filename, "wb")	
		p.dump(dict, fd)
		fd.close()
	else:
		dict[name] = info
		fd = open(filename, "wb")	
		p.dump(dict, fd)
		fd.close()
	
elif action == "del":
	name = sys.argv[2][:]
	fd = open(filename, "rb")
	dict = p.load(fd)
	del dict[name]
	fd.close()

	fd = open(filename, "wb")	
	p.dump(dict, fd)
	fd.close()
	
elif action == "find":
	# print(action)
	name = sys.argv[2][:]
	fd = open(filename, "rb")
	dicta = p.load(fd)
	print(dicta[name])
	fd.close()
	
else:
	print("Wrong action!")
	sys.exit()