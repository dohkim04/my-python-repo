# Date: 04/09/2023
# Name: Do Hyung Kim

# Title: create a script generating a list of dictionaries about files
# This script file meet both requirements below:

# FOUNDATIONAL‌ REQUIREMENT 
# Create a script to that generates a list of dictionaries about files in the working directory. 
# Then print the list. Push your code to GitHub and include the link in your write up.

# ADVANCED REQUIREMENT
# Modify the script into a function such that any path can be passed as a parameter. 
# This parameter should be optional and should default to working directory when the variable is not passed. 
# The function should then create the list of dictionaries about files from that path. 
# The function should also return information on files nested in folders (recursive).

#########################################################################################################
#!/usr/bin/env python3.10
import os # access to directories and files in operating system

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
# -- It create a list of files including the pathway and the size of each file per (sub) directory
# -- This method will be called recursively by get_tree_directory method.
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
# -- This method passes the entry of user's directory pathway onto the get_tree_directory method.
# -- It set up your current working directory as default working directory if no arugmnet is provided. 
#####################################################################
#### search_file method (This is the function that set up a default directory path for no argument).
def search_file(dir = os.getcwd()): # if nothing is entered, use this default pathway.
    complete_file_list = get_tree_directory(dir)
    #print(complete_file_list) ##### this code is for testing purpose only
    return complete_file_list  ##### return a final version of a file list of dictionaries
    
    
#####################################################################
# Method 4: file_folder_dictionary method
# Determine whether received arguments are acceptable.
# Show a warning message and stop the program if the arguments are not acceptable
# Pass the arguments onto search_file method to initiate the creation of a file list of dictionaries 
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
    if result == []:
        print("No result found due to an invalid directory pathway. Try again.")
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




