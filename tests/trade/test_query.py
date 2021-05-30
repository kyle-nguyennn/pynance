from pynance.trade import getAccountInfo
import unittest


class TestQuery(unittest.TestCase):
    def testGetAccountInfo(self):
        resp = getAccountInfo()
        self.assertIsNotNone(resp)

if __name__=='__main__':
    unittest.main()
