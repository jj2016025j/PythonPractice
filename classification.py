import os
import shutil

# 定義源目錄和目標目錄
source_dir = './test'
image_dir = './test/images'
video_dir = './test/videos'
audio_dir = './test/audios'
document_dir = './test/documents'
other_dir = './test/other'

# 確保目標資料夾存在
os.makedirs(image_dir, exist_ok=True)
os.makedirs(video_dir, exist_ok=True)
os.makedirs(audio_dir, exist_ok=True)
os.makedirs(document_dir, exist_ok=True)
os.makedirs(other_dir, exist_ok=True)

# 定義文件類型
image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp')
video_extensions = ('.mp4', '.avi', '.mov', '.mkv')
audio_extensions = ('.mp3', '.wav', '.flac', '.aac')
document_extensions = ('.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt')

# 遍歷源目錄中的所有文件
for filename in os.listdir(source_dir):
    file_path = os.path.join(source_dir, filename)
    
    # 如果是文件而不是文件夾
    if os.path.isfile(file_path):
        # 獲取文件擴展名
        file_extension = os.path.splitext(filename)[1].lower()
        
        # 根據文件類型移動文件
        if file_extension in image_extensions:
            shutil.move(file_path, os.path.join(image_dir, filename))
            print(f'Moved {filename} to {image_dir}')
        elif file_extension in video_extensions:
            shutil.move(file_path, os.path.join(video_dir, filename))
            print(f'Moved {filename} to {video_dir}')
        elif file_extension in audio_extensions:
            shutil.move(file_path, os.path.join(audio_dir, filename))
            print(f'Moved {filename} to {audio_dir}')
        elif file_extension in document_extensions:
            shutil.move(file_path, os.path.join(document_dir, filename))
            print(f'Moved {filename} to {document_dir}')
        else:
            shutil.move(file_path, os.path.join(other_dir, filename))
            print(f'File {filename} does not match any category, leaving in source directory.')
