import pytest
import asyncio
from unittest import IsolatedAsyncioTestCase
from mock import Mock, patch
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

    def test_get_index_queue_item(self):
        """
        Get positional item from queue
        """

        dummy_queue = list(range(10))
        dummy_index_worker = indexer.index_worker(dummy_queue)
        fetch_queue_item = dummy_index_worker.fetch_index(1)
        assert(fetch_queue_item, 1)


class TestAsyncMain(IsolatedAsyncioTestCase):

    async def test_async_main(self):
        """

        """
        async_worker = await indexer.main()
        # lets test it runs and doesnt return anything
        self.assertEquals(async_worker, None)
