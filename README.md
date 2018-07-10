# Python Media Mover

Python media mover is a command line utility script, which can be used to migrate various media files off of one system and onto another. It can also be used to gather files of a specific type to a central target directory. 

Basically its for searching and copying over files :)

### Supported Environments:
	- Supports Python 2.xx.xx & 3.xx.xx
	- Supports Mac and Windows environments

### Configuration and set up: 
	- All Application configurations are stored in ./conf/conf.py, within the dict var SCRIPT_CONFIG. Various capabilities of the script can be modified directly here, or via the CLI when running app.py
	- Please note that the automation will STOP if the destination drives free space is lower than the number SCRIPT_CONFIG['avail_byte_limit']

### Install and run:
```sh
$ git clone
$ cd python_media_copier
$ python app.py
```

Once in the CLI, simply follow the prompts to continue with the automation

License
----
MIT

**If you have any issues or feedback please let me know!**