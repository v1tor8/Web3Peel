# test_web3peel.py
"""
Tests for Web3Peel module.
"""

import unittest
from web3peel import Web3Peel

class TestWeb3Peel(unittest.TestCase):
    """Test cases for Web3Peel class."""

    def test_initialization(self):
        """Test class initialization."""
        instance = Web3Peel()
        self.assertIsInstance(instance, Web3Peel)

    def test_run_method(self):
        """Test the run method."""
        instance = Web3Peel()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
