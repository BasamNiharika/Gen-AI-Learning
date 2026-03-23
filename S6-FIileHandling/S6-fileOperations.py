import os

print('File Operations')

# read the whole file 
with open('example.txt','r') as file:
    content = file.read()
    print(content)

# Read a file line by line 
with open('example.txt', 'r') as file:
    for line in file:
        print(line)  #strip() removes newline character 

# Writing a file (Overwriting)
with open('example.txt','w') as file:
    file.write('Hello world\n')
    file.write('this is a new line\n')

# Writing a file (without overwriting)
with open('example.txt','a') as file:
    file.write('Append operation is taking place')

# writing multiple lines to a file 
lines = ['First line\n', 'Second line\n', 'Third line\n', 'Fourth line\n']
with open('example.txt', 'a') as file:
    file.writelines(lines)

# reading the content from source text file to destination text file
with open('example.txt', 'r') as source_file:
    content = source_file.read()
with open('destination.txt','w') as destination_file:
    destination_file.write(content)

# Writing and then reading a file 
with open('example2.txt','w+') as file:
    file.write("Hello Every one.")
    file.write("Hearty Welcome !!!")

    ## Move file cursor to the beginning 
    file.seek(0)

    # reading from a file 
    content = file.read()
    print(content)

## creat a new directory 
new_directory = "folder"
# os.mkdir(new_directory)
print(f"Directory '{new_directory}' Created.")

## Listing files and directories
items = os.listdir('.')
print(items)

## Joining Paths 
dir_name = "folder1"
file_name = "file.txt"
full_path = os.path.join(os.getcwd(),dir_name, file_name)
print(full_path)

# Checking if file path exists or not 
path = 'example.txt'
if os.path.exists(path):
    print(f"The path {path} exists")
else:
    print(f"The path {path} does not exist")

# Checking if a path is file or directory
path = 'folder'
if os.path.isfile(path):
    print(f"The path '{path}' is a file")
elif os.path.isdir(path):
    print(f"The Path '{path}' is a directory")
else:
    print(f"The path '{path} is neither a file nor a directory'")

# Getting the absolute path
relative_path = 'example.txt'
absolute_path = os.path.abspath(relative_path)
print(absolute_path)