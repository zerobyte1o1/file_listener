import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class FileEventHandler(FileSystemEventHandler):
    def on_moved(self, event):
        if event.is_directory:
            print("directory modified:{0}".format(event.src_path))



if __name__ == "__main__":
    # 实例化Observer对象
    observer = Observer()
    event_handler = FileEventHandler()
    # 设置监听目录
    dis_dir = "/Users/liufangjing/Downloads/mit2meter.json"
    observer.schedule(event_handler, dis_dir, True)
    observer.start()
    try:
        while True:
            # 设置监听频率(间隔周期时间)
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    observer.join()
