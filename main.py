import os
import time
import shutil
import subprocess

file_path = 'c:/dish.listen'
auto_folder_path = 'c:/winuitest-AIDish'
port = 8765
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
            if os.path.exists(auto_folder_path):
                try:
                    # Get the process ID using the port
                    netstat_output = subprocess.check_output(f'netstat -ano | findstr :{port}', shell=True)
                    pid = netstat_output.decode().split()[-1]
                    print(f'Port {port} is in use')
                    # Forcefully terminate the process using the port
                    subprocess.check_output(f'taskkill /F /PID {pid}', shell=True)
                    print(f'Process using port {port} terminated')
                    # Delete the folder
                except subprocess.CalledProcessError:
                    print(f'Port {port} is not in use')

                shutil.rmtree(auto_folder_path)
                print(f'Folder {auto_folder_path} deleted')
                Error
                occurred: [WinError 5]
                拒绝访问。: 'c:/winuitest-AIDish\\.git\\objects\\pack\\pack-a9ea86a55099f1a43c8bc00c1a489fbad9c44183.idx'


            else:
                print(f'Folder {auto_folder_path} does not exist')     
    except Exception as e:
        print(f'Error occurred: {e}')

    time.sleep(3)
