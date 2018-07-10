from util.general import log_and_print, str_build_helper
import os
import shutil

VISITED_DIRECTORIES=[]

def check_dir(d):
	try:
		if os.path.exists(d):
			return
		else:
			os.mkdir(d)
	except Exception as e:
		print(str(e))

def target_dir_setup(conf):
	check_dir(os.path.exists(conf['directories']['destination_dir']))

def get_destination_memory(conf):
	if conf['os_cmds']['os'].upper() == 'W':
		# Move to destination drive
		os.chdir(conf['directories']['destination_dir'])
		avail=os.popen(conf['os_cmds']['get_memory_cmd']).read().replace("\n","")
		# Go Back
		os.chdir(conf['directories']['home_dir'][0])
		print(avail)
		return int(avail)
	else: 
		avail=os.popen(conf['os_cmds']['get_memory_cmd']).read().split("\t")[0]
		return int(avail)


# TODO back slashing for mac vs windows 
# EDGE CASE DONT COPY IF TARGET DESTINATION IS NESTED IN SOURCE, INDIRECT RECURSION CASE 
def grab_directory_files(directory, conf,MEDIA_TYPES,Log):
	DIR=os.listdir(directory)
	files_in_dir=[]

	for f in DIR:
		print("===== CURRENT DIRECTORY ======" + directory)
		try:
			log_and_print(Log,str_build_helper(["Checking ", f]))
			
			if os.path.isdir(str_build_helper([directory,conf['os_cmds']['os_directory_slash'],f])) and str_build_helper([directory,conf['os_cmds']['os_directory_slash'],f]) not in VISITED_DIRECTORIES and str_build_helper([directory,conf['os_cmds']['os_directory_slash'],f]) != (conf['directories']['destination_dir']):

				VISITED_DIRECTORIES.append(str_build_helper([directory,conf['os_cmds']['os_directory_slash'],f]))
				log_and_print(Log,str_build_helper(["This is a directory ",directory,conf['os_cmds']['os_directory_slash'], f]))
				os.chdir(str_build_helper([directory,conf['os_cmds']['os_directory_slash'], f]))
				
				# RECURSIVE CALL 
				files_in_dir.extend(grab_directory_files(str_build_helper([directory,conf['os_cmds']['os_directory_slash'],f]), conf, MEDIA_TYPES,Log))
				
			elif not os.path.isdir(str_build_helper([directory,conf['os_cmds']['os_directory_slash'],f])):
				print("not a dir...?")
				if f[-3:].upper() in conf["general"]["media_types"] or f[-3:].lower() in conf["general"]["media_types"]:
					log_and_print(Log,str_build_helper(["This is an approved file ",directory,conf['os_cmds']['os_directory_slash'], f]))
					files_in_dir.append(str_build_helper([directory,conf['os_cmds']['os_directory_slash'],f]))
		except Exception as e:
			continue
	if directory is not conf['directories']['home_dir']:
		os.chdir("..")
	#print(files_in_dir)
	return files_in_dir

def copy_over(file_path, target_path):
	try:
		if os.path.exists(file_path):
			shutil.copyfile(file_path, target_path)
	except Exception as e:
		print(str(e))