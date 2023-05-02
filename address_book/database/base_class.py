import typing

from sqlalchemy.ext.declarative import as_declarative, declared_attr

class_registry: dict[typing.Any, typing.Any] = {}


@as_declarative(class_registry=class_registry)
class Base:
    id: typing.Any
    pid: str
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr  # type: ignore
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
