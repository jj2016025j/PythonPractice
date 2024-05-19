import os

# 定義要遍歷的資料夾
# folder_path = './'
folder_path = 'C:/Users/User/Github/PythonTool/test'

# 遍歷資料夾中的所有文件和子資料夾
for root, dirs, files in os.walk(folder_path):
    print(f'Current folder: {root}')
    for dir_name in dirs:
        print(f'Directory: {dir_name}')
    for file_name in files:
        print(f'File: {file_name}')

# OK