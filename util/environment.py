from util.general import str_build_helper,log_and_print
import os
import sys

# python version specific attributes
# 2.7 support
if sys.version_info[0] == 2:
	user_input=raw_input
# 3+ support 
if sys.version_info[0] >=3:
	user_input=input
# end python specific attributes

def get_current_user_windows():
	return os.popen('echo %USERNAME%').read().replace("\n","")

# Method used for managing array of source directories 
def manage_source_directories(conf,Log):
	source_dir_action=""
	while source_dir_action.upper() != "Q":
		source_dir_action=user_input("Current directories to iterate( " + str(conf['directories']['home_dir']) + ") \nWould you like to remove a directory (R), add a directory (A), or Quit(Q):" )

		if source_dir_action.upper() == "R":
			index_to_remove=-1
			i=0
			output_builder="Current Directories:\n"
			while i < len(conf['directories']['home_dir']):
				output_builder+=("[" + str(i) + "]" + conf['directories']['home_dir'][i] + "\n")
				i+=1
			output_builder+="Please specify an index to remove from the list:"
			index_to_remove=user_input(output_builder)

			if int(index_to_remove) < 0 or int(index_to_remove) >= len(conf['directories']['home_dir']):
				print("index out of range!")
			else:
				conf['directories']['home_dir'].pop(int(index_to_remove))

		elif source_dir_action.upper() == "A":
			directory_to_add=user_input("Provide a VALID directory to add:")

			if os.path.isdir(directory_to_add):
				conf['directories']['home_dir'].append(directory_to_add)
			else:
				print("invalid directory provided!")
		elif source_dir_action.upper() == "Q":
			if len(conf['directories']['home_dir']) < 1:
				print("Cant quit unless you have at least one directory to loop through!")
				source_dir_action="N/A"
			else:
				return
		else:
			print("invalid input provided!")

def SETUP_WINDOWS_ENV(conf,Log):
	log_and_print(Log,"PREPPING FOR WINDOWS ENVIRONMENT")

	conf['directories']['home_dir'].append(str_build_helper(["C:\\Users\\",get_current_user_windows()]))

	override_homedir=user_input("This is the current directory to be copied : " + str(conf['directories']['home_dir'] ) + ". Would you like to override this(You may add or remove more directories to loop through)?[Y/N]")

	if override_homedir == 'Y' or override_homedir == 'y':
		manage_source_directories(conf,Log)

	log_and_print(Log,"directories :: " + str(conf['directories']['home_dir'] ))

	# Change dir to home dir
	# os.chdir(str_build_helper([ conf['directories']['home_dir']]))

	log_and_print(Log,str_build_helper(["Current Directory : ", os.getcwd()]))

	conf['os_cmds']['get_memory_cmd']="powershell \"" +  conf['directories']['original_script_directory'] + "/util/win/get_drive_memory.ps1\" -drive \"" + conf['directories']['destination_dir'].split(":")[0] + "\""

	conf['os_cmds']['os_directory_slash']="\\"
# SUM OF MEMORY : powershell for windows (Get-ChildItem -Recurse | Measure-Object -Sum Length).sum


def SETUP_MAC_ENV(conf, Log):
	from os.path import expanduser
	log_and_print(Log,"PREPPING FOR MAC ENVIRONMENT")

	conf['directories']['home_dir']=expanduser("~")

	override_homedir=user_input("This is the current directory to be copied : " + str(conf['directories']['home_dir'] ) + ". Would you like to override this(You may add or remove more directories to loop through)?[Y/N]")

	if override_homedir == 'Y' or override_homedir == 'y':
		manage_source_directories(conf,Log)

	log_and_print(Log,"directories :: " + str(conf['directories']['home_dir'] ))

	# Change dir to home dir
	# os.chdir(str_build_helper([ conf['directories']['home_dir']]))

	log_and_print(Log,str_build_helper(["Current Directory : ", os.getcwd()]))

	conf['os_cmds']['get_memory_cmd']="du -s " + conf['directories']['home_dir']
	conf['os_cmds']['os_directory_slash']="/"


def SETUP_ENV(conf,Log, env):
	if env.upper() == 'M':
		SETUP_MAC_ENV(conf, Log)
	elif env.upper() == 'W':
		SETUP_WINDOWS_ENV(conf,Log)
	else:
		raise Exception("Invalid environment provided")

def cmd_input(conf):
	print("## Welcome to the python media copy program ##")
	print("## This program will copy over specified contents of a computer, to a target external drive ##")
	print("## Current files to copy : " + str(conf["general"]["media_types"]))
	print("## Destination directory : " + conf["directories"]["destination_dir"])

	override_destination=user_input("Would you like to override the destination directory?[Y/N]:")
	if override_destination.upper() == 'Y':
		conf['directories']['destination_dir']=user_input("Please provide a new destintion:")
	override_media_types=user_input("Would you like to override media types?[Y/N]:")

	if override_media_types.upper() == 'Y':
		new_media_types=user_input("Please provide a comma seperated list of media extensions to look through(EX: .mp3, .jpg, .img:")
		conf["general"]["media_types"]=new_media_types.split(",")

	windows_or_mac=user_input("Is this a mac or windows system?[M/W]:")
	conf['os_cmds']['os']=windows_or_mac

	return windows_or_mac