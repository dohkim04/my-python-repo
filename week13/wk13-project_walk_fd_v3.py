#!/usr/bin/env python3.10
import os # import os library to access to directory and file in operating system

# Initialization: Create an empty list and an empty dictionary.
file_list=[]
dict_of_list={}

#####################################################################
# Method 1: get_tree_directory
# This method traverse a directory tree and call get_file_list method
#####################################################################
def get_tree_directory(dir=os.getcwd()):
    for root, sub_dir_names, file_names in os.walk(dir):
        #Below is the code for testing purpose - list all sub directories and file names.  
        #print (f"{root},\n{sub_dir_names}, {file_names}") 
 
       
        if sub_dir_names == []: # In case there are no sub-directories under your current directory,                                
            each_file_list_per_each_dir = get_file_list(root, file_names, each_sub_dir='') # create a list of the path and the size of all the files under the current directory.
        #   The following block of codes turned into 'get_file_list' method. ###########
        #   print("This is the directory of ", os.path.join(root))
        #       for each_file in file_names:
        #       each_item = { 'path' : os.path.join(root, each_file), 'size' : os.path.getsize(os.path.join(root, each_file))}
        #       file_list.append(each_item)                 
        #       print(each_item, sep="\n")

        
        else:                                  # If there are sub-directories under your current directory,
            for each_sub_dir in sub_dir_names: # loop through each sub directory under your current directory.                
                each_file_list_per_each_dir = get_file_list(root, file_names, each_sub_dir) # create a list of the path and the size of all the files under each sub-directory.  
        #   The following block of codes turns into 'get_file_list' method. ###########
        #   print("This is the directory of ", os.path.join(root))
        #   for each_file in file_names:
        #       each_item = { 'path' : os.path.join(root, each_file), 'size' : os.path.getsize(os.path.join(root, each_file))}
        #       file_list.append(each_item)                 
        #       print(each_item, sep="\n")

    return file_list # the file_list list will be returned  


#####################################################################
# Method 2: get_file_list method
# -- It create a list of files under a directory the directory and the size of each file per directory.
# -- This method will be called recursively per eah sub directory by get_tree_directory method.
#####################################################################
def get_file_list(root, file_names, each_sub_dir):
    print("\n##############################################################")
    print(f'##### This is the directory of "{os.path.join(root,each_sub_dir)}"')
    for each_file in file_names:
        each_item = {'path' : os.path.join(root, each_sub_dir, each_file), 'size' : os.path.getsize(os.path.join(root,each_file))}
        file_list.append(each_item)
        print(each_item, sep="\n") # print each file item per line on computer screen.

    return file_list   ##### return the created file_list per each sub-directory. 


#####################################################################
# Method 3: search_file method
# -- This method passes the entry of user's directory pathway to get_tree_directory method.
# -- It also set up current working directory by default if no user arugmnet is entered. 
#####################################################################
#### search_file method (This is the function that set up a default directory path for no argument).
def search_file(dir = os.getcwd()): # if nothing is entered, use this default pathway.
    complete_file_list = get_tree_directory(dir)
    #print(complete_file_list) ##### this code is for testing purpose only
    return complete_file_list  ##### return a final version of a list of dictionary
    
    
#####################################################################
# Method 4: file_folder_dictionary method
# Receive user's arguments from command line.
# When user's arguments is not acceptable, show a warning message and stop the program.
#####################################################################
import sys # import system library to accept argument as input through user's command line

def file_folder_dictionary(argv): # receive a directory pathway as an argument
    # final_list_of_dict=[] ##### prepare for an empty list 
    
    ##### The following is for testing purpose only #####
    # sys.argv[0] indicates the first entry on your Linux command, "./wk13-project_walk_fd_v3.py"
    # therefore  your system argument values from index 1 a
    # for i in range(1, len(sys.argv)): 
    #    print('argument:', i, 'value:', sys.argv[i])
    
    ##### Execute user's command based on the status of user's arguments. 
    if len(sys.argv) >=3: # if more than 2 terms are entered, exit the program
        print("Please use only 1 complete directory pathway as an argument")     
        print("Try again.")
        sys.exit(2)
    if len(sys.argv) == 2: # if one argument is entered, pass the argument to search_file method
        return search_file(sys.argv[1]) ##### return the final version of a list of dictionary
    if len(sys.argv) == 1: # There is no argument entered 
        return search_file()            ##### return the final version of a list of dictionary
    
    ''' Output: 
    $ ./wk13-project_walk_fd_v3.py sdfsd sgd  sgd
    argument: 1 value: sdfsd
    argument: 2 value: sgd
    argument: 3 value: sgd
    Please use only 1 complete directory pathway as an argument
    Try again.

    $ ./wk13-project_walk_fd_v3.py sdfsd sgd 
    argument: 1 value: sdfsd
    argument: 2 value: sgd
    Please use only 1 complete directory pathway as an argument
    Try again.
    ''' 


#######################################################
##### Main function
##### This script will start to execute from this point
if __name__ == "__main__": # 
    result=file_folder_dictionary(sys.argv) # receive an argument from command line
    ## (example) 
    ## ./wk13-project_walk_fd_v3.py /home/dohyungkim2023/my-python-repo
    if result == []:
        print("You have entered an invalid directory pathway. Try again!")
        sys.exit(2)
    else:
        print("\n\n################################################\n")
        print("See the final version of a lits of dictionary below:\n\n\n", result)




##########################################################################################
##########################################################################################
##### The following codes were used for testing purpose for search_file() function #####
##### Test 1 #####
#print('Case 1: No parameter is given: executed "search_file()"')
#print("Please find a list of dictionaries\nAll the files and all the sub directories are reported: ")

#list_of_dict1 = search_file() # no parameter is given
#print("This is the end of 1st task")


###### Reintialization #####
#complete_file_list=[]
#file_list=[]

##### Test 2 #####
#print('Case 2: a directory path is given: executed "seaerch_file("/home/dohyungkim2023/my-python-repo/week13")"')
#print("Please find a list of dictionaries\nAll the files and all the sub directories are reported: ")

#list_of_dict2 = search_file("/home/dohyungkim2023/my-python-repo/week13") # parameter is given
#print("This is the end of 2nd task")

# Reintialization 
# complete_file_list=[]
# file_list=[]




