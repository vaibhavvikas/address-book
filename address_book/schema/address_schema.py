from typing import Optional

from pydantic import BaseModel


class AddressSchema(BaseModel):
    pid: Optional[str] | None = None
    name: str
    city: str
    state: str
    country: str
    pincode: str
    latitude: float
    longitude: float

    class Config:
        orm_mode = True


class CreateAddressSchema(AddressSchema):
    ...


# Properties to receive via API on update
class UpdateAddressSchema(AddressSchema):
    name: str | None
    city: str | None
    state: str | None
    country: str | None
    pincode: str | None
    latitude: float | None
    longitude: float | None


class DeleteAddressSchema(AddressSchema):
    pid: str
    status = "Address deleted successfully"
