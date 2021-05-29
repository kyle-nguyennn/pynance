import pandas as pd
import numpy as np
from typing import List

class ColumnMetadata:
    name: str
    type: np.dtype

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

class TableMetadata:
    columnMetadataList: List[ColumnMetadata]
    def __init__(self, columnMetadataList):
        self.columnMetadataList = columnMetadataList

    def columnNames(self):
        return [meta.name for meta in self.columnMetadataList]

    def columnTypes(self):
        return [meta.type for meta in self.columnMetadataList]

    def dataFrame(self, data):
        df = pd.DataFrame(data, columns=self.columnNames())
        return df.astype({col: type for col, type in zip(self.columnNames(), self.columnTypes())})


CandlestickMetadata = TableMetadata([
    ColumnMetadata(name='Open time', type=np.int64),
    ColumnMetadata(name='Open', type=np.float),
    ColumnMetadata(name='High', type=np.float),
    ColumnMetadata(name='Low', type=np.float),
    ColumnMetadata(name='Close', type=np.float),
    ColumnMetadata(name='Volume', type=np.float),
    ColumnMetadata(name='Close time', type=np.int64),
    ColumnMetadata(name='Quote asset volume', type=np.float),
    ColumnMetadata(name='Number of trades', type=np.int64),
    ColumnMetadata(name='Taker buy base asset volume', type=np.float),
    ColumnMetadata(name='Taker buy quote asset volume', type=np.float),
    ColumnMetadata(name='Ignore', type=np.float),
])