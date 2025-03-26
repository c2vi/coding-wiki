


def main():

	import sys

	args = sys.argv[1:]

	if args[0] == "insert":

		if args[1] == "python":
			from main.insert import insert_python
			insert_python()

	elif args[0] == "ss" or args[0] == "simplesearch" or args[0] == "ssearch":
		from main.search import simple_search
		print(simple_search(args[1],args[2],args[3],args[4]))

	else:
		print("Wrong Argument")



