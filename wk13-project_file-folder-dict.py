# Date: 04/07/2023
# Title: Week 13 project - creating a list of file and folder dictionary

# FOUNDATIONAL
# Create a script to that generates a list of dictionaries about files in the working directory. 
# Then print the list.
# Push your code to GitHub and include the link in your write up.

##########################################

#!/usr/bin/env python3.7
# define a Python library for operating system, 'os'
import os

# Basic Python code review on how to retrieve file and directory 
current_directory = os.getcwd() # get current directory pathway as string value.
dir_name = os.path.dirname(current_directory) # (current_directory)
base_name = os.path.basename(current_directory)
print (dir_name, base_name)


current_directory = os.getcwd()
print(type(current_directory))          # <class 'str'>
print(type(os.walk(current_directory))) # <class 'generator'>



def get_dir_file(current_directory):
    dir_info= os.walk(current_directory)
    for root, sub_dir_names, file_names in dir_info: # walk() method generates the file names in a directory tree by walking the tree either top-down or bottom-up.
        for sub_dir_name in sub_dir_names:
            for each_file in file_names:
                if os.path.isfile(each_file) == True:
                    print(f"{os.path.isfile(each_file)}, 'path' : {root}, {sub_dir_name}, {each_file}, 'size' : {os.path.getsize(each_file)}")


get_dir_file(current_directory)


'''
##########################################
# ADVANCED
# Modify the script into a function such that any path can be passed as a parameter. 
# This parameter should be optional and should default to working directory when the variable is not passed. 
# The function should then create the list of dictionaries about files from that path. 
# The function should also return information on files nested in folders (recursive).

# COMPLEX (Very Tricky)
# Modify the function to display recursive file information as dictionary of dictionaries.

'''