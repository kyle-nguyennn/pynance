from pynance import send_signed_request
from pynance.model.enums import OrderSide, OrderType, OrderResponseType, HttpMethod

# support only market order for now
def sendOrder(symbol: str, side: OrderSide, type: OrderType, quantity: float, newOrderRespType: OrderResponseType = None,
              test = True):
    params = {
        'symbol': symbol,
        'side': side.name,
        'type': type.name,
        'quantity': quantity,
    }
    if not test:
        path = 'order'
        newOrderRespType = newOrderRespType or OrderResponseType.ACK
        params['newOrderRespType'] = newOrderRespType.value
    else:
        path = 'order/test'
    resp = send_signed_request(HttpMethod.POST.value, path, payload=params)
    return resp
