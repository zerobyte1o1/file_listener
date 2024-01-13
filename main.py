import os
import time

file_path = '/Users/liufangjing/Downloads/mit2meter.json'
last_modified = None

while True:
    current_modified = os.path.getmtime(file_path)
    print(current_modified)
    if last_modified is None or current_modified > last_modified:
        print('文件被修改')
        last_modified = current_modified

    time.sleep(3)
