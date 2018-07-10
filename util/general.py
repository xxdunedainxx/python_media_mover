from datetime import datetime

def log_and_print(Log,s):
	# Logging 
	Log.write(str(datetime.now()) +  " :: " + s + "\n")

	# CMD output
	print(s)

def str_build_helper(str_data):
	str_build=""
	for d in str_data:
		str_build+=str(d)
	return str_build

