import sys


class index_worker():
    """
        Index worker for queue(TBA) can put/get item on queue
    """

    def __init__(self, queue):
        self.queue = queue

    def put_item(self, item):
        """
        Put item on queue
        """
        return self.queue.put(item)

    def get_item(self):
        """
        Get item from queue
        """
        return self.queue.get()

    def fetch_index(self, index):
        """
        Fetch index of queue
        """
        return self.queue[index]

    def drain_queue(self):
        """
        Drain queue
        """

        return self.queue.drain()


def indexer(worker):
    while True:
        # TO DO: take items of queue to chosen queue
        try:
            worker.get_item()
        except Exception as err:
            # replace with logging system
            print('following error when taking off queue: %s' % (err))


if __name__ == '__main__':
    worker = index_worker()
    if 'start' in sys.argv:
        indexer(worker)
