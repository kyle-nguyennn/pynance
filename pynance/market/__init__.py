import os

import pandas as pd

from pynance.model import TimeInterval
from pynance import send_public_request

# Type aliases
from pynance.model.metadata import CandlestickMetadata

Timestamp = int

def klines(symbol: str, interval: TimeInterval, startTime: Timestamp = None, endTime: Timestamp = None, limit = 500)\
        -> pd.DataFrame:
    assert(limit <= 1000)
    path = 'klines'
    params = {
        'symbol': symbol,
        'interval': str(interval),
        'startTime': startTime,
        'endTime': endTime,
        'limit': limit
    }
    data = send_public_request(path, payload=params)
    df = CandlestickMetadata.dataFrame(data)
    df = df.set_index(pd.to_datetime(df['Close time'], unit='ms'))
    return df

