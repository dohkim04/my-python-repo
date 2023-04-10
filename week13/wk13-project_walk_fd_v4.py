#!/usr/bin/env python3.10
import os # access to directories and files in operating system

# Date: 04/09/2023
# Name: Do Hyung Kim

# Title: create a script generating a list of dictionaries about files
# This script file meet both requirements below:

# COMPLEX (Very Tricky)
# Modify the function to display recursive file information as dictionary of dictionaries.

# Strategy:
# For Foundational and Advanced requirement, we created a list of dictionaries.
# Some groups of the files are under their shared directory pathways.
# For this complex requirement, use the shared file directory 
# {'shared pathway1':([file1, size1], [file2, size2], ...), shared pathway2:  }, 

#########################################################################################################
# Initialization: Create an empty list and an empty dictionary.
file_of_dict={}
dir_of_dict={}

#####################################################################
# Method 1: get_tree_directory
# This method traverse a directory tree and call get_file_list method
#####################################################################
def get_tree_directory(dir=os.getcwd()):
    for root, sub_dir_names, file_names in os.walk(dir):
        #Below is the code for testing purpose - list all sub directories and file names.  
        #print (f"{root},\n{sub_dir_names}, {file_names}") 
        if sub_dir_names == []: # In case there are no sub-directories under your current directory,                                
            each_file_dir_per_each_dir = get_file_list(root, file_names, each_sub_dir='') # create a list of the path and the size of all the files under the current directory.
        else:                                  # If there are sub-directories under your current directory,
            for each_sub_dir in sub_dir_names: # loop through each sub directory under your current directory.                
                each_file_dir_per_each_dir = get_file_list(root, file_names, each_sub_dir) # create a list of the path and the size of all the files under each sub-directory.  
    return dir_of_dict # the file_list list will be returned  


#####################################################################
# Method 2: get_file_list method
# -- It create a list of files including the pathway and the size of each file per (sub) directory
# -- This method will be called recursively by get_tree_directory method.
#####################################################################
def get_file_list(root, file_names, each_sub_dir):
    print(f'##### This is the directory of "{os.path.join(root,each_sub_dir)}"')
    for each_file in file_names:
        file_of_dict = {'file' : each_file, 'size' : os.path.getsize(os.path.join(root,each_file))}
        #dir_of_dict[os.path.join(root,each_sub_dir)] = file_of_dict
        print(file_of_dict, sep="\n") # print each file item per line on computer screen.
    dir_of_dict[os.path.join(root, each_sub_dir)] = file_of_dict
    return dir_of_dict   ##### return the created file_list per each sub-directory. 


#####################################################################
# Method 3: search_file method
# -- This method passes the entry of user's directory pathway onto the get_tree_directory method.
# -- It set up your current working directory as default working directory if no arugmnet is provided. 
#####################################################################
#### search_file method (This is the function that set up a default directory path for no argument).
def search_file(dir = os.getcwd()): # if nothing is entered, use this default pathway.
    complete_dir_of_dict = get_tree_directory(dir)
    #print(complete_file_list) ##### this code is for testing purpose only
    return complete_dir_of_dict  ##### return a final version of a file list of dictionaries
    
    
#####################################################################
# Method 4: file_folder_dictionary method
# Determine whether received arguments are acceptable.
# Show a warning message and stop the program if the arguments are not acceptable
# Pass the arguments onto search_file method to initiate the creation of a file list of dictionaries 
#####################################################################
import sys # import system library to accept argument as input through user's command line

def file_folder_dictionary(argv): # receive a directory pathway as an argument
    ##### Execute user's command based on the status of user's arguments. 
    if len(sys.argv) >=3: # if more than 2 terms are entered, exit the program
        print("Please use only 1 complete directory pathway as an argument")     
        print("Try again.")
        sys.exit(2)
    if len(sys.argv) == 2: # if one argument is entered, pass the argument to search_file method
        return search_file(sys.argv[1]) ##### return the final version of a list of dictionary
    if len(sys.argv) == 1: # There is no argument entered 
        return search_file()            ##### return the final version of a list of dictionary
    
#######################################################
##### Method 5: Main method
##### The exeucution of this Python script will start from and end at this method
##### Receive arguments from command line and pass them onto file_folder_dictionary method for processing
#######################################################
if __name__ == "__main__": 
    # receive an argument and pass it onto file_folder_dictionary method
    ## an examplary command line with an argument below: 
    ## ./wk13-project_walk_fd_v3.py /home/dohyungkim2023/my-python-repo
    # the outcome of the script will be saved into result variable in the format of a list of dictionaries format.
    result=file_folder_dictionary(sys.argv) 

    ## Print the list of dictionaries appropriately based on the status of the result.
    if result == {}:
        print("No result found due to an invalid directory pathway. Try again.")
        sys.exit(2)
    else:
        print("\n\n################################################\n")
        print("See the final version of a lits of dictionary below:\n\n\n", result)
