# Date: 04/07/2023
# Title: Week 13 project - creating a list of file and folder dictionary
'''
This is screen version of the script to satisfy Foundational and Advanced sections. ###
It will be used to create a new script genearating a list of dictionary.
'''

##########################################
# FOUNDATIONAL
# Create a script to that generates a list of dictionaries about files in the working directory. 
# Then print the list.
# Push your code to GitHub and include the link in your write up.
##########################################
# ADVANCED
# Modify the script into a function such that any path can be passed as a parameter. 
# This parameter should be optional and should default to working directory when the variable is not passed. 
# The function should then create the list of dictionaries about files from that path. 
# The function should also return information on files nested in folders (recursive).
##########################################
##########################################
# 0. Preparation: reviewed basic Python codes on how to retrieve the information on file and directories
# 
# os.getcwd() method: get the current directory pathway as initial starting folder.
# print(type(os.getcwd))  # <class 'str'>
# walk() method: generate the file names in a directory tree by walking the tree either top-down or bottom-up. the default is top-down.
# print(type(os.walk(os.getcwd() ))) # <class 'generator'>

##########################################
#!/usr/bin/env python3.10
#1. define a Python library for miscellaneous operating system interfaces
import os

file_list = []
file_dict = {}
#2. define a method to retrieve file and directory pathway per a given current directory
# Method [1]: get_dir_file() function 
# Per a user's file pathway input, generate the file names in a directory tree by walking the tree from top to bottom.
def get_dir_file(current_directory): # current_directory is a parameter of this method
    dir_tree_info= os.walk(current_directory)
    look_through_directory(dir_tree_info) # call look_through_directory() function

# Method [2]: using the above generated directory tree, loop through the entire directory and files recursively. 
def look_through_directory(dir_info): # dir_tree_info argument will be passed onto the parameter dir_info in this method   
    for root, sub_dir_names, file_names in dir_info: #   
        # print(f"The scanning directory is {root}{'/'}{sub_dir_names}.")
        if len(sub_dir_names) !=0: 
            for sub_dir_name in sub_dir_names:
                # print("We are now in a sub-directory:",os.path.join(root,sub_dir_name))
                # os.path.join(root,sub_dir_name))
                for each_file in file_names:
                    if os.path.isfile(each_file) == True:
                        print(f"{os.path.isfile(each_file)}, 'path' : {root}, {sub_dir_name}, {each_file}, 'size' : {os.path.getsize(each_file)}")
                        file_path = os.path.join(root,each_file)
                        file_size = os.path.getsize(each_file)
                        file_dict[file_path] = file_size
                        file_list.append({''})

###########################
#3. Ask user to enter a specific directory pathway to start with.
current_directory = input("Enter your directory patyway (your current working directory is set by default): ")
if len(current_directory) == 0:
    current_directory = os.getcwd() # default value will be set up as current working directory if nothing is entered
get_dir_file(current_directory)     # call get_dir_file function above (See #2. Method[1])


'''


# COMPLEX (Very Tricky)
# Modify the function to display recursive file information as dictionary of dictionaries.

'''