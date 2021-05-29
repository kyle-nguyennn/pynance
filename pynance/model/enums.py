from enum import Enum

class HttpMethod(Enum):
    GET = 'get'
    POST = 'post'
    UPDATE = 'update'
    DELETE = 'delete'

class TimeIntervalUnit(Enum):
    MINUTES = 'm'
    HOURS = 'h'
    DAYS = 'd'
    WEEKS = 'w'
    MONTHS = 'M'

    @classmethod
    def valueToNameMap(cls):
        return {v.value: v for _, v in cls.__members__.items()}
    @classmethod
    def fromValue(cls, value):
        return TimeIntervalUnit.valueToNameMap().get(value, cls.MINUTES)

class OrderSide(Enum):
    BUY = 'BUY'
    SELL = 'SELL'

class OrderType(Enum):
    MARKET = 'MARKET'
    LIMIT = 'LIMIT'

class OrderResponseType(Enum):
    ACK = 'ACK'
    RESULT = 'RESULT'
    FULL = 'FULL'
