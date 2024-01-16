import os
import time
import subprocess

file_path = 'c:/dish.listen'
auto_folder_path = 'c:\\winuitest-AIDish'
port = 8765
last_modified = None
try:
    last_modified = os.path.getmtime(file_path)

except Exception as e:
    print(f'Error occurred: {e}')

while True:
    try:
        current_modified = os.path.getmtime(file_path)  
    except Exception as e:
        print(f'Error occurred: {e}')
        continue
    print(time.time())
    if last_modified is None:
        break
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
                continue

            try:
                os.system(f'rd /s /q {auto_folder_path}')
                print(f'Folder {auto_folder_path} deleted')
            except Exception as e:
                print(f'Error occurred while deleting folder: {e}')
                continue

        else:
            print(f'Folder {auto_folder_path} does not exist')
        try:
            print("拉取代码")
            subprocess.Popen(
                'cmd /c "cd /d C:\\ && git clone https://liufj:lfj19980123@git.shifang.co/test/winuitest-AIDish.git && cd winuitest-AIDish && run.bat"',shell=True)
        except Exception as e:
            print(f'Error occurred while cloning repository: {e}')
            continue



    time.sleep(5)
