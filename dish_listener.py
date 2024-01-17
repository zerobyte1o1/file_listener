import os
import threading
import time
import sys
import subprocess

file_path = 'c:/dish.listen'
auto_folder_path = 'c:\\winuitest-AIDish'
port = 8765


class Modify:
    last_modified = None
    current_modified = None

def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def check_file():
        if os.path.exists(auto_folder_path):
            try:
                # Get the process ID using the port
                netstat_process = subprocess.Popen(f'netstat -ano | findstr :{port}', shell=True, stdout=subprocess.PIPE)
                netstat_output = netstat_process.stdout.read().decode().split()
                if len(netstat_output) > 0:
                    pid = netstat_output[-1]
                    print(f'Port {port} is in use')
                    # Forcefully terminate the process using the port
                    subprocess.Popen(f'taskkill /F /PID {pid}', shell=True, stdout=subprocess.PIPE)
                    print(f'Process using port {port} terminated')
                    # Delete the folder
                else:
                    print(f'Port {port} is not in use')

            except Exception as e:
                print(f'Port {port} is not in use exc')

            if os.path.exists(auto_folder_path):
                os.system(f'rd /s /q {auto_folder_path}')
                print(f'Folder {auto_folder_path} deleted')
            else:
                print(f'Folder {auto_folder_path} not')
         


        else:
            print(f'Folder {auto_folder_path} does not exist')
        try:
            print("拉取代码")
            subprocess.Popen(
                'cmd /c "cd /d C:\\ && git clone https://liufj:lfj19980123@git.shifang.co/test/winuitest-AIDish.git && cd winuitest-AIDish && run.bat"',
                shell=True)
            # command = 'cmd /c "cd /d C:\\ && git clone https://liufj:lfj19980123@git.shifang.co/test/winuitest-AIDish.git && cd winuitest-AIDish && run.bat"'
            # subprocess.Popen(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).detach()
            restart_program()
        except Exception as e:
            print(f'Error occurred while cloning repository: {e}')


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
