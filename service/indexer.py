import sys
import asyncio
from .schema import validate_schema


class index_worker:
    """
        Index worker for queue(TBA), including:
        - put items on queue
        - get items on queue
        - drain items on queue
        - get positional items of queue
    """

    def __init__(self, queue):
        self.queue = queue

    def put_item(self, item):
        """
        Put item on queue
        """
        return self.queue.put(item)

    def get_message(self):
        """
        Get one item from queue
        """
        queue_item = self.queue.pop()
        if validate_schema(queue_item):
            return queue_item

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

    def message_recieved(self, item):
        """

        """
        # check is one message recieved
        if item:
            return True



async def indexer_engine(worker=None, sleep_time=None):
    """
        Engine of the indexer where tasks ran until complete, includes:
        - worker: queue and its tasks
        - sleep_time: amount to wait for an asyncio task
    """
    while True:
        try:
            await asyncio.sleep(sleep_time)
            queue_item = worker.get_message()
            if queue_item:
                    # Confirm one item recieved
                    confirm_item_reciept = worker.message_recieved(queue_item)
                    if confirm_item_reciept:
                        print(queue_item)# do something with the result
        except Exception as err:
            # replace with logging system
            print('following error when taking off queue: %s' % (err))
            return


def fetch_queue():
    """
        Fetch queue to be used
        TBA production queue details
    """
    # queue = 'prod_queue_details' TO DO: consume production queue
    queue = list(range(10))
    return queue


async def main():
    """
        Running the asyncio tasks, include:
        - fetch queue
        - associate queue to index worker
        - assign tasks to the worker
    """
    queue = fetch_queue()
    sleep_time = 1
    worker = index_worker(queue)
    await indexer_engine(worker, sleep_time)
    print('---- done consuming----')


if __name__ == '__main__':
    """
        'start' and 'stop' capability for the indexer
    """
    if 'start' in sys.argv:
        print('start indexer service')
        asyncio.run(main())
    elif 'stop' in sys.argv:
        print('stop indexer service')
        loop = asyncio.get_event_loop()
        loop.close()
