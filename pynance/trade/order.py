from pynance import send_signed_request
from pynance.model.enums import OrderSide, OrderType, OrderResponseType, HttpMethod

# support only market order for now
def sendOrder(symbol: str, side: OrderSide, type: OrderType, quantity: float = None, quoteOrderQty: float = None,
              newOrderRespType: OrderResponseType = None, test = True):
    params = {
        'symbol': symbol,
        'side': side.name,
        'type': type.name,
    }
    qt_key = 'quantity' if quantity else 'quoteOrderQty'
    qt_value = quantity or quoteOrderQty
    params[qt_key] = qt_value
    if not test:
        path = 'order'
        newOrderRespType = newOrderRespType or OrderResponseType.ACK
        params['newOrderRespType'] = newOrderRespType.value
    else:
        path = 'order/test'
    resp = send_signed_request(HttpMethod.POST.value, path, payload=params)
    return resp
