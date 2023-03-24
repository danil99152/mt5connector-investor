from fastapi import APIRouter
from starlette.responses import JSONResponse

from service.model import MetaTrader5Wrapper

router = APIRouter(prefix='/investor')
mt5wrapper = MetaTrader5Wrapper()


@router.get('/ping', response_class=JSONResponse)
async def ping():
    response: str = 'pong'
    return response


@router.post('/init-terminal/', response_class=JSONResponse)
async def init_terminal(data: dict):
    mt5wrapper.init_mt(data)
