from PIL import Image

# 創建一個新的圖像 (RGB模式, 100x100 大小, 紅色)
image = Image.new('RGB', (100, 100), 'red')

# 保存圖像
image.save('./test/example_image.png')

print('Image created and saved as example_image.png')

import cv2
import numpy as np

# 定義影片屬性
width, height = 640, 480
fps = 30
duration = 5  # 影片持續時間（秒）
output_filename = './test/example_video.avi'

# 創建影片寫入對象
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(output_filename, fourcc, fps, (width, height))

# 生成影片
for i in range(int(fps * duration)):
    # 創建一個隨機顏色的畫面
    frame = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
    out.write(frame)

# 釋放資源
out.release()

print(f'Video created and saved as {output_filename}')

from pydub import AudioSegment
from pydub.generators import Sine

# 生成一個1秒的A4音（440Hz）
tone = Sine(440).to_audio_segment(duration=1000)

# 保存音頻文件
tone.export('./test/example_audio.wav', format='wav')

print('Audio created and saved as example_audio.wav')


# 成功 重覆檔名會覆蓋