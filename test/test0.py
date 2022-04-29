import unittest
import src

class Test0(unittest.TestCase):
    def src_hello(self):
        self.assertEqual("hello", src.hello())

if __name__ == '__main__':
	unittest.main()