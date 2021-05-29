from pynance.model.enums import TimeIntervalUnit
import re

class TimeInterval:
    value: int
    unit: TimeIntervalUnit

    @classmethod
    def fromString(cls, s):
        m = re.match(r'(?P<value>\d+)(?P<unit>\w+)', s)
        if m:
            d = m.groupdict()
            return TimeInterval(int(d['value']), TimeIntervalUnit[d['unit']])

    @classmethod
    def allowedIntervals(cls):
        return ['1m','3m','5m','15m','30m','1h','2h','4h','6h','8h','12h','1d','3d','1w','1M']

    def __init__(self, value: int, unit:TimeIntervalUnit):
        assert isinstance(value, int)
        assert isinstance(unit, TimeIntervalUnit)
        self.value = value
        self.unit = unit
        if str(self) not in self.allowedIntervals():
            raise Exception(f"Interval not in allowed list: {self.allowedIntervals()}")

    def __str__(self):
        return f"{self.value}{self.unit.name}"

    def __eq__(self, other):
        return self.unit == other.unit and self.value == other.value