import os
from conf.conf import Log, SCRIPT_CONFIG, MEDIA_TYPES
from util.directory import grab_directory_files, target_dir_setup, get_destination_memory
import util.environment as ENV
from util.general import log_and_print

# Files to loop through and copy 
ALL_FILES={}

# User CMD Input for automation config
windows_or_mac=ENV.cmd_input(SCRIPT_CONFIG)

# Environment specific set up
ENV.SETUP_ENV(SCRIPT_CONFIG, Log, windows_or_mac)

# Target directory configuration 
target_dir_setup(SCRIPT_CONFIG)

# Gather all file paths to copy 
for source_directory in SCRIPT_CONFIG['directories']['home_dir']:
	if os.path.isdir(source_directory):
		print(ALL_FILES)
		print("source dir :: " + source_directory)
		print("working dir :: " + os.getcwd())
		os.chdir(source_directory)
		ALL_FILES[source_directory]=(grab_directory_files(source_directory,SCRIPT_CONFIG, MEDIA_TYPES, Log))
	else:
		log_and_print(Log,source_directory + " is not a valid DIRECTORY ")
log_and_print(Log, "Finish grabbing all files")

# Trace byte usage to ensure we dont overflow on memory
TOTAL_BYTES_DESTINATION=int(get_destination_memory(SCRIPT_CONFIG))
log_and_print(Log, "Total bytes in destination:: " + str(TOTAL_BYTES_DESTINATION))