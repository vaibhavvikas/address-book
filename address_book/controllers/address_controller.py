from typing import Any, List

import logging

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm.session import Session

from address_book.app import deps
from address_book.schema.address_schema import (
    AddressSchema,
    CreateAddressSchema,
    DeleteAddressSchema,
    UpdateAddressSchema,
)
from address_book.services import address_service
from address_book.validators import address_validator
from address_book.views import ErrorResponse

router = APIRouter(prefix="/address")
log = logging.getLogger(__name__)


@router.post("/create", response_model=AddressSchema)
def create_address(
    *, db: Session = Depends(deps.get_db), address_in: CreateAddressSchema
) -> Any:
    address_validator.validate_create_address_request(db, address_in)
    address = address_service.create_address(db, address_in)
    return address


@router.get(
    "",
    status_code=200,
    responses={422: {"model": ErrorResponse}},
    response_model=List[AddressSchema],
)
def get_all_address(
    *,
    db: Session = Depends(deps.get_db),
    lat: float = Query(None),
    long: float = Query(None),
    distance: int = Query(None),
) -> Any:
    addresses = address_service.get_all_address(db, lat, long, distance)
    return addresses


@router.get(
    "/{pid}",
    status_code=200,
    responses={422: {"model": ErrorResponse}},
    response_model=AddressSchema,
)
def get_address_by_pid(*, db: Session = Depends(deps.get_db), pid: str) -> Any:
    address = address_service.get_address(db, pid)
    return address


@router.put("/{pid}", response_model=AddressSchema)
def update_address(
    *, db: Session = Depends(deps.get_db), address_in: UpdateAddressSchema, pid: str
) -> Any:
    address = address_validator.validate_update_address_request(db, pid)
    address = address_service.update_address(db, address, address_in)
    return address


@router.delete("/{pid}", response_model=DeleteAddressSchema)
def delete_address(*, db: Session = Depends(deps.get_db), pid: str) -> Any:
    address = address_validator.validate_delete_address_request(db, pid)
    address = address_service.delete_address(db, pid)
    return address
