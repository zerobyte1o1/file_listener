import os
import time

file_path = 'c:/dish_listen'
last_modified = None

while True:
    try:
        current_modified = os.path.getmtime(file_path)
        print(current_modified)
        if last_modified is None or current_modified > last_modified:
            print('文件被修改')
            last_modified = current_modified
            os.system('c:/yx-dish.exe')
            
    except Exception as e:
        print(f'Error occurred: {e}')

    time.sleep(3)
