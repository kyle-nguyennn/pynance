import unittest

from pynance.model.enums import OrderType, OrderSide
from pynance.trade import sendOrder


class TestMarket(unittest.TestCase):
    def testOrderTestWithQty(self):
        resp = sendOrder('BTCUSDT', OrderSide.BUY, OrderType.MARKET, quantity=0.1, test=True)
        self.assertEqual({}, resp)

    def testOrderTestWithQuoteQty(self):
        resp = sendOrder('BTCUSDT', OrderSide.BUY, OrderType.MARKET, quoteOrderQty=10, test=True)
        self.assertEqual({}, resp)

    # def testOrderNew(self):
    #     resp = sendOrder('BTCUSDT', OrderSide.BUY, OrderType.MARKET, quantity=0.1, test=False)  # do send order to exchange
    #     self.assertIsNotNone(resp)

if __name__=='__main__':
    unittest.main()
