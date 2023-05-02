import logging

import uvicorn
from fastapi import APIRouter, FastAPI

from address_book.app.config import settings
from address_book.controllers.address_controller import router

app = FastAPI()

api_router = APIRouter()
log = logging.getLogger(__name__)


@api_router.get("/", status_code=200)
def root():
    """
    Root Get
    """
    return {"msg": "Welcome to Address Book!"}


app.include_router(api_router)
app.include_router(router)


def start():
    """Launched with `poetry run start` at root level"""
    log.Info("App is Starting")
    uvicorn.run(
        "address_book.__main__:app",
        host="127.0.0.1",
        port=8000,
        log_config=settings.LOG_PATH,
    )


if __name__ == "__main__":
    start()
