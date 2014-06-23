import sys
import os
import pickle as p

if len(sys.argv) < 2:
	print("No action is defined!")
	sys.exit()
elif len(sys.argv) == 2 :
	print("Too few parameters!")
	sys.exit()
	
filename = "contacts.txt"
action = sys.argv[1]
dict = {}
if action == "add":
	if len(sys.argv) == 3:
		print("Too few parameters")
		sys.exit()
		
	name = sys.argv[2][:]
	info = sys.argv[3:]
	
	if os.path.isfile(filename):
		try:
			fd = open(filename, "rb")
			dict = p.load(fd)
			fd.close()		
			dict[name] = info
			fd = open(filename, "wb")	
			p.dump(dict, fd)
			fd.close()
		except EOFError:
			dict[name] = info
			fd = open(filename, "wb")	
			p.dump(dict, fd)
			fd.close()
		
	else:
		dict[name] = info
		fd = open(filename, "wb")	
		p.dump(dict, fd)
		fd.close()
	print("Succeed.")
	
elif action == "del":
	name = sys.argv[2][:]
	try:
		fd = open(filename, "rb")
		dict = p.load(fd)
		del dict[name]
		fd.close()
		fd = open(filename, "wb")	
		p.dump(dict, fd)
		fd.close()
		print("Succeed.")
		
	except EOFError:
		print("contacts is null!")
		sys.exit()
		
	except KeyError:
		errorInfo = '"%s" is not in the contacts.' % (name)
		print(errorInfo)
		sys.exit()
	
elif action == "find":
	name = sys.argv[2][:]
	try:
		fd = open(filename, "rb")
		dicta = p.load(fd)
		print(dicta[name])
		fd.close()
		
	except EOFError:
		print("contacts is null!")
		sys.exit()
		
	except KeyError:
		errorInfo = '"%s" is not in the contacts.'
		print(errorInfo)
		sys.exit()
	
else:
	print("Wrong action!")
	sys.exit()