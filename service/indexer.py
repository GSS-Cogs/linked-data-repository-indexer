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
            tasks = asyncio.ensure_future(worker)
            loop.run_until_complete(tasks)  # wait until tasks are done
        except Exception as err:
            # replace with logging system
            print('following error when taking off queue: %s' % (err))
        loop.close()


async def main():
    queue = asyncio.Queue()  # replace with production queue
    sleep_time = 10
    worker = index_worker(queue)

    # producers = [asyncio.create_task(producer(queue))
    #              for _ in range(3)] # example of producers on queue
    consumers = [asyncio.create_task(indexer_engine(worker, sleep_time))
                 for _ in range(10)]

    # with both producers and consumers running, wait for
    # the producers to finish
    # await asyncio.gather(*producers)
    print('---- done producing')

    # wait for the remaining tasks to be processed
    await queue.join()

    # cancel the consumers, which are now idle
    for c in consumers:
        c.cancel()


asyncio.run(main())


if __name__ == '__main__':
    if 'start' in sys.argv:
        asyncio.run(main())
    if 'stop' in sys.argv:
        loop = asyncio.get_event_loop()
        loop.close()
