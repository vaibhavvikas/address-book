from address_book.database.base_class import Base
from address_book.database.init_db import engine
from address_book.model.address_model import AddressModel

__all__ = ["Base", "AddressModel"]

Base.metadata.create_all(engine)
