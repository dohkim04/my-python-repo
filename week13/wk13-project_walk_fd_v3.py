#!/usr/bin/env python3.10
import os

# Initialization: Create an empty list and an empty dictionary
file_list=[]
dict_of_list={}

#####################################################################
# Method 1: get_tree_directory
# This method traverse a directory tree and call get_file_list method
#####################################################################
def get_tree_directory(dir=os.getcwd()):
    for root, sub_dir_names, file_names in os.walk(dir):
        #Below is the code for testing purpose - list all sub directories and file names  
        #print (f"{root},\n{sub_dir_names}, {file_names}") 
 
       
        if sub_dir_names == []: # In case there are no sub-directories under your current directory,                                
            each_file_list_per_each_dir = get_file_list(root, file_names, each_sub_dir='') # create a list of the path and the size of all the files under the current directory.
        #   The following block of codes turned into 'get_file_list' method ###########
        #   print("This is the directory of ", os.path.join(root))
        #       for each_file in file_names:
        #       each_item = { 'path' : os.path.join(root, each_file), 'size' : os.path.getsize(os.path.join(root, each_file))}
        #       file_list.append(each_item)                 
        #       print(each_item, sep="\n")

        
        else:                                  # If there are sub-directories under your current directory,
            for each_sub_dir in sub_dir_names: # loop through each sub directory under your current directory.                
                each_file_list_per_each_dir = get_file_list(root, file_names, each_sub_dir) # create a list of the path and the size of all the files under each sub-directory.  
        #   The following block of codes turns into 'get_file_list' method ###########
        #   print("This is the directory of ", os.path.join(root))
        #   for each_file in file_names:
        #       each_item = { 'path' : os.path.join(root, each_file), 'size' : os.path.getsize(os.path.join(root, each_file))}
        #       file_list.append(each_item)                 
        #       print(each_item, sep="\n")

    return file_list # the file_list list will be returned  


#####################################################################
# Method 2: get_file_list method
# It create a list of dictionary containing the directory and the size of each file per directory.
# This method will be called recursively per each sub directory from get_tree_directory method.
#####################################################################
def get_file_list(root, file_names, each_sub_dir):
    print("This is the directory of ", os.path.join(root,each_sub_dir))
    for each_file in file_names:
        each_item = {'path' : os.path.join(root, each_file), 'size' : os.path.getsize(os.path.join(root, each_file))}
        file_list.append(each_item)
        print(each_item, sep="\n") # print each file item per line on computer screen

    return file_list # return the created file_list per each sub-directory. 


'''   
    working_path = input("Enter the working directory pathway: ") # /home/dohyungkim2023/my-python-repo"
    if working_path == '':
        working_path = os.getcwd()        
'''


def search_file(dir = '/home/dohyungkim2023/my-python-repo'):
    complete_file_list = get_tree_directory(dir)
    print(complete_file_list)
    

##### The following codes test search_file method #####
##### Test 1 #####
print('Case 1: No parameter is given: executed "search_file()"')
print("Please find a list of dictionaries\nAll the files and all the sub directories are reported: ")

search_file() # no parameter is given
print("This is the end of 1st task")


###### Reintialization #####
complete_file_list=[]
file_list=[]

##### Test 2 #####
print('Case 2: a directory path is given: executed "seaerch_file("/home/dohyungkim2023/my-python-repo/week13")"')
print("Please find a list of dictionaries\nAll the files and all the sub directories are reported: ")

search_file("/home/dohyungkim2023/my-python-repo/week13") # parameter is given
print("This is the end of 2nd task")

# Reintialization 
# complete_file_list=[]
# file_list=[]




