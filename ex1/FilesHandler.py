
######## http://brunorocha.org/python/watching-a-directory-for-file-changes-with-python.html 
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


class MyHandler(PatternMatchingEventHandler):
    patterns = ["*.txt", "*.csv"]

    @staticmethod
    def event_handler(event):
        """
        event.event_type
            'modified' | 'created' | 'moved' | 'deleted'
        event.is_directory
            True | False
        event.src_path
            path/to/observed/file
        """
        # the file will be processed there
        print event.src_path, event.event_type, 'at', time.ctime()  # print now only for degug
	print "\n"

    def on_moved(self, event):
        self.event_handler(event)

    def on_created(self, event):
        self.event_handler(event)

    def on_deleted(self, event):
	self.event_handler(event)

