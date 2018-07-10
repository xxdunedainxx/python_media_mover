import os
from datetime import datetime
import shutil
from conf.conf import GET_MEMORY_CMD,avail_byte_limit

from util.general import log_and_print,str_build_helper
from util.directory import check_dir, get_destination_memory, copy_over
from util.setup import TOTAL_BYTES_DESTINATION, ALL_FILES, target_dir_setup, SCRIPT_CONFIG,Log



def main(TOTAL_BYTES_DESTINATION, ALL_FILES, SCRIPT_CONFIG,Log):
	for directories_to_copy in ALL_FILES.keys():
		log_and_print(Log,"going through :: " + directories_to_copy)
		for file_to_copy in ALL_FILES[directories_to_copy]:
			dirs=file_to_copy.replace(directories_to_copy,"").split(SCRIPT_CONFIG['os_cmds']['os_directory_slash'])
			i=0

			# Build out destination directory on drive 
			dir_builder=""
			while i < len(dirs) - 1:
				check_dir(SCRIPT_CONFIG['directories']['destination_dir'] + SCRIPT_CONFIG['os_cmds']['os_directory_slash'] + dir_builder + dirs[i])
				dir_builder+=(dirs[i] + SCRIPT_CONFIG['os_cmds']['os_directory_slash'])
				i+=1
			TOTAL_BYTES_DESTINATION-=(int((os.path.getsize(file_to_copy))))
			# IF destination capacity met exit
			if TOTAL_BYTES_DESTINATION  < avail_byte_limit:
				log_and_print(Log,"Byte limit met for destination, exiting")
				exit(1)
			else:
				log_and_print(Log,"Current byte capacity at destination :: " + str(TOTAL_BYTES_DESTINATION))
				copy_over(file_to_copy, (SCRIPT_CONFIG['directories']['destination_dir'] + file_to_copy.replace(directories_to_copy,"") ))

if __name__ == "__main__":
	# Main Args::
	# Total bytes - track the byte memory capacity of the target directory to prevent overflow
	# ALL_FILES - all the files to be copied over
	# SCRIPT_CONFIG - configuration for script. For configuration key / values, please refer to ./conf/conf.py
	# Log - Log file stream 
	main(TOTAL_BYTES_DESTINATION, ALL_FILES,SCRIPT_CONFIG,Log)