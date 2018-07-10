import os

# Logging
LOG_DIR="./log/main.log"
Log=open(LOG_DIR,"a")
MEDIA_TYPES=["mp4","mp3","img", "jpg", "png","pdf", "tiff"]
GET_MEMORY_CMD=""
avail_byte_limit=5000

SCRIPT_CONFIG={
	'general' :{
		# Media types to be copied over
	 	'media_types' : ["mp4","mp3","img", "jpg", "png","pdf"],

	 	# Byte limit precaution amount 
	 	'avail_byte_limit' : 5000
	 },
	 'directories' : {
	 	# Various directories used by automation
	 	'original_script_directory' : os.getcwd(),
		'home_dir' : ['C:\\Users\\zach.mcfadden\\Downloads','C:\\Users\\zach.mcfadden\\Pictures'],
		'cur_dir' : '',
		'source_drive' : 'C:',
		'target_drive' : 'D:',
		'destination_dir' : 'C:\\Users\\zach.mcfadden\\Desktop\\test_target'
	},
	'os_cmds' : {
		'os' : '',
		'list_directory_cmd' : '',
		'get_memory_cmd' : '',
		'os_directory_slash' : ','
	},
	'directory_cachers': {
		'all_files' : [],
		'visited_directories' : []
	}
}