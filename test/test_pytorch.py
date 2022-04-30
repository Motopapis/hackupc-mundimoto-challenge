import unittest
import logging

class test_pytorch(unittest.TestCase):
    def test_pytorch_import(self):
        try:
            import torch
            is_ok = True
        except Error as e:
            logging.error(e)
            is_ok = False
        
        self.assertTrue(is_ok)