from sqlalchemy import Column, Float, Integer, String

from address_book.database.base_class import Base


class AddressModel(Base):
    __tablename__ = "address"  # type: ignore

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    pid = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    country = Column(String, nullable=False)
    pincode = Column(String, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
