import json
from service import indexer



class TestIndexer:

    def test_sanity(self):
        """
        Sanity setup test
        """
        assert(1 + 1, 2)

    def test_indexer(self):
        """
        Indexer is callable
        """
        dummy_indexer = indexer.indexer_engine
        assert(callable(dummy_indexer))

    def test_index_worker(self):
        """
        Index worker is callable
        """

        dummy_index_worker = indexer.IndexWorker
        assert(callable(dummy_index_worker))

    def test_get_message_queue(self):
        """
            Get last item from queue

        """
        dummy_queue = [json.dumps({'item_one': 'test',
                                    'item_two': 10})]
        dummy_index_worker = indexer.IndexWorker(dummy_queue)
        fetch_queue_item = dummy_index_worker.get_message()
        assert(fetch_queue_item, {'item_one': 'test',
                                    'item_two': 10})

    def test_get_index_queue_item(self):
        """
        Get positional item from queue
        """

        dummy_queue = list(range(10))
        dummy_index_worker = indexer.IndexWorker(dummy_queue)
        fetch_queue_item = dummy_index_worker.fetch_index(1)
        assert(fetch_queue_item, 1)


class TestAsyncMain():

    def test_async_main(self):
        """
            Async Indexer main is callable

        """
        # lets test it if async indexer is callable
        assert (callable(indexer.main))
