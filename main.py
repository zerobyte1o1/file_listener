import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            # 文件被修改时触发
            print(f"File modified: {event.src_path}")


if __name__ == "__main__":
    path = "c:/dish.listen"  # 监听的文件路径

    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
