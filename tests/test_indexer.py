import pytest
from mock import Mock
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
        dummy_indexer = indexer.indexer
        assert(callable(dummy_indexer))

    def test_index_worker(self):
        """
        Idex worker is callable
        """

        dummy_index_worker = indexer.index_worker
        assert(callable(dummy_index_worker))

    def test_get_item_queue(self):
        """
            Get last item from queue
        """
        dummy_queue = Mock()
        dummy_queue.return_value = 'test_item'
        dummy_index_worker = indexer.index_worker(dummy_queue)
        fetch_queue_item = dummy_index_worker.get_item()
        assert(fetch_queue_item, 'test_item')
