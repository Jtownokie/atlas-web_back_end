#!/usr/bin/env python3
""" DB Class Module """
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from user import Base, User
from typing import TypeVar


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db")
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ Adds User to Database """
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """ Find a user by keyword argument filtering """
        query = self._session.query(User)
        for key, value in kwargs.items():
            if key not in User.__table__.columns.keys():
                raise InvalidRequestError()
            query = query.filter(getattr(User, key) == value)

        user = query.first()

        if user is None:
            raise NoResultFound()

        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """ Updates User Columns """
        user = self.find_user_by(id=user_id)
        for key, value in kwargs.items():
            if key not in User.__table__.columns.keys():
                raise ValueError()
            setattr(user, key, value)
        self._session.commit()
        return None
