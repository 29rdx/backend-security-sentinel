import time

class ScanWorker:
    def __init__(self, target_queue: list):
        self.queue = target_queue

    def process_next(self):
        if not self.queue:
            return None
        return self.queue.pop(0)
