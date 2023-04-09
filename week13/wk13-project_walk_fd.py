#!/usr/bin/env python3.10
import os
path = "/home/dohyungkim2023/my-python-repo"
walkthrough=os.walk(path)
# looping through all exisitng files under the specific pathway

#for (root, sub_dir_names,file_names) in walkthrough:
#
#	for each_file in file_names:
#		print (root)
#

## looping through all sub directories
for root, sub_dir_names,file_names in os.walk(path):
	print (root, sub_dir_names, file_names)
	#for each_dir in sub_dir_names:
	#	print(os.path.join(root,each_dir))
		



