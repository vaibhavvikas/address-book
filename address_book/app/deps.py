from typing import Any

from collections.abc import Generator

from address_book.database.init_db import SessionLocal


def get_db() -> Generator:  # type: ignore
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
