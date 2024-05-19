import os
from collections import defaultdict

def rename_files_in_directory(directory):
    # 用于存储每种扩展名的文件数量
    extension_counts = defaultdict(int)

    # 获取目录中的所有文件
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            # 获取文件的扩展名
            file_extension = os.path.splitext(filename)[1]

            # 更新扩展名的计数
            extension_counts[file_extension] += 1

            # 生成新的文件名
            new_filename = f"{file_extension[1:].lower()}_{extension_counts[file_extension]}{file_extension}"
            new_filepath = os.path.join(directory, new_filename)

            # 重命名文件
            os.rename(os.path.join(directory, filename), new_filepath)
            print(f"Renamed '{filename}' to '{new_filename}'")

# 使用示例
directory = "C:/Users/User/Downloads/新增資料夾"  # 替换为您的目录路径
rename_files_in_directory(directory)


# 幫整個資料夾內的檔案做排序