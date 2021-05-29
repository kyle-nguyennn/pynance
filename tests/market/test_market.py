import unittest
import vcr
from pynance.market import klines
from pynance.model import TimeInterval
import math


class TestMarket(unittest.TestCase):
    @vcr.use_cassette()
    def testKLines(self):
        data = klines('BTCUSDT', TimeInterval.fromString('1m'), endTime=1622242439999, limit=1)
        self.assertTrue(math.isclose(data.Close, 34866.17))
        print(data)

if __name__=='__main__':
    unittest.main()