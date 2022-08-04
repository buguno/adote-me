from functools import lru_cache
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


class DBSession:
    engine = create_engine('sqlite:///database.sqlite3', echo=True)

    @lru_cache
    def create_session(self) -> scoped_session:
        return scoped_session(
            sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self.engine
            )
        )

    def get_session(self) -> Generator[scoped_session, None, None]:
        database = self.create_session()

        try:
            yield database
        except Exception:
            database.remove()


session = DBSession()
