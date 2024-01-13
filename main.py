import os
import time

file_path = 'c:/dish.listen'

try:
    last_modified = os.path.getmtime(file_path)

except Exception as e:
    print(f'Error occurred: {e}')
    
while True:
    try:
        current_modified = os.path.getmtime(file_path)
        print(current_modified)
        if current_modified > last_modified:
            print('文件被修改')
            last_modified = current_modified
            os.system("""C:/"Program Files"/AIDish/Client/yx-dish.exe""")
            
    except Exception as e:
        print(f'Error occurred: {e}')

    time.sleep(3)
