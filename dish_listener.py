import os
import threading
import time
import subprocess

file_path = 'c:/dish.listen'
auto_folder_path = 'c:\\winuitest-AIDish'
port = 8765


class Modify:
    last_modified = None
    current_modified = None


def check_file():
        if os.path.exists(auto_folder_path):
            
            # Get the process ID using the port
            netstat_output = subprocess.check_output(f'netstat -ano | findstr :{port}', shell=True)
            pid = netstat_output.decode().split()[-1]
            print(f'Port {port} is in use')
            # Forcefully terminate the process using the port
            subprocess.check_output(f'taskkill /F /PID {pid}', shell=True)
            print(f'Process using port {port} terminated')
            # Delete the folder
            

            
            os.system(f'rd /s /q {auto_folder_path}')
            print(f'Folder {auto_folder_path} deleted')
            
        else:
            print(f'Folder {auto_folder_path} does not exist')
       
        print("拉取代码")
        subprocess.Popen(
            'cmd /c "cd /d C:\\ && git clone https://liufj:lfj19980123@git.shifang.co/test/winuitest-AIDish.git && cd winuitest-AIDish && run.bat"',
            shell=True)
       


if os.path.exists(file_path):
    Modify.last_modified = os.path.getmtime(file_path)
    Modify.current_modified = os.path.getmtime(file_path)
else:
    Modify.last_modified = None
    Modify.current_modified = None

while True:
    print(time.time())
    try:
        Modify.current_modified = os.path.getmtime(file_path)
        if Modify.current_modified is None:
            continue
        if Modify.current_modified > Modify.last_modified:
            print('文件被修改')
            Modify.last_modified = Modify.current_modified
            thread = threading.Thread(target=check_file)
            thread.daemon = True
            thread.start()
    except Exception as e:
        print(e)
    time.sleep(5)
