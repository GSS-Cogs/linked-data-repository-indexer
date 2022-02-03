import sys
import asyncio


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


async def indexer(worker, sleep_time):
    while True:
        # TO DO: take items of queue to chosen queue
        try:
            await asyncio.sleep(sleep_time)
            worker.get_item()
        except Exception as err:
            # replace with logging system
            print('following error when taking off queue: %s' % (err))


if __name__ == '__main__':
    queue_detail = ''
    sleep_time = 100
    worker = index_worker(queue_detail)
    if 'start' in sys.argv:
        asyncio.run(indexer(worker, sleep_time))
