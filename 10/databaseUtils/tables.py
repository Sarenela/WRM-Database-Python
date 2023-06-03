from sqlalchemy import ForeignKey,String,Integer,DateTime,Column,Index
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
import sys

Base = declarative_base()


class Rentals(Base):
    __tablename__="Rentals"
    UID = Column(Integer, primary_key=True)
    bike_num = Column(String(30))
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    rent_station= Column(Integer,ForeignKey("Stations.UID"))
    return_station = Column(Integer, ForeignKey("Stations.UID"))
    duration = Column(Integer)

    def __repr__(self) -> str:
        return f"Rental(UID={self.UID!r}, bike number ={self.bike_num!r}, rent date={self.start_time!r}, return date={self.end_time!r}, rent station={self.rent_station!r}, return station= {self.return_station!r}, duration={self.duration!r})"

class Stations(Base):
    __tablename__="Stations"
    UID = Column(Integer,primary_key=True, autoincrement=True)
    station_name= Column(String)

    def __repr__(self) -> str:
        return f"Station(UID={self.UID!r},  name={self.station_name!r})"

station_index = Index("id_station_name", Stations.station_name)


def create_database(database_file):
    engine = create_engine(f"sqlite:///{database_file}.db", echo=True)
    Base.metadata.create_all(engine)
    return engine


if __name__=="__main__":
    if len(sys.argv) > 1:
      create_database(sys.argv[1])
    else:
        print("Please provide a database name as a command-line argument.")
        sys.exit(1)
