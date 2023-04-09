#!/usr/bin/env python3.10
import os

# Create an empty list and an empty dictionary
file_list=[]
dict_of_list={}

#def get_file_list(root, file_names, each_sub_dir):
#    print("This is the directory of ", os.path.join(root,each_sub_dir))
#    for each_file in file_names:
#        each_item = f"'path' : {os.path.join(root, each_sub_dir)}, 'size' : {os.stat(each_file).st_size}"
#        file_list.append(each_item)
#        print(each_item, sep="\n") # print each file item per line on computer screen
#    return file_list # return the created file_list list 

def get_tree_directory(dir='/home/dohyungkim2023/my-python-repo'):
    for root, sub_dir_names, file_names in os.walk(dir):
        #print (f"{root},\n{sub_dir_names}, {file_names}") # list sub directories and file names under the directory  
        if sub_dir_names ==[]:
#            each_file_list_per_each_dir = get_file_list(root, file_names, each_sub_dir='')
            print("This is the directory of ", os.path.join(root))
            for each_file in file_names:
                each_item = { 'path' : os.path.join(root, each_file), 'size' : os.path.getsize(os.path.join(root, each_file))}
                file_list.append(each_item)                 
                print(each_item, sep="\n")
        else:            
            for each_sub_dir in sub_dir_names: 
                for each_file in file_names:
                    each_item = { 'path' : os.path.join(root, each_file), 'size' : os.path.getsize(os.path.join(root, each_file))}
                    file_list.append(each_item)                 
                    print(each_item, sep="\n")
        
        
    print(file_list)






working_path = input("Enter the working directory pathway: ") # /home/dohyungkim2023/my-python-repo"
get_tree_directory(working_path)







