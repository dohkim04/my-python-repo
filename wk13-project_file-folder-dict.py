# Date: 04/07/2023
# Title: Week 13 project - creating a list of file and folder dictionary

# FOUNDATIONAL
# Create a script to that generates a list of dictionaries about files in the working directory. 
# Then print the list.
# Push your code to GitHub and include the link in your write up.

##########################################

#!/usr/bin/env python3.7
import os

current_directory = os.getcwd()

# print(current_directory)
entries = os.path(current_directory)
for entry in entries:
    print(entry.is_file)

        
    

##########################################
# ADVANCED
# Modify the script into a function such that any path can be passed as a parameter. 
# This parameter should be optional and should default to working directory when the variable is not passed. 
# The function should then create the list of dictionaries about files from that path. 
# The function should also return information on files nested in folders (recursive).

# COMPLEX (Very Tricky)
# Modify the function to display recursive file information as dictionary of dictionaries.

