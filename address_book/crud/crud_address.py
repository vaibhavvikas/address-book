from typing import Any, Dict, Optional, Union

from sqlalchemy import Numeric, cast
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import text

from address_book.crud.base import CRUDBase
from address_book.model.address_model import AddressModel
from address_book.schema.address_schema import CreateAddressSchema, UpdateAddressSchema
from address_book.utils import helper


class CRUDAddress(CRUDBase[AddressModel, CreateAddressSchema, UpdateAddressSchema]):
    """CRUD object with default methods to Create, Read, Update, Delete (CRUD).

    Args:
        model: A Pydantic model (schema) class
        schema: A SQLAlchemy model class.
    """

    def get_by_lat_long(
        self, db: Session, *, latitude: float, longitude: float
    ) -> Optional[AddressModel]:
        return (
            db.query(AddressModel)
            .filter(
                AddressModel.latitude == latitude, AddressModel.longitude == longitude
            )
            .first()
        )

    def get_all_by_lat_long(
        self, db: Session, *, latitude: float = None, longitude: float = None
    ) -> Optional[AddressModel]:
        query = db.query(AddressModel)
        if latitude is not None and longitude is not None:
            query = query.filter(
                AddressModel.latitude == latitude, AddressModel.longitude == longitude
            )
        elif latitude is not None:
            query = query.filter(AddressModel.latitude == latitude)
        elif longitude is not None:
            query = query.filter(AddressModel.longitude == longitude)
        return query.all()

    def get_by_lat_long_dis(
        self, db: Session, *, latitude: float, longitude: float, distance: int
    ) -> Optional[list[AddressModel]]:
        # Using Haversine Formula to calculate distance
        return (
            db.query(AddressModel)
            .filter(
                (
                    6371000
                    * cast(
                        text(
                            "acos(cos(radians(:lat)) * cos(radians(latitude)) * cos(radians(longitude) - radians(:long)) + sin(radians(:lat)) * sin(radians(latitude)))"
                        ),
                        Numeric,
                    )
                ).params(lat=latitude, long=longitude)
                < (distance * 1000)
            )
            .all()
        )


address = CRUDAddress(AddressModel)
