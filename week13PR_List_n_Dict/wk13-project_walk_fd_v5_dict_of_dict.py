#!/usr/bin/env python3.10
import os # access to directories and files in operating system
import sys # accept argument as input from user through Linux command line. ==> Method 4 and 5.
#############################################################################
# Date: 04/10/2023                                                          #
# Name: Do Hyung Kim                                                        #
##############################################################################################################
# Title: create a script generating a dictionary of dictionaries about files                                 #
# This script was modified from the previous ver 4. program meeting FOUNDATIONAL AND ADVANCED REQUIREMENTS   #
# This script file meets COMPLEX REQUIREMENT shown below: This is the ver 5. program                         #
# This script can print and create all the dictionaries with no files as well.                               #   
##############################################################################################################
# FOUNDATIONAL‌ REQUIREMENT 
# Create a script to that generates a list of dictionaries about files in the working directory. 
# Then print the list. Push your code to GitHub and include the link in your write up.
#
# ADVANCED REQUIREMENT
# Modify the script into a function such that any path can be passed as a parameter. 
# This parameter should be optional and should default to working directory when the variable is not passed. 
# The function should then create the list of dictionaries about files from that path. 
# The function should also return information on files nested in folders (recursive).
#
# COMPLEX REQUIREMENT (Very Tricky)
# Modify the function to display recursive file information as dictionary of dictionaries.
##############################################################################################################
# Initialization: create an empty dictionary.
# this is used to create a finalized dictionary of dictionaries about files.
dict_of_dict={} 

#####################################################################
# Method 1: get_tree_directory
# -- This method traverses an entire directory tree under your current working directory.
# -- Call "get_file_dict() method" to receive each individual dictionary of dictionaries.
# -- Create a fianlized dictionary of dictionaries and return it to "search_file() method".
#####################################################################
def get_tree_directory(dir=os.getcwd()):
    for root, sub_dir_names, file_names in os.walk(dir): 
    # per each loop, walk() function will traverse all the sub directories,
    # and all the files under your current working directory recursively. 
        # create and initialize "each_item_dict" as an empty dictionary.
        each_item_dict={} 

        # create a big single dictionary of multiple file dictionaries per your current directory.
        # (example)  
        # {'file: <file_name1>': 'size: <file_size1>', 'file: <file_name2>': 'size: <file_size2>', ...}
        each_item_dict = get_file_dict(root, file_names)  
        
        # create a gigantic "dict_of_dict" dictionary by setting up the 'key' as your current directory path,
        # and the 'value' with the above "each_item_dict" dictionaries per your current directory. 
        # (example)
        #   {'<shared-directory_a>': {'file: <file_name_a1>': 'size: <file_size_a1>', 'file: <file_name_a2>': 'size: <file_size_a2>', ...},
        #    '<shared_directory_b>': {'file: <file_name_b1>', 'size: <file_size_b1>', 'file: <file_name_b2>', 'size: <file_size_b2>', ...}, ...} 
        dict_of_dict[os.path.join(root)] = each_item_dict 
        #print(dict_of_dict) # this code is only for tesing purpose and checks whether a dictionary of dictionary is correctly created. 
    
    return dict_of_dict ##### return the finalized dictionary of dictionaries to search_file() method. #####


#####################################################################
# Method 2: get_file_list method
# -- It create a dictionary of files including the pathway and the size of each file per (sub) directory.
# -- If no files are present under a current directory, show a complete pathway.
# -- This method will be called recursively by get_tree_directory method.
# -- return each single dictionary of multiple file dictionaries to "get_tree_dictionary() method". #####
#####################################################################
def get_file_dict(root, file_names):
    each_item = {} # initialize each_item as an empty dictionary to accept a new single dictionary.
    print(f'##### This is the directory of "{os.path.join(root)}"') # display your current directory.
    
    # if no files are present in your current directory, 
    # set the key as the current directory path and the value as "0 file exists".
    # (example) {'path: <directory_path>': 'size: N/A - 0 file exists'}
    if len(file_names) == 0: 
        each_item[f"path: {os.path.join(root)}"]= f"size: N/A - {len(file_names)} file exists"
        #each_item[f"file: N/A "]= f"size: N/A"  ##### this can be used as an alternate input. 
    else:
        for each_file in file_names:
        #   The following "if case" block execution was ignored with the following output: "'/home/dohyungkim2023/my-python-repo/.git/objects': {}".
        #   if each_file=={}:
        #       each_item[f"file: no files are present"]=f"size: Not Applicable"
        #   else:
            
            # create an "each_item" single dictionary consisting of the name and the size of each file present under your current directory:
            # (example)  {'file: <file_name1>', 'size: <file_size1>'}
            # add up the above single dictionary to "each_item" dictionary
            each_item[f"file: {os.path.join(each_file)}"]= f"size: {os.path.getsize(os.path.join(root,each_file))}"                
    print(each_item, sep="\n") # print the "each_item" single dictionary containing the multiple file dictionaries above.
    return each_item      ###### return each single dictionary of multiple file dictionaries to "get_tree_dictionary" method. #####


#####################################################################
# Method 3: search_file method
# -- This method passes the entry of user's directory pathway onto the get_tree_directory method.
# -- It set up your current working directory as default working directory if no arugmnet is provided.
# -- Return a complete dictionary of dictionaries to "file_folder_dictionary() method" 
#####################################################################
#### search_file method (This is the function that set up a default directory path for no argument).
def search_file(dir = os.getcwd()): # if nothing is entered, use this default pathway.
    complete_dict_of_file_dict = get_tree_directory(dir)
    #print(complete_file_dict) ##### this code is for testing purpose only
    return complete_dict_of_file_dict  ##### return a complete dictionary of dictionaries to "file_folder_dictionary() method". #####
    
    
#####################################################################
# Method 4: file_folder_dictionary method
# -- Determine whether received arguments are acceptable.
# -- Show a warning message and stop the program if the arguments are not acceptable
# -- Pass the arguments onto search_file method to initiate the creation of a file list of dictionaries 
# -- receive the dictionary of dictionaris from search_file() method and return it to "main() method".
#####################################################################
# import sys 
# Python system library 'sys' is used to accept argument as input from user through Linux command line.

def file_folder_dictionary(argv): # receive a directory pathway as an argument
    # final_list_of_dict=[] ##### prepare for an empty list 
    
    ##### The following is for testing purpose only #####
    # sys.argv[0] # indicates the first entry on your Linux command, "./wk13-project_walk_fd_v3.py"
    # therefore  your system argument values from index 1 a
    # for i in range(1, len(sys.argv)): 
    #     print('argument:', i, 'value:', sys.argv[i])
    
    ##### Execute user's command based on the status of user's arguments. 
    if len(sys.argv) >=3: # if more than 2 terms are entered, exit the program
        print("Please use only 1 complete directory pathway as an argument")     
        print("Try again.")
        sys.exit(2)
    if len(sys.argv) == 2: # if one argument is entered, pass the argument to search_file method
        return search_file(sys.argv[1]) ##### return the final version of a list of dictionary
    if len(sys.argv) == 1: # There is no argument entered 
        return search_file()            ##### return the final version of a list of dictionary
    
    ''' 
    Output: 
    
    ~/my-python-repo$ week13/wk13-project_walk_fd_v4_rev1.py sdfsd sgd sgd
    argument: 1 value: sdfsd
    argument: 2 value: sgd
    argument: 3 value: sgd
    Please use only 1 complete directory pathway as an argument
    Try again.

    ~/my-python-repo$ week13/wk13-project_walk_fd_v4_rev1.py sdfsd sgd
    argument: 1 value: sdfsd
    argument: 2 value: sgd
    Please use only 1 complete directory pathway as an argument
    Try again.
    ''' 


#######################################################
# Method 5: Main method
# -- The exeucution of this Python script will start from and end at this method
# -- Receive arguments from command line and pass them onto file_folder_dictionary method for processing
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
        print("See the final version of a dict of dict below:\n\n\n", result)


#################################################################
##### Output - print and create a file list of dictionaries #####
'''
[Case 1] Execute the script with no argument on Linux command line

~/my-python-repo$ week13/wk13-project_walk_fd_v4_rev1.py 
##### This is the directory of "/home/dohyungkim2023/my-python-repo"
{'file: testing-functions.py': 'size: 4248', 'file: string-info.py': 'size: 2679', 'file: scopes.py': 'size: 2292', 'file: .gitignore': 'size: 1799', 'file: fizz-buzz.py': 'size: 1121', 'file: py-if-elif-else.py': 'size: 1397', 'file: using-dictionaries.py': 'size: 6584', 'file: README.md': 'size: 152', 'file: find_string.py': 'size: 1006', 'file: split&join_again.py': 'size: 1930', 'file: scope2.py': 'size: 1444', 'file: fizz-buzz-item.py': 'size: 1203', 'file: wk13-Mon-lesson-04032023.py': 'size: 6904', 'file: using-list.py': 'size: 4017', 'file: variations.py': 'size: 3297', 'file: Hello_world.py': 'size: 53', 'file: Hello_yourname.py': 'size: 1080', 'file: using-generator.py': 'size: 2540'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git"
{'file: index': 'size: 2288', 'file: HEAD': 'size: 30', 'file: packed-refs': 'size: 46', 'file: config': 'size: 263', 'file: description': 'size: 73', 'file: FETCH_HEAD': 'size: 102', 'file: COMMIT_EDITMSG': 'size: 51', 'file: ORIG_HEAD': 'size: 41'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/branches"
{'path: /home/dohyungkim2023/my-python-repo/.git/branches': 'size: N/A - 0 file exists'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/hooks"
{'file: fsmonitor-watchman.sample': 'size: 4655', 'file: push-to-checkout.sample': 'size: 2783', 'file: update.sample': 'size: 3650', 'file: pre-applypatch.sample': 'size: 424', 'file: pre-push.sample': 'size: 1374', 'file: pre-receive.sample': 'size: 544', 'file: pre-merge-commit.sample': 'size: 416', 'file: applypatch-msg.sample': 'size: 478', 'file: pre-commit.sample': 'size: 1643', 'file: prepare-commit-msg.sample': 'size: 1492', 'file: commit-msg.sample': 'size: 896', 'file: post-update.sample': 'size: 189', 'file: pre-rebase.sample': 'size: 4898'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects"
{'path: /home/dohyungkim2023/my-python-repo/.git/objects': 'size: N/A - 0 file exists'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/49"
{'file: 643f1f2687790aa54b9c066a5c303e7b530f0e': 'size: 162'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/52"
{'file: 8b11654c973a9fd1d30cca7746b1989a84d0aa': 'size: 280'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/c5"
{'file: 65835127d3055fd14927dd5644cca075b84dbb': 'size: 165'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/7d"
{'file: 287af85a3a917e3ae6f4085b44e45d5e9b3e5f': 'size: 186', 'file: 928b1ee8ddcdd4d2de61219b9d48190e57f26d': 'size: 517'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/e3"
{'file: 3d9011c1307a3d6eceb5a796be9a7121fcb329': 'size: 1364', 'file: e83ecd35e8f75eca5b4400a320ad0c27cf0ec4': 'size: 177'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/7c"
{'file: 68f4aafcb40a040100f86f122148d1765c1abd': 'size: 190'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/ad"
{'file: 0bfc9860c05866da5cb074379abb189a3f38d8': 'size: 746'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/a2"
{'file: b1fde369283c0aae5847fba2e635d666112091': 'size: 588'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/44"
{'file: e91f48ddd90ca5b30ca4b6d07f3b48fcc496ab': 'size: 1115'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/3e"
{'file: 02c256775bfba9516bdb6a69f2dea5e0d54399': 'size: 517'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/30"
{'file: bdfd802123c72180ef2a02dc80b729be4b84ca': 'size: 174'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/f5"
{'file: b1518f34f1473117f1170e96e86345190c8d33': 'size: 188'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/5b"
{'file: b4097d5112118577f618488f29e59fa1990241': 'size: 189', 'file: 836af98a0821787f2a7b8292535a27cc6d088c': 'size: 467'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/b4"
{'file: fd8f400b07573940da882f5f1f69856057be3e': 'size: 552'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/b0"
{'file: db908dc9b902458ca3619f65bbf31c0174c3d1': 'size: 773', 'file: ec75214984034f96d9d20ccab1a475a83aca7e': 'size: 1508'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/8c"
{'file: 00630e0e4ba8ff1395ab48258f738e9aa99af9': 'size: 16132'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/51"
{'file: ffc52f125dbfefa6669a2371b39ff0c76b1695': 'size: 175'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/a8"
{'file: b4964f6c3a87f27faab9bd670656957ab01fa8': 'size: 12428', 'file: 5225a0ce546492e8138a283873e50512268044': 'size: 646', 'file: 4021b0641b86c33c748a40f0a3517e182486da': 'size: 757'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/bd"
{'file: 3aba3c41e36b11d0605ee91f2b8940950f65aa': 'size: 195', 'file: 43c57c4f276dff983b3fa1eea25b63413fcd11': 'size: 192'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/6b"
{'file: 426a519a7a65f7aef9bfa9a60f7200ac7e2124': 'size: 274'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/55"
{'file: 189ea76ed6d6f154245f467346675d966916fd': 'size: 1187', 'file: 48d1e3a25e1ab5793b8651d894f29296cee398': 'size: 186'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/86"
{'file: 0c00594ae75ca8ec2f1ecbc21dd1b06bff69b4': 'size: 645'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/df"
{'file: fca6d33fde52fb73d66cb2cec201641fb22a8c': 'size: 5616'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/8b"
{'file: 9201506d17e10935cab341abf3403fc0fab1df': 'size: 192'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/07"
{'file: 081d9d3778d79f8358839d337d7362bfc1fa4d': 'size: 168'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/15"
{'file: 1309920de6d161f251f4f527f2e2ba5a784d53': 'size: 372', 'file: a1d717d75979fd412b3faed51f4cb34740c2dc': 'size: 713', 'file: 5b7a5fd67e2c460966144abbc3d673f63fc4cf': 'size: 12396'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/1e"
{'file: 3caea0585fc90c7f1d1a4cd9a6b0b1619a1336': 'size: 460'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/79"
{'file: b04af55b52006dd4e77e9f7b1c58690601e941': 'size: 548', 'file: a221e97a644a94d2a290fff52607c5514cebef': 'size: 12030'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/bb"
{'file: 1ba790a3ca1a2de7cdccb5942617e1ace6bd58': 'size: 181'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/24"
{'file: 206c4d129cc3ca3fa03aa204a14de820609e02': 'size: 879'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/6a"
{'file: a6d559918d3a22f38b8628f9a685bcd720b90e': 'size: 1425'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/3b"
{'file: fba49af95e18b2a96a64661c7b7c5a043733cb': 'size: 339', 'file: a1ec3f81e9f27ef1a03bf64ba7863033c9807b': 'size: 180'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/12"
{'file: 1101ae5553a457bc5ea51c393683c5bc819af2': 'size: 754'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/bc"
{'file: db0c253e3122380a94bb72f97af683a5f221d6': 'size: 645'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/f2"
{'file: 2c338f4806a135e349a35aa89d3b65aa1e9266': 'size: 2839'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/pack"
{'file: pack-c2f6c395361081eacaa8ad99cdd5b6ee71fe9e7a.pack': 'size: 47586', 'file: pack-c2f6c395361081eacaa8ad99cdd5b6ee71fe9e7a.idx': 'size: 9696'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/39"
{'file: 0fc4105e38ad77ba4af26915c7c8c4938116a1': 'size: 648'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/fe"
{'file: dd72890cd1e67ceb128ada17d74dc9a9e48e8d': 'size: 174', 'file: fa9d82db3038e37b1b66188665adf819761497': 'size: 714', 'file: e918db9d682b5b72afaa0380ffc308e95b1fe6': 'size: 630'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/cf"
{'file: 68c5c767b37ca1da86e7ef7787179bb9f92d3d': 'size: 713'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/89"
{'file: d2d529acb7b3eec35eb253eaad3d2d560561ea': 'size: 175'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/56"
{'file: 8059592871c1af40ab29184ee72ac1b4fa6256': 'size: 706'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/a9"
{'file: 39dcfb58ea56b075d0d9a20e04ccad0680aade': 'size: 649', 'file: b715aa58581aae109876cd4b943834b53da2e0': 'size: 727'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/5c"
{'file: 592fd7f7d3d6f0aefc6c7e6e45d1ec530057ef': 'size: 793', 'file: 629f6f736c2399279ee7ab0bc2d28fb15fec70': 'size: 659'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/db"
{'file: ff3b0ede55191a9c1794f1b16caeb0f512851c': 'size: 186', 'file: c5e624e52b3600f60321ed9c01220f760d2940': 'size: 166', 'file: c8ad028bf4647fb621e5a836c421a805c3c897': 'size: 166'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/f8"
{'file: d5d1c35d69a126e0f0d00b2e18fded21dae18a': 'size: 10391', 'file: 3488d50435da081d04272f8a9f421c3fca0024': 'size: 627'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/61"
{'file: 563060fd251ec7a59f7640627f4ac9be965f8a': 'size: 517'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/8f"
{'file: 04b5aa8d81b80c98310a7de08e971449a67465': 'size: 517', 'file: b0f0ab6204966eafa3ca4eb4c160c1ff655cf4': 'size: 237'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/d0"
{'file: ba861cd519bce06732c63c594dc2fe151c6ac8': 'size: 679'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/da"
{'file: 0f4ef9d638bf1771feb75196285faab00f636f': 'size: 11952'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/fd"
{'file: 84e220aadc3997f7fd9e692da8b989cf4ea523': 'size: 517'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/2e"
{'file: 8b658b034ee863a505ac60f69e93833f0dfeae': 'size: 631'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/77"
{'file: af61b5e0da01cdf7ee65a51cff5126cc22c05c': 'size: 754'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/e1"
{'file: 0b9e03b8b4ded7022d28f13cad3a5234ec0a8b': 'size: 1069'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/a4"
{'file: 2a34aee20dd0cc48cb07380cc1185e3ae34e69': 'size: 268'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/05"
{'file: 24cbdcd374d58f9fe916af757873132f7ee761': 'size: 13784'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/cd"
{'file: 2628560a9c20fbf5bde25ad75df07717bc44ee': 'size: 588', 'file: 57ec51d6528b92ae854c39797800a56793ba0f': 'size: 1437'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/4e"
{'file: 56e999470e8fea5b33bf166521043e61ebf21a': 'size: 185'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/57"
{'file: 39ca7bcd15400233caba1c2837324eff0581a2': 'size: 640'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/1f"
{'file: 17d9d2aa9216156ec305041b4af962f33c0324': 'size: 2171'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/2d"
{'file: feca495a97bbe68f80ead23b9a180b3f016b4f': 'size: 1338'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/7a"
{'file: a14c719238ba6ab4ad189959c7139b1b673aed': 'size: 12380', 'file: 0e4e6490879ab51ab5f950c3b163ea3942a713': 'size: 746'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/9a"
{'file: da4f7af78af440a5dbffd659b8c07b69d9deb6': 'size: 13782', 'file: 1d7c1c1cd9e40f56809a9f602d4dc7f65c30ff': 'size: 746'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/87"
{'file: 2192097cd47d4aabc96a290362a78914031857': 'size: 16152'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/d1"
{'file: c9460bbfe8ed3998144c61e3cad22476ea9196': 'size: 175', 'file: 54061b8c4e2c477e239d3a3b4cc1091bdece75': 'size: 790'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/c4"
{'file: db043e639574c668321a15b9fe9449d485710d': 'size: 237'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/11"
{'file: 34d4c525753dbf2b7b67c6a2dbbcbcc5141dc5': 'size: 162', 'file: 2e3fa45e7a3066403586af9c8b732298cbf2fb': 'size: 754'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/4a"
{'file: 21f73359a1041ee825a3b90a221737df66360a': 'size: 182'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/04"
{'file: 4ace1ce598045b3f6e144b86a363938e468d22': 'size: 713'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/ef"
{'file: 1d0aa6c117b712c88f5f5b85b8785878abec21': 'size: 172', 'file: 770e80243fa8b983b7c460ae10fa8f94080a16': 'size: 180'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/91"
{'file: 445d045d48af5ac657eb4e57236affbf957319': 'size: 848'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/70"
{'file: f87e88c40362500f354d5ba0cb19c36ff9dffd': 'size: 165', 'file: efc0e9308124404b7dac3bf1d18514f7497fbc': 'size: 168'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/7e"
{'file: 2eac4fb2c2b50ddfdedc3be41fa57dbeb0bd89': 'size: 708', 'file: 94229fabe95566121299ecdc96732378999a5d': 'size: 171'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/3f"
{'file: 8acedfc8c2781a22bf6f359bcee9345750f6ed': 'size: 83810'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/de"
{'file: b2b7dffe81dae9747eaf28d555227390a4eef4': 'size: 517'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/0e"
{'file: 397a5bac8d47df962c710719e7f79d31769787': 'size: 175'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/4d"
{'file: 0cad273b78f9ce5ec8cfa7223ef02804a46d33': 'size: 517'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/f3"
{'file: 00cd16db6b883fa518abd447da5711734553dc': 'size: 165'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/b2"
{'file: 42bdcca03f0488714b078cd0005f8bccc634a6': 'size: 81'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/85"
{'file: 24c6b4b47627abea364661a1e10821e5e5060f': 'size: 713', 'file: f5a01de7c56e79c5ae50edc6dcb9a0cb048aa6': 'size: 1230'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/03"
{'file: 4b92b1e2ff5ad46af3aaa6b07c453da225dc06': 'size: 261'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/60"
{'file: ee7ff66a4e24815a19ab6a15bead0e47157c4a': 'size: 2184', 'file: f9e859e5263392d33b03497072e861a6a50e47': 'size: 176'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/ba"
{'file: 5a2aebfef323fff7e8b5f3d097c4e06a75f40e': 'size: 2806'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/ec"
{'file: da58750c3637d01fc9f560f74c6998fca70450': 'size: 899', 'file: b7ec65bb946cc74c9d4f7cfe465d382c988cfa': 'size: 531'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/ea"
{'file: e7f62b0516c65b4bc8a47a1fe1b78707057e35': 'size: 746'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/09"
{'file: b012e77630215158a34813ad624b4691a1a986': 'size: 807'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/80"
{'file: e20920fb732fa585230f43947b322d1799ac9f': 'size: 615'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/67"
{'file: 1b28ccee7ddae70faa0a53eb0781d189d65c42': 'size: 649'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/a7"
{'file: 21c62629648d6caefd3d5f6e19580730d96413': 'size: 164'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/1d"
{'file: bba33dac22c791e86c3ccfa51c9b16f082f02a': 'size: 187'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/13"
{'file: d8f8378b80496f778fd5c2660bcaa9fceb0a8c': 'size: 175', 'file: 24716327e824d34d0e3ad907d1c27729b2dd1f': 'size: 1183'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/32"
{'file: 696ee6c5b102d64d16df6e768cb99b0b35926a': 'size: 517', 'file: 8d69ce0d59c5175ff58b47e87325ae3e3b52d5': 'size: 1238'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/99"
{'file: 8d0486e5e00f4c759743ec478546c54f338968': 'size: 713'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/info"
{'path: /home/dohyungkim2023/my-python-repo/.git/objects/info': 'size: N/A - 0 file exists'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/b6"
{'file: 779320394da6f4484bc926683d21ac41196b54': 'size: 1179', 'file: f777725f0000abc51738efdbd413deaee48e36': 'size: 176'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/e8"
{'file: bfcf8ce4f9be67019cedb45f1b5265693f6e18': 'size: 175'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/26"
{'file: c3a1c490466b6d9e9aa65b04b8e02f34d13a0b': 'size: 615'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/b1"
{'file: 9c779b1749ef6badecbc74a6e2b3646bbf790a': 'size: 687', 'file: 336a948e9eb6a9d3eb06c93e287ff6f1d0d91c': 'size: 624'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/1b"
{'file: fcb3f5f9d27524136b744d4a6b907e412ee5ab': 'size: 469'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/e0"
{'file: fdef9563b110ef1925bfa6544acb10cf16fbc2': 'size: 889'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/0c"
{'file: fc551ba8c25d1330b421d22b2b2125ee5d8a6f': 'size: 140'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/5d"
{'file: 49ebb685c5b602a58d909b7d7bb4949542a48b': 'size: 320', 'file: b10daf8245892c7fe874dffe59abe45ef12d78': 'size: 2284'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/1a"
{'file: a0a95110d1c19e9de7308d2e3ffb2594faa6e3': 'size: 232'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/7b"
{'file: 1cc34cff9ff511d166ad4b71dd0e052ac8fb1d': 'size: 166', 'file: 11c8c687a57780b9baf1038cc22efbd9f78422': 'size: 178'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/e7"
{'file: abc8b9014da7209cf242c1ff948e8feddc23b8': 'size: 171'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/fc"
{'file: 52f07c3c82b3df2deaf49200ab2a56c14175f8': 'size: 552', 'file: a03bab2fcd8d039a7998af59a15f3de173f8c0': 'size: 547'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/d9"
{'file: fea6ac86159840757f30565dbda375e79ba39f': 'size: 1244'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/6c"
{'file: 5f11fcb426454c02847c6b795354fff776cab4': 'size: 713'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/eb"
{'file: 01d12a6335d005c5276a8d2dc634452a64bd1c': 'size: 1011'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/84"
{'file: d41bc3d2fbc8faa86f8b4dfed887b412a4b92b': 'size: 189'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/97"
{'file: 538fb7f1403c182ac1af1b4e77bea4d67e0db9': 'size: 237'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/e5"
{'file: 309aa67ed69b926490a44f0b6b76518b64ee29': 'size: 632'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/54"
{'file: 402fbf718bdccd6231740f7db1a192dd0b49d5': 'size: 925'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/c8"
{'file: b8bf481cc58a43b4927caf04c4bdb0e1d58da6': 'size: 2514'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/38"
{'file: 6838c905ce704e33c4eaa205211714ed9e0e39': 'size: 551'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/17"
{'file: 61e3eff0243b7c3f93f1846e38c635540200e1': 'size: 496'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/c2"
{'file: ae9d8e619633e3611372b6a7c6ebd979cc56a9': 'size: 587', 'file: e33ef95f6f2cb20dabaa77274576ff984f4b49': 'size: 616'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/62"
{'file: b69a0aedacf895ce57c84e7331500a04c12097': 'size: 650'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/b7"
{'file: ebfcccb1369a2d8828ca0c77080a7d3a33dfc6': 'size: 647'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/6e"
{'file: 540a6c0e7ca18ec97fd1e5d6d3be3577422572': 'size: 166', 'file: 63693a9b4e96d5edb28fd6178ff7633ce0a2e5': 'size: 713'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/b9"
{'file: c3c09c68c5fa940719c0df51f4ad94ff5c086c': 'size: 5699'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/objects/e9"
{'file: d85e4cc767f8c076c9498b9d2b618a357384ca': 'size: 642'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/info"
{'file: exclude': 'size: 240'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/refs"
{'path: /home/dohyungkim2023/my-python-repo/.git/refs': 'size: N/A - 0 file exists'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/refs/tags"
{'path: /home/dohyungkim2023/my-python-repo/.git/refs/tags': 'size: N/A - 0 file exists'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/refs/remotes"
{'path: /home/dohyungkim2023/my-python-repo/.git/refs/remotes': 'size: N/A - 0 file exists'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/refs/remotes/origin"
{'file: main': 'size: 41'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/refs/heads"
{'file: main': 'size: 41', 'file: dkim-04102023': 'size: 41'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/logs"
{'file: HEAD': 'size: 13441'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/logs/refs"
{'path: /home/dohyungkim2023/my-python-repo/.git/logs/refs': 'size: N/A - 0 file exists'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/logs/refs/remotes"
{'path: /home/dohyungkim2023/my-python-repo/.git/logs/refs/remotes': 'size: N/A - 0 file exists'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/logs/refs/remotes/origin"
{'file: main': 'size: 1960'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/.git/logs/refs/heads"
{'file: main': 'size: 3292', 'file: dkim-04102023': 'size: 870'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/week13"
{'file: wk13-project_walk_fd_v1.py': 'size: 16183', 'file: wk13-project_walk_fd_v3.py': 'size: 89740', 'file: wk13-project_walk_fd_v4_list_of_dict.py': 'size: 69017', 'file: wk13-project_list_v1.py': 'size: 1471', 'file: wk13-project_file_dict_1st_draft.py': 'size: 3745', 'file: wk13-project_walk_fd_v2.py': 'size: 68164', 'file: wk13-project_walk_fd_v4_rev1.py': 'size: 9305', 'file: output.txt': 'size: 487529'}
##### This is the directory of "/home/dohyungkim2023/my-python-repo/week12"
{'file: wk12-project_AWS-service-inventory.py': 'size: 6779'}


################################################

See the final version of a dict of dict below:


 {'/home/dohyungkim2023/my-python-repo': {'file: testing-functions.py': 'size: 4248', 'file: string-info.py': 'size: 2679', 'file: scopes.py': 'size: 2292', 'file: .gitignore': 'size: 1799', 'file: fizz-buzz.py': 'size: 1121', 'file: py-if-elif-else.py': 'size: 1397', 'file: using-dictionaries.py': 'size: 6584', 'file: README.md': 'size: 152', 'file: find_string.py': 'size: 1006', 'file: split&join_again.py': 'size: 1930', 'file: scope2.py': 'size: 1444', 'file: fizz-buzz-item.py': 'size: 1203', 'file: wk13-Mon-lesson-04032023.py': 'size: 6904', 'file: using-list.py': 'size: 4017', 'file: variations.py': 'size: 3297', 'file: Hello_world.py': 'size: 53', 'file: Hello_yourname.py': 'size: 1080', 'file: using-generator.py': 'size: 2540'}, '/home/dohyungkim2023/my-python-repo/.git': {'file: index': 'size: 2288', 'file: HEAD': 'size: 30', 'file: packed-refs': 'size: 46', 'file: config': 'size: 263', 'file: description': 'size: 73', 'file: FETCH_HEAD': 'size: 102', 'file: COMMIT_EDITMSG': 'size: 51', 'file: ORIG_HEAD': 'size: 41'}, '/home/dohyungkim2023/my-python-repo/.git/branches': {'path: /home/dohyungkim2023/my-python-repo/.git/branches': 'size: N/A - 0 file exists'}, '/home/dohyungkim2023/my-python-repo/.git/hooks': {'file: fsmonitor-watchman.sample': 'size: 4655', 'file: push-to-checkout.sample': 'size: 2783', 'file: update.sample': 'size: 3650', 'file: pre-applypatch.sample': 'size: 424', 'file: pre-push.sample': 'size: 1374', 'file: pre-receive.sample': 'size: 544', 'file: pre-merge-commit.sample': 'size: 416', 'file: applypatch-msg.sample': 'size: 478', 'file: pre-commit.sample': 'size: 1643', 'file: prepare-commit-msg.sample': 'size: 1492', 'file: commit-msg.sample': 'size: 896', 'file: post-update.sample': 'size: 189', 'file: pre-rebase.sample': 'size: 4898'}, '/home/dohyungkim2023/my-python-repo/.git/objects': {'path: /home/dohyungkim2023/my-python-repo/.git/objects': 'size: N/A - 0 file exists'}, '/home/dohyungkim2023/my-python-repo/.git/objects/49': {'file: 643f1f2687790aa54b9c066a5c303e7b530f0e': 'size: 162'}, '/home/dohyungkim2023/my-python-repo/.git/objects/52': {'file: 8b11654c973a9fd1d30cca7746b1989a84d0aa': 'size: 280'}, '/home/dohyungkim2023/my-python-repo/.git/objects/c5': {'file: 65835127d3055fd14927dd5644cca075b84dbb': 'size: 165'}, '/home/dohyungkim2023/my-python-repo/.git/objects/7d': {'file: 287af85a3a917e3ae6f4085b44e45d5e9b3e5f': 'size: 186', 'file: 928b1ee8ddcdd4d2de61219b9d48190e57f26d': 'size: 517'}, '/home/dohyungkim2023/my-python-repo/.git/objects/e3': {'file: 3d9011c1307a3d6eceb5a796be9a7121fcb329': 'size: 1364', 'file: e83ecd35e8f75eca5b4400a320ad0c27cf0ec4': 'size: 177'}, '/home/dohyungkim2023/my-python-repo/.git/objects/7c': {'file: 68f4aafcb40a040100f86f122148d1765c1abd': 'size: 190'}, '/home/dohyungkim2023/my-python-repo/.git/objects/ad': {'file: 0bfc9860c05866da5cb074379abb189a3f38d8': 'size: 746'}, '/home/dohyungkim2023/my-python-repo/.git/objects/a2': {'file: b1fde369283c0aae5847fba2e635d666112091': 'size: 588'}, '/home/dohyungkim2023/my-python-repo/.git/objects/44': {'file: e91f48ddd90ca5b30ca4b6d07f3b48fcc496ab': 'size: 1115'}, '/home/dohyungkim2023/my-python-repo/.git/objects/3e': {'file: 02c256775bfba9516bdb6a69f2dea5e0d54399': 'size: 517'}, '/home/dohyungkim2023/my-python-repo/.git/objects/30': {'file: bdfd802123c72180ef2a02dc80b729be4b84ca': 'size: 174'}, '/home/dohyungkim2023/my-python-repo/.git/objects/f5': {'file: b1518f34f1473117f1170e96e86345190c8d33': 'size: 188'}, '/home/dohyungkim2023/my-python-repo/.git/objects/5b': {'file: b4097d5112118577f618488f29e59fa1990241': 'size: 189', 'file: 836af98a0821787f2a7b8292535a27cc6d088c': 'size: 467'}, '/home/dohyungkim2023/my-python-repo/.git/objects/b4': {'file: fd8f400b07573940da882f5f1f69856057be3e': 'size: 552'}, '/home/dohyungkim2023/my-python-repo/.git/objects/b0': {'file: db908dc9b902458ca3619f65bbf31c0174c3d1': 'size: 773', 'file: ec75214984034f96d9d20ccab1a475a83aca7e': 'size: 1508'}, '/home/dohyungkim2023/my-python-repo/.git/objects/8c': {'file: 00630e0e4ba8ff1395ab48258f738e9aa99af9': 'size: 16132'}, '/home/dohyungkim2023/my-python-repo/.git/objects/51': {'file: ffc52f125dbfefa6669a2371b39ff0c76b1695': 'size: 175'}, '/home/dohyungkim2023/my-python-repo/.git/objects/a8': {'file: b4964f6c3a87f27faab9bd670656957ab01fa8': 'size: 12428', 'file: 5225a0ce546492e8138a283873e50512268044': 'size: 646', 'file: 4021b0641b86c33c748a40f0a3517e182486da': 'size: 757'}, '/home/dohyungkim2023/my-python-repo/.git/objects/bd': {'file: 3aba3c41e36b11d0605ee91f2b8940950f65aa': 'size: 195', 'file: 43c57c4f276dff983b3fa1eea25b63413fcd11': 'size: 192'}, '/home/dohyungkim2023/my-python-repo/.git/objects/6b': {'file: 426a519a7a65f7aef9bfa9a60f7200ac7e2124': 'size: 274'}, '/home/dohyungkim2023/my-python-repo/.git/objects/55': {'file: 189ea76ed6d6f154245f467346675d966916fd': 'size: 1187', 'file: 48d1e3a25e1ab5793b8651d894f29296cee398': 'size: 186'}, '/home/dohyungkim2023/my-python-repo/.git/objects/86': {'file: 0c00594ae75ca8ec2f1ecbc21dd1b06bff69b4': 'size: 645'}, '/home/dohyungkim2023/my-python-repo/.git/objects/df': {'file: fca6d33fde52fb73d66cb2cec201641fb22a8c': 'size: 5616'}, '/home/dohyungkim2023/my-python-repo/.git/objects/8b': {'file: 9201506d17e10935cab341abf3403fc0fab1df': 'size: 192'}, '/home/dohyungkim2023/my-python-repo/.git/objects/07': {'file: 081d9d3778d79f8358839d337d7362bfc1fa4d': 'size: 168'}, '/home/dohyungkim2023/my-python-repo/.git/objects/15': {'file: 1309920de6d161f251f4f527f2e2ba5a784d53': 'size: 372', 'file: a1d717d75979fd412b3faed51f4cb34740c2dc': 'size: 713', 'file: 5b7a5fd67e2c460966144abbc3d673f63fc4cf': 'size: 12396'}, '/home/dohyungkim2023/my-python-repo/.git/objects/1e': {'file: 3caea0585fc90c7f1d1a4cd9a6b0b1619a1336': 'size: 460'}, '/home/dohyungkim2023/my-python-repo/.git/objects/79': {'file: b04af55b52006dd4e77e9f7b1c58690601e941': 'size: 548', 'file: a221e97a644a94d2a290fff52607c5514cebef': 'size: 12030'}, '/home/dohyungkim2023/my-python-repo/.git/objects/bb': {'file: 1ba790a3ca1a2de7cdccb5942617e1ace6bd58': 'size: 181'}, '/home/dohyungkim2023/my-python-repo/.git/objects/24': {'file: 206c4d129cc3ca3fa03aa204a14de820609e02': 'size: 879'}, '/home/dohyungkim2023/my-python-repo/.git/objects/6a': {'file: a6d559918d3a22f38b8628f9a685bcd720b90e': 'size: 1425'}, '/home/dohyungkim2023/my-python-repo/.git/objects/3b': {'file: fba49af95e18b2a96a64661c7b7c5a043733cb': 'size: 339', 'file: a1ec3f81e9f27ef1a03bf64ba7863033c9807b': 'size: 180'}, '/home/dohyungkim2023/my-python-repo/.git/objects/12': {'file: 1101ae5553a457bc5ea51c393683c5bc819af2': 'size: 754'}, '/home/dohyungkim2023/my-python-repo/.git/objects/bc': {'file: db0c253e3122380a94bb72f97af683a5f221d6': 'size: 645'}, '/home/dohyungkim2023/my-python-repo/.git/objects/f2': {'file: 2c338f4806a135e349a35aa89d3b65aa1e9266': 'size: 2839'}, '/home/dohyungkim2023/my-python-repo/.git/objects/pack': {'file: pack-c2f6c395361081eacaa8ad99cdd5b6ee71fe9e7a.pack': 'size: 47586', 'file: pack-c2f6c395361081eacaa8ad99cdd5b6ee71fe9e7a.idx': 'size: 9696'}, '/home/dohyungkim2023/my-python-repo/.git/objects/39': {'file: 0fc4105e38ad77ba4af26915c7c8c4938116a1': 'size: 648'}, '/home/dohyungkim2023/my-python-repo/.git/objects/fe': {'file: dd72890cd1e67ceb128ada17d74dc9a9e48e8d': 'size: 174', 'file: fa9d82db3038e37b1b66188665adf819761497': 'size: 714', 'file: e918db9d682b5b72afaa0380ffc308e95b1fe6': 'size: 630'}, '/home/dohyungkim2023/my-python-repo/.git/objects/cf': {'file: 68c5c767b37ca1da86e7ef7787179bb9f92d3d': 'size: 713'}, '/home/dohyungkim2023/my-python-repo/.git/objects/89': {'file: d2d529acb7b3eec35eb253eaad3d2d560561ea': 'size: 175'}, '/home/dohyungkim2023/my-python-repo/.git/objects/56': {'file: 8059592871c1af40ab29184ee72ac1b4fa6256': 'size: 706'}, '/home/dohyungkim2023/my-python-repo/.git/objects/a9': {'file: 39dcfb58ea56b075d0d9a20e04ccad0680aade': 'size: 649', 'file: b715aa58581aae109876cd4b943834b53da2e0': 'size: 727'}, '/home/dohyungkim2023/my-python-repo/.git/objects/5c': {'file: 592fd7f7d3d6f0aefc6c7e6e45d1ec530057ef': 'size: 793', 'file: 629f6f736c2399279ee7ab0bc2d28fb15fec70': 'size: 659'}, '/home/dohyungkim2023/my-python-repo/.git/objects/db': {'file: ff3b0ede55191a9c1794f1b16caeb0f512851c': 'size: 186', 'file: c5e624e52b3600f60321ed9c01220f760d2940': 'size: 166', 'file: c8ad028bf4647fb621e5a836c421a805c3c897': 'size: 166'}, '/home/dohyungkim2023/my-python-repo/.git/objects/f8': {'file: d5d1c35d69a126e0f0d00b2e18fded21dae18a': 'size: 10391', 'file: 3488d50435da081d04272f8a9f421c3fca0024': 'size: 627'}, '/home/dohyungkim2023/my-python-repo/.git/objects/61': {'file: 563060fd251ec7a59f7640627f4ac9be965f8a': 'size: 517'}, '/home/dohyungkim2023/my-python-repo/.git/objects/8f': {'file: 04b5aa8d81b80c98310a7de08e971449a67465': 'size: 517', 'file: b0f0ab6204966eafa3ca4eb4c160c1ff655cf4': 'size: 237'}, '/home/dohyungkim2023/my-python-repo/.git/objects/d0': {'file: ba861cd519bce06732c63c594dc2fe151c6ac8': 'size: 679'}, '/home/dohyungkim2023/my-python-repo/.git/objects/da': {'file: 0f4ef9d638bf1771feb75196285faab00f636f': 'size: 11952'}, '/home/dohyungkim2023/my-python-repo/.git/objects/fd': {'file: 84e220aadc3997f7fd9e692da8b989cf4ea523': 'size: 517'}, '/home/dohyungkim2023/my-python-repo/.git/objects/2e': {'file: 8b658b034ee863a505ac60f69e93833f0dfeae': 'size: 631'}, '/home/dohyungkim2023/my-python-repo/.git/objects/77': {'file: af61b5e0da01cdf7ee65a51cff5126cc22c05c': 'size: 754'}, '/home/dohyungkim2023/my-python-repo/.git/objects/e1': {'file: 0b9e03b8b4ded7022d28f13cad3a5234ec0a8b': 'size: 1069'}, '/home/dohyungkim2023/my-python-repo/.git/objects/a4': {'file: 2a34aee20dd0cc48cb07380cc1185e3ae34e69': 'size: 268'}, '/home/dohyungkim2023/my-python-repo/.git/objects/05': {'file: 24cbdcd374d58f9fe916af757873132f7ee761': 'size: 13784'}, '/home/dohyungkim2023/my-python-repo/.git/objects/cd': {'file: 2628560a9c20fbf5bde25ad75df07717bc44ee': 'size: 588', 'file: 57ec51d6528b92ae854c39797800a56793ba0f': 'size: 1437'}, '/home/dohyungkim2023/my-python-repo/.git/objects/4e': {'file: 56e999470e8fea5b33bf166521043e61ebf21a': 'size: 185'}, '/home/dohyungkim2023/my-python-repo/.git/objects/57': {'file: 39ca7bcd15400233caba1c2837324eff0581a2': 'size: 640'}, '/home/dohyungkim2023/my-python-repo/.git/objects/1f': {'file: 17d9d2aa9216156ec305041b4af962f33c0324': 'size: 2171'}, '/home/dohyungkim2023/my-python-repo/.git/objects/2d': {'file: feca495a97bbe68f80ead23b9a180b3f016b4f': 'size: 1338'}, '/home/dohyungkim2023/my-python-repo/.git/objects/7a': {'file: a14c719238ba6ab4ad189959c7139b1b673aed': 'size: 12380', 'file: 0e4e6490879ab51ab5f950c3b163ea3942a713': 'size: 746'}, '/home/dohyungkim2023/my-python-repo/.git/objects/9a': {'file: da4f7af78af440a5dbffd659b8c07b69d9deb6': 'size: 13782', 'file: 1d7c1c1cd9e40f56809a9f602d4dc7f65c30ff': 'size: 746'}, '/home/dohyungkim2023/my-python-repo/.git/objects/87': {'file: 2192097cd47d4aabc96a290362a78914031857': 'size: 16152'}, '/home/dohyungkim2023/my-python-repo/.git/objects/d1': {'file: c9460bbfe8ed3998144c61e3cad22476ea9196': 'size: 175', 'file: 54061b8c4e2c477e239d3a3b4cc1091bdece75': 'size: 790'}, '/home/dohyungkim2023/my-python-repo/.git/objects/c4': {'file: db043e639574c668321a15b9fe9449d485710d': 'size: 237'}, '/home/dohyungkim2023/my-python-repo/.git/objects/11': {'file: 34d4c525753dbf2b7b67c6a2dbbcbcc5141dc5': 'size: 162', 'file: 2e3fa45e7a3066403586af9c8b732298cbf2fb': 'size: 754'}, '/home/dohyungkim2023/my-python-repo/.git/objects/4a': {'file: 21f73359a1041ee825a3b90a221737df66360a': 'size: 182'}, '/home/dohyungkim2023/my-python-repo/.git/objects/04': {'file: 4ace1ce598045b3f6e144b86a363938e468d22': 'size: 713'}, '/home/dohyungkim2023/my-python-repo/.git/objects/ef': {'file: 1d0aa6c117b712c88f5f5b85b8785878abec21': 'size: 172', 'file: 770e80243fa8b983b7c460ae10fa8f94080a16': 'size: 180'}, '/home/dohyungkim2023/my-python-repo/.git/objects/91': {'file: 445d045d48af5ac657eb4e57236affbf957319': 'size: 848'}, '/home/dohyungkim2023/my-python-repo/.git/objects/70': {'file: f87e88c40362500f354d5ba0cb19c36ff9dffd': 'size: 165', 'file: efc0e9308124404b7dac3bf1d18514f7497fbc': 'size: 168'}, '/home/dohyungkim2023/my-python-repo/.git/objects/7e': {'file: 2eac4fb2c2b50ddfdedc3be41fa57dbeb0bd89': 'size: 708', 'file: 94229fabe95566121299ecdc96732378999a5d': 'size: 171'}, '/home/dohyungkim2023/my-python-repo/.git/objects/3f': {'file: 8acedfc8c2781a22bf6f359bcee9345750f6ed': 'size: 83810'}, '/home/dohyungkim2023/my-python-repo/.git/objects/de': {'file: b2b7dffe81dae9747eaf28d555227390a4eef4': 'size: 517'}, '/home/dohyungkim2023/my-python-repo/.git/objects/0e': {'file: 397a5bac8d47df962c710719e7f79d31769787': 'size: 175'}, '/home/dohyungkim2023/my-python-repo/.git/objects/4d': {'file: 0cad273b78f9ce5ec8cfa7223ef02804a46d33': 'size: 517'}, '/home/dohyungkim2023/my-python-repo/.git/objects/f3': {'file: 00cd16db6b883fa518abd447da5711734553dc': 'size: 165'}, '/home/dohyungkim2023/my-python-repo/.git/objects/b2': {'file: 42bdcca03f0488714b078cd0005f8bccc634a6': 'size: 81'}, '/home/dohyungkim2023/my-python-repo/.git/objects/85': {'file: 24c6b4b47627abea364661a1e10821e5e5060f': 'size: 713', 'file: f5a01de7c56e79c5ae50edc6dcb9a0cb048aa6': 'size: 1230'}, '/home/dohyungkim2023/my-python-repo/.git/objects/03': {'file: 4b92b1e2ff5ad46af3aaa6b07c453da225dc06': 'size: 261'}, '/home/dohyungkim2023/my-python-repo/.git/objects/60': {'file: ee7ff66a4e24815a19ab6a15bead0e47157c4a': 'size: 2184', 'file: f9e859e5263392d33b03497072e861a6a50e47': 'size: 176'}, '/home/dohyungkim2023/my-python-repo/.git/objects/ba': {'file: 5a2aebfef323fff7e8b5f3d097c4e06a75f40e': 'size: 2806'}, '/home/dohyungkim2023/my-python-repo/.git/objects/ec': {'file: da58750c3637d01fc9f560f74c6998fca70450': 'size: 899', 'file: b7ec65bb946cc74c9d4f7cfe465d382c988cfa': 'size: 531'}, '/home/dohyungkim2023/my-python-repo/.git/objects/ea': {'file: e7f62b0516c65b4bc8a47a1fe1b78707057e35': 'size: 746'}, '/home/dohyungkim2023/my-python-repo/.git/objects/09': {'file: b012e77630215158a34813ad624b4691a1a986': 'size: 807'}, '/home/dohyungkim2023/my-python-repo/.git/objects/80': {'file: e20920fb732fa585230f43947b322d1799ac9f': 'size: 615'}, '/home/dohyungkim2023/my-python-repo/.git/objects/67': {'file: 1b28ccee7ddae70faa0a53eb0781d189d65c42': 'size: 649'}, '/home/dohyungkim2023/my-python-repo/.git/objects/a7': {'file: 21c62629648d6caefd3d5f6e19580730d96413': 'size: 164'}, '/home/dohyungkim2023/my-python-repo/.git/objects/1d': {'file: bba33dac22c791e86c3ccfa51c9b16f082f02a': 'size: 187'}, '/home/dohyungkim2023/my-python-repo/.git/objects/13': {'file: d8f8378b80496f778fd5c2660bcaa9fceb0a8c': 'size: 175', 'file: 24716327e824d34d0e3ad907d1c27729b2dd1f': 'size: 1183'}, '/home/dohyungkim2023/my-python-repo/.git/objects/32': {'file: 696ee6c5b102d64d16df6e768cb99b0b35926a': 'size: 517', 'file: 8d69ce0d59c5175ff58b47e87325ae3e3b52d5': 'size: 1238'}, '/home/dohyungkim2023/my-python-repo/.git/objects/99': {'file: 8d0486e5e00f4c759743ec478546c54f338968': 'size: 713'}, '/home/dohyungkim2023/my-python-repo/.git/objects/info': {'path: /home/dohyungkim2023/my-python-repo/.git/objects/info': 'size: N/A - 0 file exists'}, '/home/dohyungkim2023/my-python-repo/.git/objects/b6': {'file: 779320394da6f4484bc926683d21ac41196b54': 'size: 1179', 'file: f777725f0000abc51738efdbd413deaee48e36': 'size: 176'}, '/home/dohyungkim2023/my-python-repo/.git/objects/e8': {'file: bfcf8ce4f9be67019cedb45f1b5265693f6e18': 'size: 175'}, '/home/dohyungkim2023/my-python-repo/.git/objects/26': {'file: c3a1c490466b6d9e9aa65b04b8e02f34d13a0b': 'size: 615'}, '/home/dohyungkim2023/my-python-repo/.git/objects/b1': {'file: 9c779b1749ef6badecbc74a6e2b3646bbf790a': 'size: 687', 'file: 336a948e9eb6a9d3eb06c93e287ff6f1d0d91c': 'size: 624'}, '/home/dohyungkim2023/my-python-repo/.git/objects/1b': {'file: fcb3f5f9d27524136b744d4a6b907e412ee5ab': 'size: 469'}, '/home/dohyungkim2023/my-python-repo/.git/objects/e0': {'file: fdef9563b110ef1925bfa6544acb10cf16fbc2': 'size: 889'}, '/home/dohyungkim2023/my-python-repo/.git/objects/0c': {'file: fc551ba8c25d1330b421d22b2b2125ee5d8a6f': 'size: 140'}, '/home/dohyungkim2023/my-python-repo/.git/objects/5d': {'file: 49ebb685c5b602a58d909b7d7bb4949542a48b': 'size: 320', 'file: b10daf8245892c7fe874dffe59abe45ef12d78': 'size: 2284'}, '/home/dohyungkim2023/my-python-repo/.git/objects/1a': {'file: a0a95110d1c19e9de7308d2e3ffb2594faa6e3': 'size: 232'}, '/home/dohyungkim2023/my-python-repo/.git/objects/7b': {'file: 1cc34cff9ff511d166ad4b71dd0e052ac8fb1d': 'size: 166', 'file: 11c8c687a57780b9baf1038cc22efbd9f78422': 'size: 178'}, '/home/dohyungkim2023/my-python-repo/.git/objects/e7': {'file: abc8b9014da7209cf242c1ff948e8feddc23b8': 'size: 171'}, '/home/dohyungkim2023/my-python-repo/.git/objects/fc': {'file: 52f07c3c82b3df2deaf49200ab2a56c14175f8': 'size: 552', 'file: a03bab2fcd8d039a7998af59a15f3de173f8c0': 'size: 547'}, '/home/dohyungkim2023/my-python-repo/.git/objects/d9': {'file: fea6ac86159840757f30565dbda375e79ba39f': 'size: 1244'}, '/home/dohyungkim2023/my-python-repo/.git/objects/6c': {'file: 5f11fcb426454c02847c6b795354fff776cab4': 'size: 713'}, '/home/dohyungkim2023/my-python-repo/.git/objects/eb': {'file: 01d12a6335d005c5276a8d2dc634452a64bd1c': 'size: 1011'}, '/home/dohyungkim2023/my-python-repo/.git/objects/84': {'file: d41bc3d2fbc8faa86f8b4dfed887b412a4b92b': 'size: 189'}, '/home/dohyungkim2023/my-python-repo/.git/objects/97': {'file: 538fb7f1403c182ac1af1b4e77bea4d67e0db9': 'size: 237'}, '/home/dohyungkim2023/my-python-repo/.git/objects/e5': {'file: 309aa67ed69b926490a44f0b6b76518b64ee29': 'size: 632'}, '/home/dohyungkim2023/my-python-repo/.git/objects/54': {'file: 402fbf718bdccd6231740f7db1a192dd0b49d5': 'size: 925'}, '/home/dohyungkim2023/my-python-repo/.git/objects/c8': {'file: b8bf481cc58a43b4927caf04c4bdb0e1d58da6': 'size: 2514'}, '/home/dohyungkim2023/my-python-repo/.git/objects/38': {'file: 6838c905ce704e33c4eaa205211714ed9e0e39': 'size: 551'}, '/home/dohyungkim2023/my-python-repo/.git/objects/17': {'file: 61e3eff0243b7c3f93f1846e38c635540200e1': 'size: 496'}, '/home/dohyungkim2023/my-python-repo/.git/objects/c2': {'file: ae9d8e619633e3611372b6a7c6ebd979cc56a9': 'size: 587', 'file: e33ef95f6f2cb20dabaa77274576ff984f4b49': 'size: 616'}, '/home/dohyungkim2023/my-python-repo/.git/objects/62': {'file: b69a0aedacf895ce57c84e7331500a04c12097': 'size: 650'}, '/home/dohyungkim2023/my-python-repo/.git/objects/b7': {'file: ebfcccb1369a2d8828ca0c77080a7d3a33dfc6': 'size: 647'}, '/home/dohyungkim2023/my-python-repo/.git/objects/6e': {'file: 540a6c0e7ca18ec97fd1e5d6d3be3577422572': 'size: 166', 'file: 63693a9b4e96d5edb28fd6178ff7633ce0a2e5': 'size: 713'}, '/home/dohyungkim2023/my-python-repo/.git/objects/b9': {'file: c3c09c68c5fa940719c0df51f4ad94ff5c086c': 'size: 5699'}, '/home/dohyungkim2023/my-python-repo/.git/objects/e9': {'file: d85e4cc767f8c076c9498b9d2b618a357384ca': 'size: 642'}, '/home/dohyungkim2023/my-python-repo/.git/info': {'file: exclude': 'size: 240'}, '/home/dohyungkim2023/my-python-repo/.git/refs': {'path: /home/dohyungkim2023/my-python-repo/.git/refs': 'size: N/A - 0 file exists'}, '/home/dohyungkim2023/my-python-repo/.git/refs/tags': {'path: /home/dohyungkim2023/my-python-repo/.git/refs/tags': 'size: N/A - 0 file exists'}, '/home/dohyungkim2023/my-python-repo/.git/refs/remotes': {'path: /home/dohyungkim2023/my-python-repo/.git/refs/remotes': 'size: N/A - 0 file exists'}, '/home/dohyungkim2023/my-python-repo/.git/refs/remotes/origin': {'file: main': 'size: 41'}, '/home/dohyungkim2023/my-python-repo/.git/refs/heads': {'file: main': 'size: 41', 'file: dkim-04102023': 'size: 41'}, '/home/dohyungkim2023/my-python-repo/.git/logs': {'file: HEAD': 'size: 13441'}, '/home/dohyungkim2023/my-python-repo/.git/logs/refs': {'path: /home/dohyungkim2023/my-python-repo/.git/logs/refs': 'size: N/A - 0 file exists'}, '/home/dohyungkim2023/my-python-repo/.git/logs/refs/remotes': {'path: /home/dohyungkim2023/my-python-repo/.git/logs/refs/remotes': 'size: N/A - 0 file exists'}, '/home/dohyungkim2023/my-python-repo/.git/logs/refs/remotes/origin': {'file: main': 'size: 1960'}, '/home/dohyungkim2023/my-python-repo/.git/logs/refs/heads': {'file: main': 'size: 3292', 'file: dkim-04102023': 'size: 870'}, '/home/dohyungkim2023/my-python-repo/week13': {'file: wk13-project_walk_fd_v1.py': 'size: 16183', 'file: wk13-project_walk_fd_v3.py': 'size: 89740', 'file: wk13-project_walk_fd_v4_list_of_dict.py': 'size: 69017', 'file: wk13-project_list_v1.py': 'size: 1471', 'file: wk13-project_file_dict_1st_draft.py': 'size: 3745', 'file: wk13-project_walk_fd_v2.py': 'size: 68164', 'file: wk13-project_walk_fd_v4_rev1.py': 'size: 9305', 'file: output.txt': 'size: 487529'}, '/home/dohyungkim2023/my-python-repo/week12': {'file: wk12-project_AWS-service-inventory.py': 'size: 6779'}}

 
 
 Convert the above output into the following JSON format 
 using JSON Formatter and Validator: https://jsonformatter.curiousconcept.com/#
 
 {
   "/home/dohyungkim2023/my-python-repo":{
      "file: testing-functions.py":"size: 4248",
      "file: string-info.py":"size: 2679",
      "file: scopes.py":"size: 2292",
      "file: .gitignore":"size: 1799",
      "file: fizz-buzz.py":"size: 1121",
      "file: py-if-elif-else.py":"size: 1397",
      "file: using-dictionaries.py":"size: 6584",
      "file: README.md":"size: 152",
      "file: find_string.py":"size: 1006",
      "file: split&join_again.py":"size: 1930",
      "file: scope2.py":"size: 1444",
      "file: fizz-buzz-item.py":"size: 1203",
      "file: wk13-Mon-lesson-04032023.py":"size: 6904",
      "file: using-list.py":"size: 4017",
      "file: variations.py":"size: 3297",
      "file: Hello_world.py":"size: 53",
      "file: Hello_yourname.py":"size: 1080",
      "file: using-generator.py":"size: 2540"
   },
   "/home/dohyungkim2023/my-python-repo/.git":{
      "file: index":"size: 2288",
      "file: HEAD":"size: 30",
      "file: packed-refs":"size: 46",
      "file: config":"size: 263",
      "file: description":"size: 73",
      "file: FETCH_HEAD":"size: 102",
      "file: COMMIT_EDITMSG":"size: 51",
      "file: ORIG_HEAD":"size: 41"
   },
   "/home/dohyungkim2023/my-python-repo/.git/branches":{
      "path: /home/dohyungkim2023/my-python-repo/.git/branches":"size: N/A - 0 file exists"
   },
   "/home/dohyungkim2023/my-python-repo/.git/hooks":{
      "file: fsmonitor-watchman.sample":"size: 4655",
      "file: push-to-checkout.sample":"size: 2783",
      "file: update.sample":"size: 3650",
      "file: pre-applypatch.sample":"size: 424",
      "file: pre-push.sample":"size: 1374",
      "file: pre-receive.sample":"size: 544",
      "file: pre-merge-commit.sample":"size: 416",
      "file: applypatch-msg.sample":"size: 478",
      "file: pre-commit.sample":"size: 1643",
      "file: prepare-commit-msg.sample":"size: 1492",
      "file: commit-msg.sample":"size: 896",
      "file: post-update.sample":"size: 189",
      "file: pre-rebase.sample":"size: 4898"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects":{
      "path: /home/dohyungkim2023/my-python-repo/.git/objects":"size: N/A - 0 file exists"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/49":{
      "file: 643f1f2687790aa54b9c066a5c303e7b530f0e":"size: 162"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/52":{
      "file: 8b11654c973a9fd1d30cca7746b1989a84d0aa":"size: 280"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/c5":{
      "file: 65835127d3055fd14927dd5644cca075b84dbb":"size: 165"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/7d":{
      "file: 287af85a3a917e3ae6f4085b44e45d5e9b3e5f":"size: 186",
      "file: 928b1ee8ddcdd4d2de61219b9d48190e57f26d":"size: 517"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/e3":{
      "file: 3d9011c1307a3d6eceb5a796be9a7121fcb329":"size: 1364",
      "file: e83ecd35e8f75eca5b4400a320ad0c27cf0ec4":"size: 177"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/7c":{
      "file: 68f4aafcb40a040100f86f122148d1765c1abd":"size: 190"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/ad":{
      "file: 0bfc9860c05866da5cb074379abb189a3f38d8":"size: 746"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/a2":{
      "file: b1fde369283c0aae5847fba2e635d666112091":"size: 588"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/44":{
      "file: e91f48ddd90ca5b30ca4b6d07f3b48fcc496ab":"size: 1115"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/3e":{
      "file: 02c256775bfba9516bdb6a69f2dea5e0d54399":"size: 517"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/30":{
      "file: bdfd802123c72180ef2a02dc80b729be4b84ca":"size: 174"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/f5":{
      "file: b1518f34f1473117f1170e96e86345190c8d33":"size: 188"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/5b":{
      "file: b4097d5112118577f618488f29e59fa1990241":"size: 189",
      "file: 836af98a0821787f2a7b8292535a27cc6d088c":"size: 467"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/b4":{
      "file: fd8f400b07573940da882f5f1f69856057be3e":"size: 552"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/b0":{
      "file: db908dc9b902458ca3619f65bbf31c0174c3d1":"size: 773",
      "file: ec75214984034f96d9d20ccab1a475a83aca7e":"size: 1508"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/8c":{
      "file: 00630e0e4ba8ff1395ab48258f738e9aa99af9":"size: 16132"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/51":{
      "file: ffc52f125dbfefa6669a2371b39ff0c76b1695":"size: 175"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/a8":{
      "file: b4964f6c3a87f27faab9bd670656957ab01fa8":"size: 12428",
      "file: 5225a0ce546492e8138a283873e50512268044":"size: 646",
      "file: 4021b0641b86c33c748a40f0a3517e182486da":"size: 757"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/bd":{
      "file: 3aba3c41e36b11d0605ee91f2b8940950f65aa":"size: 195",
      "file: 43c57c4f276dff983b3fa1eea25b63413fcd11":"size: 192"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/6b":{
      "file: 426a519a7a65f7aef9bfa9a60f7200ac7e2124":"size: 274"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/55":{
      "file: 189ea76ed6d6f154245f467346675d966916fd":"size: 1187",
      "file: 48d1e3a25e1ab5793b8651d894f29296cee398":"size: 186"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/86":{
      "file: 0c00594ae75ca8ec2f1ecbc21dd1b06bff69b4":"size: 645"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/df":{
      "file: fca6d33fde52fb73d66cb2cec201641fb22a8c":"size: 5616"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/8b":{
      "file: 9201506d17e10935cab341abf3403fc0fab1df":"size: 192"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/07":{
      "file: 081d9d3778d79f8358839d337d7362bfc1fa4d":"size: 168"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/15":{
      "file: 1309920de6d161f251f4f527f2e2ba5a784d53":"size: 372",
      "file: a1d717d75979fd412b3faed51f4cb34740c2dc":"size: 713",
      "file: 5b7a5fd67e2c460966144abbc3d673f63fc4cf":"size: 12396"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/1e":{
      "file: 3caea0585fc90c7f1d1a4cd9a6b0b1619a1336":"size: 460"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/79":{
      "file: b04af55b52006dd4e77e9f7b1c58690601e941":"size: 548",
      "file: a221e97a644a94d2a290fff52607c5514cebef":"size: 12030"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/bb":{
      "file: 1ba790a3ca1a2de7cdccb5942617e1ace6bd58":"size: 181"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/24":{
      "file: 206c4d129cc3ca3fa03aa204a14de820609e02":"size: 879"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/6a":{
      "file: a6d559918d3a22f38b8628f9a685bcd720b90e":"size: 1425"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/3b":{
      "file: fba49af95e18b2a96a64661c7b7c5a043733cb":"size: 339",
      "file: a1ec3f81e9f27ef1a03bf64ba7863033c9807b":"size: 180"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/12":{
      "file: 1101ae5553a457bc5ea51c393683c5bc819af2":"size: 754"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/bc":{
      "file: db0c253e3122380a94bb72f97af683a5f221d6":"size: 645"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/f2":{
      "file: 2c338f4806a135e349a35aa89d3b65aa1e9266":"size: 2839"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/pack":{
      "file: pack-c2f6c395361081eacaa8ad99cdd5b6ee71fe9e7a.pack":"size: 47586",
      "file: pack-c2f6c395361081eacaa8ad99cdd5b6ee71fe9e7a.idx":"size: 9696"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/39":{
      "file: 0fc4105e38ad77ba4af26915c7c8c4938116a1":"size: 648"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/fe":{
      "file: dd72890cd1e67ceb128ada17d74dc9a9e48e8d":"size: 174",
      "file: fa9d82db3038e37b1b66188665adf819761497":"size: 714",
      "file: e918db9d682b5b72afaa0380ffc308e95b1fe6":"size: 630"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/cf":{
      "file: 68c5c767b37ca1da86e7ef7787179bb9f92d3d":"size: 713"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/89":{
      "file: d2d529acb7b3eec35eb253eaad3d2d560561ea":"size: 175"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/56":{
      "file: 8059592871c1af40ab29184ee72ac1b4fa6256":"size: 706"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/a9":{
      "file: 39dcfb58ea56b075d0d9a20e04ccad0680aade":"size: 649",
      "file: b715aa58581aae109876cd4b943834b53da2e0":"size: 727"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/5c":{
      "file: 592fd7f7d3d6f0aefc6c7e6e45d1ec530057ef":"size: 793",
      "file: 629f6f736c2399279ee7ab0bc2d28fb15fec70":"size: 659"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/db":{
      "file: ff3b0ede55191a9c1794f1b16caeb0f512851c":"size: 186",
      "file: c5e624e52b3600f60321ed9c01220f760d2940":"size: 166",
      "file: c8ad028bf4647fb621e5a836c421a805c3c897":"size: 166"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/f8":{
      "file: d5d1c35d69a126e0f0d00b2e18fded21dae18a":"size: 10391",
      "file: 3488d50435da081d04272f8a9f421c3fca0024":"size: 627"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/61":{
      "file: 563060fd251ec7a59f7640627f4ac9be965f8a":"size: 517"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/8f":{
      "file: 04b5aa8d81b80c98310a7de08e971449a67465":"size: 517",
      "file: b0f0ab6204966eafa3ca4eb4c160c1ff655cf4":"size: 237"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/d0":{
      "file: ba861cd519bce06732c63c594dc2fe151c6ac8":"size: 679"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/da":{
      "file: 0f4ef9d638bf1771feb75196285faab00f636f":"size: 11952"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/fd":{
      "file: 84e220aadc3997f7fd9e692da8b989cf4ea523":"size: 517"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/2e":{
      "file: 8b658b034ee863a505ac60f69e93833f0dfeae":"size: 631"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/77":{
      "file: af61b5e0da01cdf7ee65a51cff5126cc22c05c":"size: 754"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/e1":{
      "file: 0b9e03b8b4ded7022d28f13cad3a5234ec0a8b":"size: 1069"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/a4":{
      "file: 2a34aee20dd0cc48cb07380cc1185e3ae34e69":"size: 268"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/05":{
      "file: 24cbdcd374d58f9fe916af757873132f7ee761":"size: 13784"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/cd":{
      "file: 2628560a9c20fbf5bde25ad75df07717bc44ee":"size: 588",
      "file: 57ec51d6528b92ae854c39797800a56793ba0f":"size: 1437"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/4e":{
      "file: 56e999470e8fea5b33bf166521043e61ebf21a":"size: 185"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/57":{
      "file: 39ca7bcd15400233caba1c2837324eff0581a2":"size: 640"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/1f":{
      "file: 17d9d2aa9216156ec305041b4af962f33c0324":"size: 2171"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/2d":{
      "file: feca495a97bbe68f80ead23b9a180b3f016b4f":"size: 1338"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/7a":{
      "file: a14c719238ba6ab4ad189959c7139b1b673aed":"size: 12380",
      "file: 0e4e6490879ab51ab5f950c3b163ea3942a713":"size: 746"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/9a":{
      "file: da4f7af78af440a5dbffd659b8c07b69d9deb6":"size: 13782",
      "file: 1d7c1c1cd9e40f56809a9f602d4dc7f65c30ff":"size: 746"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/87":{
      "file: 2192097cd47d4aabc96a290362a78914031857":"size: 16152"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/d1":{
      "file: c9460bbfe8ed3998144c61e3cad22476ea9196":"size: 175",
      "file: 54061b8c4e2c477e239d3a3b4cc1091bdece75":"size: 790"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/c4":{
      "file: db043e639574c668321a15b9fe9449d485710d":"size: 237"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/11":{
      "file: 34d4c525753dbf2b7b67c6a2dbbcbcc5141dc5":"size: 162",
      "file: 2e3fa45e7a3066403586af9c8b732298cbf2fb":"size: 754"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/4a":{
      "file: 21f73359a1041ee825a3b90a221737df66360a":"size: 182"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/04":{
      "file: 4ace1ce598045b3f6e144b86a363938e468d22":"size: 713"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/ef":{
      "file: 1d0aa6c117b712c88f5f5b85b8785878abec21":"size: 172",
      "file: 770e80243fa8b983b7c460ae10fa8f94080a16":"size: 180"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/91":{
      "file: 445d045d48af5ac657eb4e57236affbf957319":"size: 848"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/70":{
      "file: f87e88c40362500f354d5ba0cb19c36ff9dffd":"size: 165",
      "file: efc0e9308124404b7dac3bf1d18514f7497fbc":"size: 168"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/7e":{
      "file: 2eac4fb2c2b50ddfdedc3be41fa57dbeb0bd89":"size: 708",
      "file: 94229fabe95566121299ecdc96732378999a5d":"size: 171"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/3f":{
      "file: 8acedfc8c2781a22bf6f359bcee9345750f6ed":"size: 83810"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/de":{
      "file: b2b7dffe81dae9747eaf28d555227390a4eef4":"size: 517"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/0e":{
      "file: 397a5bac8d47df962c710719e7f79d31769787":"size: 175"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/4d":{
      "file: 0cad273b78f9ce5ec8cfa7223ef02804a46d33":"size: 517"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/f3":{
      "file: 00cd16db6b883fa518abd447da5711734553dc":"size: 165"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/b2":{
      "file: 42bdcca03f0488714b078cd0005f8bccc634a6":"size: 81"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/85":{
      "file: 24c6b4b47627abea364661a1e10821e5e5060f":"size: 713",
      "file: f5a01de7c56e79c5ae50edc6dcb9a0cb048aa6":"size: 1230"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/03":{
      "file: 4b92b1e2ff5ad46af3aaa6b07c453da225dc06":"size: 261"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/60":{
      "file: ee7ff66a4e24815a19ab6a15bead0e47157c4a":"size: 2184",
      "file: f9e859e5263392d33b03497072e861a6a50e47":"size: 176"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/ba":{
      "file: 5a2aebfef323fff7e8b5f3d097c4e06a75f40e":"size: 2806"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/ec":{
      "file: da58750c3637d01fc9f560f74c6998fca70450":"size: 899",
      "file: b7ec65bb946cc74c9d4f7cfe465d382c988cfa":"size: 531"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/ea":{
      "file: e7f62b0516c65b4bc8a47a1fe1b78707057e35":"size: 746"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/09":{
      "file: b012e77630215158a34813ad624b4691a1a986":"size: 807"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/80":{
      "file: e20920fb732fa585230f43947b322d1799ac9f":"size: 615"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/67":{
      "file: 1b28ccee7ddae70faa0a53eb0781d189d65c42":"size: 649"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/a7":{
      "file: 21c62629648d6caefd3d5f6e19580730d96413":"size: 164"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/1d":{
      "file: bba33dac22c791e86c3ccfa51c9b16f082f02a":"size: 187"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/13":{
      "file: d8f8378b80496f778fd5c2660bcaa9fceb0a8c":"size: 175",
      "file: 24716327e824d34d0e3ad907d1c27729b2dd1f":"size: 1183"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/32":{
      "file: 696ee6c5b102d64d16df6e768cb99b0b35926a":"size: 517",
      "file: 8d69ce0d59c5175ff58b47e87325ae3e3b52d5":"size: 1238"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/99":{
      "file: 8d0486e5e00f4c759743ec478546c54f338968":"size: 713"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/info":{
      "path: /home/dohyungkim2023/my-python-repo/.git/objects/info":"size: N/A - 0 file exists"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/b6":{
      "file: 779320394da6f4484bc926683d21ac41196b54":"size: 1179",
      "file: f777725f0000abc51738efdbd413deaee48e36":"size: 176"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/e8":{
      "file: bfcf8ce4f9be67019cedb45f1b5265693f6e18":"size: 175"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/26":{
      "file: c3a1c490466b6d9e9aa65b04b8e02f34d13a0b":"size: 615"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/b1":{
      "file: 9c779b1749ef6badecbc74a6e2b3646bbf790a":"size: 687",
      "file: 336a948e9eb6a9d3eb06c93e287ff6f1d0d91c":"size: 624"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/1b":{
      "file: fcb3f5f9d27524136b744d4a6b907e412ee5ab":"size: 469"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/e0":{
      "file: fdef9563b110ef1925bfa6544acb10cf16fbc2":"size: 889"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/0c":{
      "file: fc551ba8c25d1330b421d22b2b2125ee5d8a6f":"size: 140"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/5d":{
      "file: 49ebb685c5b602a58d909b7d7bb4949542a48b":"size: 320",
      "file: b10daf8245892c7fe874dffe59abe45ef12d78":"size: 2284"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/1a":{
      "file: a0a95110d1c19e9de7308d2e3ffb2594faa6e3":"size: 232"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/7b":{
      "file: 1cc34cff9ff511d166ad4b71dd0e052ac8fb1d":"size: 166",
      "file: 11c8c687a57780b9baf1038cc22efbd9f78422":"size: 178"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/e7":{
      "file: abc8b9014da7209cf242c1ff948e8feddc23b8":"size: 171"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/fc":{
      "file: 52f07c3c82b3df2deaf49200ab2a56c14175f8":"size: 552",
      "file: a03bab2fcd8d039a7998af59a15f3de173f8c0":"size: 547"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/d9":{
      "file: fea6ac86159840757f30565dbda375e79ba39f":"size: 1244"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/6c":{
      "file: 5f11fcb426454c02847c6b795354fff776cab4":"size: 713"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/eb":{
      "file: 01d12a6335d005c5276a8d2dc634452a64bd1c":"size: 1011"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/84":{
      "file: d41bc3d2fbc8faa86f8b4dfed887b412a4b92b":"size: 189"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/97":{
      "file: 538fb7f1403c182ac1af1b4e77bea4d67e0db9":"size: 237"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/e5":{
      "file: 309aa67ed69b926490a44f0b6b76518b64ee29":"size: 632"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/54":{
      "file: 402fbf718bdccd6231740f7db1a192dd0b49d5":"size: 925"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/c8":{
      "file: b8bf481cc58a43b4927caf04c4bdb0e1d58da6":"size: 2514"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/38":{
      "file: 6838c905ce704e33c4eaa205211714ed9e0e39":"size: 551"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/17":{
      "file: 61e3eff0243b7c3f93f1846e38c635540200e1":"size: 496"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/c2":{
      "file: ae9d8e619633e3611372b6a7c6ebd979cc56a9":"size: 587",
      "file: e33ef95f6f2cb20dabaa77274576ff984f4b49":"size: 616"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/62":{
      "file: b69a0aedacf895ce57c84e7331500a04c12097":"size: 650"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/b7":{
      "file: ebfcccb1369a2d8828ca0c77080a7d3a33dfc6":"size: 647"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/6e":{
      "file: 540a6c0e7ca18ec97fd1e5d6d3be3577422572":"size: 166",
      "file: 63693a9b4e96d5edb28fd6178ff7633ce0a2e5":"size: 713"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/b9":{
      "file: c3c09c68c5fa940719c0df51f4ad94ff5c086c":"size: 5699"
   },
   "/home/dohyungkim2023/my-python-repo/.git/objects/e9":{
      "file: d85e4cc767f8c076c9498b9d2b618a357384ca":"size: 642"
   },
   "/home/dohyungkim2023/my-python-repo/.git/info":{
      "file: exclude":"size: 240"
   },
   "/home/dohyungkim2023/my-python-repo/.git/refs":{
      "path: /home/dohyungkim2023/my-python-repo/.git/refs":"size: N/A - 0 file exists"
   },
   "/home/dohyungkim2023/my-python-repo/.git/refs/tags":{
      "path: /home/dohyungkim2023/my-python-repo/.git/refs/tags":"size: N/A - 0 file exists"
   },
   "/home/dohyungkim2023/my-python-repo/.git/refs/remotes":{
      "path: /home/dohyungkim2023/my-python-repo/.git/refs/remotes":"size: N/A - 0 file exists"
   },
   "/home/dohyungkim2023/my-python-repo/.git/refs/remotes/origin":{
      "file: main":"size: 41"
   },
   "/home/dohyungkim2023/my-python-repo/.git/refs/heads":{
      "file: main":"size: 41",
      "file: dkim-04102023":"size: 41"
   },
   "/home/dohyungkim2023/my-python-repo/.git/logs":{
      "file: HEAD":"size: 13441"
   },
   "/home/dohyungkim2023/my-python-repo/.git/logs/refs":{
      "path: /home/dohyungkim2023/my-python-repo/.git/logs/refs":"size: N/A - 0 file exists"
   },
   "/home/dohyungkim2023/my-python-repo/.git/logs/refs/remotes":{
      "path: /home/dohyungkim2023/my-python-repo/.git/logs/refs/remotes":"size: N/A - 0 file exists"
   },
   "/home/dohyungkim2023/my-python-repo/.git/logs/refs/remotes/origin":{
      "file: main":"size: 1960"
   },
   "/home/dohyungkim2023/my-python-repo/.git/logs/refs/heads":{
      "file: main":"size: 3292",
      "file: dkim-04102023":"size: 870"
   },
   "/home/dohyungkim2023/my-python-repo/week13":{
      "file: wk13-project_walk_fd_v1.py":"size: 16183",
      "file: wk13-project_walk_fd_v3.py":"size: 89740",
      "file: wk13-project_walk_fd_v4_list_of_dict.py":"size: 69017",
      "file: wk13-project_list_v1.py":"size: 1471",
      "file: wk13-project_file_dict_1st_draft.py":"size: 3745",
      "file: wk13-project_walk_fd_v2.py":"size: 68164",
      "file: wk13-project_walk_fd_v4_rev1.py":"size: 9305",
      "file: output.txt":"size: 487529"
   },
   "/home/dohyungkim2023/my-python-repo/week12":{
      "file: wk12-project_AWS-service-inventory.py":"size: 6779"
   }
}


[Case 2] Execute the script with an argument

~/my-python-repo$ ./week13/wk13-project_walk_fd_v4_list_of_dict.py week13/
##### This is the directory of "week13/"
{'path': 'week13/wk13-os-functions.py', 'size': 32143}
{'path': 'week13/wk13-project_walk_fd_v1.py', 'size': 16183}
{'path': 'week13/wk13-project_walk_fd_v3.py', 'size': 89740}
{'path': 'week13/wk13-project_walk_fd_v4_list_of_dict.py', 'size': 69017}
{'path': 'week13/wk13-project_walk_fd_v5_dict_of_dict.py', 'size': 56290}
{'path': 'week13/wk13-project_file_dict_1st_draft.py', 'size': 3745}
{'path': 'week13/wk13-project_walk_fd_v2.py', 'size': 68164}
{'path': 'week13/output.txt', 'size': 487529}


################################################

See the final version of a dict of dict below:


 {'week13/': {'file: wk13-os-functions.py': 'size: 32143', 'file: wk13-project_walk_fd_v1.py': 'size: 16183', 'file: wk13-project_walk_fd_v3.py': 'size: 89740', 'file: wk13-project_walk_fd_v4_list_of_dict.py': 'size: 69017', 'file: wk13-project_walk_fd_v5_dict_of_dict.py': 'size: 81281', 'file: wk13-project_file_dict_1st_draft.py': 'size: 3745', 'file: wk13-project_walk_fd_v2.py': 'size: 68164', 'file: output.txt': 'size: 487529'}}



 Convert the above output into the following JSON format 
 using JSON Formatter and Validator: https://jsonformatter.curiousconcept.com/#
 
 {
   "week13/":{
      "file: wk13-os-functions.py":"size: 32143",
      "file: wk13-project_walk_fd_v1.py":"size: 16183",
      "file: wk13-project_walk_fd_v3.py":"size: 89740",
      "file: wk13-project_walk_fd_v4_list_of_dict.py":"size: 69017",
      "file: wk13-project_walk_fd_v5_dict_of_dict.py":"size: 81281",
      "file: wk13-project_file_dict_1st_draft.py":"size: 3745",
      "file: wk13-project_walk_fd_v2.py":"size: 68164",
      "file: output.txt":"size: 487529"
   }
}

 '''
