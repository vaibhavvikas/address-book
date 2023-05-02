from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from address_book.app.config import settings

SQLITE_URL = f"sqlite:///./{settings.SQLITE_DATABASE}"

engine = create_engine(SQLITE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autoflush=False, bind=engine)
