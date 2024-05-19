import shutil
import os

def delete_folder(folder_path):
    try:
        shutil.rmtree(folder_path)
        print(f'Folder {folder_path} and all its contents deleted successfully.')
    except FileNotFoundError:
        print(f'Error: The folder {folder_path} does not exist.')
    except PermissionError:
        print(f'Error: You do not have permission to delete {folder_path}.')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')

# 定義要刪除的資料夾路徑
folder_path = './test'

# 刪除資料夾及其內容
delete_folder(folder_path)
