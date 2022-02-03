import pytest
from service import indexer


class TestIndexer:

    def test_sanity(self):
        """
        Sanity setup test
        """
        assert(1+1, 2)

    def test_indexer(self):
        """
        Indexer is callable
        """
        dummy_indexer = indexer.indexer
        assert(callable(dummy_indexer))