
# importing os module
import os
	
Get the current working directory (CWD)
print("Current working directory:", os.getcwd())

# Changing the CWD 
os.chdir('../..') 

print("Current working directory:", os.getcwd())
print("The file is",__file__)
print("Absolute path of the file " , os.path.realpath(__file__))
print("directory where the file exists", os.path.dirname(os.path.realpath(__file__)))

path =  os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Folder_created_from_code')
print("Creating a directory at " , path)
os.mkdir(path) 


path =  os.path.join(os.path.dirname(os.path.realpath(__file__)), 'DIR_created_from_code\level1\level2')
print("Creating a directory at " , path)
   
os.makedirs(path) 

path = os.chdir('../../../')
dir_list = os.listdir(path)
print("Files and directories in '", path, "' :" , dir_list) 
  