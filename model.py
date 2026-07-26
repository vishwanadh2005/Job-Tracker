from sqlalchemy import Column, Integer, String
from database import Base



class Application(Base):

    __tablename__ = "applications"


    id = Column(
        Integer,
        primary_key=True
    )

    company = Column(
        String
    )

    position = Column(
        String
    )

    status = Column(
        String
    )

    email = Column(
        String
    )
