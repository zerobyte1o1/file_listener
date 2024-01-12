import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MyHandler(FileSystemEventHandler):
    def __init__(self, filepath):
        self.filepath = filepath
        self.last_modified_time = os.path.getmtime(filepath)

    def on_modified(self, event):
        if not event.is_directory:
            file_modified_time = os.path.getmtime(self.filepath)
            if file_modified_time > self.last_modified_time:
                self.last_modified_time = file_modified_time
                # 文件被修改时触发
                print(f"File modified: {event.src_path}")


if __name__ == "__main__":
    path = "/path/to/file"  # 监听的文件路径

    event_handler = MyHandler(path)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
