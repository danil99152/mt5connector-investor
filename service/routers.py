from fastapi import APIRouter
from starlette.responses import JSONResponse

from service.model import MetaTrader5Wrapper

router = APIRouter(prefix='/investor')
mt5wrapper = MetaTrader5Wrapper()


@router.get('/ping', response_class=JSONResponse)
async def ping():
    response: str = 'pong'
    return response


@router.post('/init/', response_class=JSONResponse)
async def init(data: dict):
    return mt5wrapper.init_mt(data)


@router.get('/get-positions/', response_class=JSONResponse)
async def get_positions():
    return mt5wrapper.get_positions()


@router.get('/get-account-info/', response_class=JSONResponse)
async def get_account_info():
    return mt5wrapper.get_account_info()


@router.get('/get-symbol-info-tick/', response_class=JSONResponse)
async def get_symbol_info_tick(params: dict):
    return mt5wrapper.get_symbol_info_tick(symbol=params.get('symbol'))


@router.get('/get-trade-action-deal/', response_class=JSONResponse)
async def get_trade_action_deal():
    return mt5wrapper.get_trade_action_deal()


@router.get('/get-order-type-buy/', response_class=JSONResponse)
async def get_order_type_buy():
    return mt5wrapper.get_order_type_buy()


@router.get('/get-order-type-sell/', response_class=JSONResponse)
async def get_order_type_sell():
    return mt5wrapper.get_order_type_sell()


@router.get('/get-order-time-gtc/', response_class=JSONResponse)
async def get_order_time_gtc():
    return mt5wrapper.get_order_time_gtc()


@router.get('/get-order-filling-ioc/', response_class=JSONResponse)
async def get_order_filling_ioc():
    return mt5wrapper.get_order_filling_ioc()


@router.post('/order-send/', response_class=JSONResponse)
async def order_send(request: dict):
    return mt5wrapper.order_send(request)


@router.get('/get-history-deals-get-with-date/', response_class=JSONResponse)
async def get_history_deals_get_with_date(params: dict):
    return mt5wrapper.get_history_deals_get_with_date(date_from=params.get('date_from'),
                                                      date_to=params.get('date_to'))


@router.get('/get-history-deals-get-with-pos-id/', response_class=JSONResponse)
async def get_history_deals_get_with_pos_id(params: dict):
    return mt5wrapper.get_history_deals_get_with_pos_id(position_id=params.get('position_id'))
