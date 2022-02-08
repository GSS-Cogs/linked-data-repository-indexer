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

    def fetch_index(self, index: int):
        """
        Fetch index of queue
        """
        return self.queue[index]

    def drain_queue(self):
        """
        Drain queue
        """

        return self.queue.drain()


loop = asyncio.get_event_loop()


async def indexer_engine(worker, sleep_time):
    # TO DO: take items of queue to chosen queue
    while True:
        try:
            await asyncio.sleep(sleep_time)
            tasks = asyncio.ensure_future(worker.get_item())
            loop.run_until_complete(tasks)  # wait until tasks are done
        except Exception as err:
            # replace with logging system
            print('following error when taking off queue: %s' % (err))
        loop.close()


def fetch_queue():
    """
        Fetch queue to be used
        TBA production queue details
    """
    # queue = 'prod_queue_details'
    queue = list(range(10))
    return queue


async def main():
    queue = fetch_queue()
    sleep_time = 10
    worker = index_worker(queue)
    await indexer_engine(worker, sleep_time)
    print('---- done consuming')

asyncio.run(main())


if __name__ == '__main__':
    if 'start' in sys.argv:
        asyncio.run(main())
    if 'stop' in sys.argv:
        loop = asyncio.get_event_loop()
        loop.close()
