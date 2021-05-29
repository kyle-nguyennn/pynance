from pynance.model import TimeInterval, TimeIntervalUnit
import unittest

class TestEnums(unittest.TestCase):
    def testEqual(self):
        it1 = TimeInterval(1, TimeIntervalUnit.m)
        it2 = TimeInterval(1, TimeIntervalUnit.m)
        self.assertEqual(it1, it2)

    def testCreateTimeIntervalFromString(self):
        s = '1m'
        it: TimeInterval = TimeInterval.fromString(s)
        it2 = TimeInterval(1, TimeIntervalUnit.m)
        self.assertEqual(s, str(it))
        self.assertEqual(it2, it)


if __name__ == '__main__':
    unittest.main()