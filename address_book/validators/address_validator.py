from fastapi import HTTPException
from sqlalchemy.orm.session import Session

from address_book.crud import crud_address
from address_book.exception import validation_exceptions
from address_book.model import address_model
from address_book.schema import address_schema


def validate_create_address_request(
    db: Session, address_in: address_schema.AddressSchema
):
    if not -90 <= address_in.latitude <= 90:
        raise validation_exceptions.InvalidRequestException(
            message="Invalid latitude: " + str(address_in.latitude), param="latitude"
        )

    if not -180 <= address_in.longitude <= 180:
        raise validation_exceptions.InvalidRequestException(
            message="Invalid longitude: " + str(address_in.longitude), param="longitude"
        )

    address = crud_address.address.get_by_lat_long(
        db=db, latitude=address_in.latitude, longitude=address_in.longitude
    )
    if address:
        raise validation_exceptions.InvalidRequestException(
            message="The address with following latitude and longitude already exist in the system.",
            param="latitude, longitude",
        )


def validate_update_address_request(
    db: Session, pid: str
) -> address_model.AddressModel:
    address = crud_address.address.get_by_pid(db=db, pid=pid)
    if not address:
        raise validation_exceptions.AddressNotFoundException("pid")
    return address


def validate_delete_address_request(
    db: Session, pid: str
) -> address_model.AddressModel:
    address = crud_address.address.get_by_pid(db=db, pid=pid)
    if not address:
        raise validation_exceptions.AddressNotFoundException("pid")
    return address
