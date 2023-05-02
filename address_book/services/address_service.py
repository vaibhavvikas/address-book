import logging

from fastapi import HTTPException
from sqlalchemy.orm.session import Session

from address_book.crud import crud_address
from address_book.exception import validation_exceptions
from address_book.model.address_model import AddressModel
from address_book.schema.address_schema import (
    AddressSchema,
    CreateAddressSchema,
    UpdateAddressSchema,
)

log = logging.getLogger(__name__)


def create_address(db: Session, address_in: CreateAddressSchema) -> AddressSchema:
    address = crud_address.address.create(db=db, obj_in=address_in)
    return address


def get_address(db: Session, pid: str) -> AddressModel:
    address = crud_address.address.get_by_pid(db=db, pid=pid)
    if not address:
        log.error(
            "[address_service][get_address] Address not found in the system: " + pid
        )
        raise validation_exceptions.AddressNotFoundException("pid")
    return address


def get_all_address(
    db: Session, lat: float = None, long: float = None, distance: int = None
) -> AddressModel:
    # Case A: Distance is passed that means lat and long will be used to get based on distancce in kms:
    if distance != None and lat != None and long != None:
        addresses = crud_address.address.get_by_lat_long_dis(
            db=db, latitude=lat, longitude=long, distance=distance
        )
    # Case B: We query based on the params
    if distance == None:
        addresses = crud_address.address.get_all_by_lat_long(
            db=db, latitude=lat, longitude=long
        )

    if len(addresses) < 1:
        log.error(
            "[address_service][get_all_address] There are no addresses in the system"
        )
        raise validation_exceptions.AddressNotFoundException()
    return addresses


def update_address(
    db: Session, address: AddressModel, address_in: UpdateAddressSchema
) -> AddressSchema:
    address = crud_address.address.update(db=db, db_obj=address, obj_in=address_in)
    return address


def delete_address(db: Session, pid: str):
    address = crud_address.address.remove(db=db, pid=pid)
    return address
