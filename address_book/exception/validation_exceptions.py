from typing import Any, Optional

from starlette.exceptions import HTTPException


class InvalidRequestException(HTTPException):
    def __init__(self, message: str, param: str):
        self.status_code = 422
        self.message = message
        self.param = param
        super().__init__(
            status_code=422,
            detail={
                "error_code": self.status_code,
                "message": self.message,
                "param": self.param,
            },
        )


class AddressNotFoundException(HTTPException):
    def __init__(self, param: str = None):
        self.param = param
        super().__init__(
            status_code=422,
            detail={
                "error_code": 422,
                "message": "The following address does not exist in the system.",
                "param": self.param,
            },
        )
