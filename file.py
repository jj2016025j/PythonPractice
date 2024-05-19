import os
import shutil

# 定義要生成的文件路徑和名稱
file_path = './for_file_test.txt'

# 使用 'w' 模式打開文件，這將創建文件（如果文件不存在）或截斷文件（如果文件已存在）
with open(file_path, 'w') as file:
    file.write("這是一個剛創建的檔案的第一行字\n")
print(f'檔案 {file_path} 被成功創建')

with open(file_path, 'w') as file:
    file.write("我覆蓋了原本的檔案\n")
print(f'檔案 {file_path} 成功被覆蓋')

# 使用 'a' 模式打開文件，這將在文件末尾追加內容
with open(file_path, 'a') as file:
    file.write("這段是改寫的內容\n")
print(f'修改文件 {file_path} 成功')

# 使用 'r' 模式打開文件，這將以只讀模式打開文件
with open(file_path, 'r') as file:
    content = file.read()
print(f'讀取文件 {file_path} 內容:\n{content}')

# 檢查文件是否存在
if os.path.exists(file_path):
    print(f'檔案 {file_path} 存在')
else:
    print(f'檔案 {file_path} 不存在')

# 定義源文件路徑和目標文件路徑
source_file = './for_file_test.txt'
target_dir = './test'

# 確保目標文件夾存在
os.makedirs(target_dir, exist_ok=True)

# 獲取文件名和擴展名
base_name = os.path.basename(source_file)
print(f'這是文件名稱 {base_name}')
name, ext = os.path.splitext(base_name)

# 初始化序號
counter = 1
new_name = f"{name}{ext}"
print(f'這是新的文件名稱 {new_name}')
new_path = os.path.join(target_dir, new_name)
print(f'這是包含路徑的文件名稱 {new_path}')

# 檢查並生成唯一文件名
while os.path.exists(new_path):
    new_name = f"{name}_{counter}{ext}"
    new_path = os.path.join(target_dir, new_name)
    print(f'發現重複檔案 計算編號 {counter}')
    counter += 1

# 移動並重命名文件
shutil.move(source_file, new_path)
print(f'移動並重命名文件 {new_path}')

# 定義來源及目標
original_file = new_path
new_file = './test/rename_file.txt'
  
# # 重命名文件
# os.rename(original_file, new_file)
# print(f'檔案 {original_file} 重新命名為 {new_file}')

# os.remove(new_file)
# print(f'檔案 {file_path} 刪除成功')
