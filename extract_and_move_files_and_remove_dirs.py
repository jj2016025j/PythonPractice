import os
import shutil
import zipfile

def extract_and_move_files(src_dir, dst_dir):
    # 第一步：解压缩
    for root, dirs, files in os.walk(src_dir):
        for name in files:
            if name.endswith('.zip'):
                zip_path = os.path.join(root, name)
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    zip_ref.extractall(root)
                os.remove(zip_path)

    # 第二步和第三步：移动文件并删除原始文件夹
    for root, dirs, files in os.walk(src_dir, topdown=False):
        for name in files:
            src_file = os.path.join(root, name)
            dst_file = os.path.join(dst_dir, name)
            shutil.move(src_file, dst_file)
        
        for name in dirs:
            os.rmdir(os.path.join(root, name))

# 使用示例
source_directory = 'C:/Users/User/Downloads/新增資料夾'  # 替换为你的源路径

extract_and_move_files(source_directory, source_directory)
