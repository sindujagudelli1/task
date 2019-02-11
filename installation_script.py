import json
import subprocess
import sys

def install(dependency_list):
	for package in dependency_list:
		subprocess.call([sys.executable, "-m", "pip", "install", package])

			

def get_dependency_string(dependency_string):
	brackets_stack = 0
	temp_dependency_string = ""
	for char in dependency_string:
		if char == '{':
			brackets_stack += 1
			continue;
		if char == '}':
			brackets_stack -= 1
			continue;
		if brackets_stack == 2 and char != '\n' and char != '\t':
			temp_dependency_string += char
	return temp_dependency_string

def get_dependency_list(dependency_string):
	return dependency_string.split(",")

if __name__ == "__main__":
	# data = []
	dependency_file = ""
	with open('dependencies.json') as filehandle:
		for line in filehandle:
			dependency_file += line

	dependency_string = get_dependency_string(dependency_file)
	dependency_list = get_dependency_list(dependency_string)

	install(dependency_list)
	print "Success!!"