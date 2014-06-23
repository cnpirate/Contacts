import sys
import pickle as p

class contacts:
	def __init__(self, name, telephone, address):
		self.name = name
		self.telephone = telephone
		self.address = address
		

if len(sys.argv) < 2:
	print("No action!")
	sys.exit()

filename = "contacts.txt"
action = sys.argv[1]
print(action)
if action == "add":	
	name = sys.argv[2][:]
	telephone = sys.argv[3][:]
	address = sys.argv[4][:]
	# print(name)
	# print(telephone)
	# print(address)
	# person = contacts(name, telephone, address)
	fd = open(filename, "rb")
	dict = p.load(fd)
	print(dict)
	fd.close()
	
	dict[name] = [telephone, address]
	fd = open(filename, "wb")	
	p.dump(dict, fd)
	fd.close()
	
elif action == "del":
	# print(action)	
	name = sys.argv[2][:]
	fd = open(filename, "rb")
	dict = p.load(fd)
	del dict[name]
	fd.close()
	
	# dict[name] = [telephone, address]
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