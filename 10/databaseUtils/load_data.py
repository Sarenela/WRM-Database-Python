import sys
import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy_utils import database_exists
from databaseUtils.tables import Base, Rentals,Stations,station_index
import datetime
import os

NONE_STATION = "Poza stacją"


def load_data_from_csv(data_file, engine):
    with open(data_file,"r", encoding="utf-8") as file:
        csv_reader=csv.reader(file)
        next(csv_reader)  #pomin naglowek
        stations_set = set()

        with Session(engine) as session:
            for row in csv_reader:
                rental = Rentals(
                    UID=row[0],
                    bike_num=row[1],
                    start_time=datetime.datetime.strptime(row[2], "%Y-%m-%d %H:%M:%S"),
                    end_time=datetime.datetime.strptime(row[3], "%Y-%m-%d %H:%M:%S"),
                    duration=row[6]
                )

                rent_station = session.query(Stations).filter_by(station_name=row[4]).first()
                if not rent_station:
                    rent_station = Stations(station_name=row[4])
                    session.add(rent_station)
                    session.flush()  # Flush to generate the ID

                return_station = session.query(Stations).filter_by(station_name=row[5]).first()
                if not return_station:
                    return_station = Stations(station_name=row[5])
                    session.add(return_station)
                    session.flush()  # Flush to generate the ID

                rental.rent_station = rent_station.UID
                rental.return_station = return_station.UID

                session.add(rental)
            session.commit()


def load_data(csv_file_path, database_path):
    if not os.path.exists(f"{database_path}.db"):
        print("The data base does not exist")
        return
    if not os.path.exists(csv_file_path):
        print("The csv file does not exist")
        return
    engine = create_engine(f"sqlite:///{database_path}.db")
    load_data_from_csv(csv_file_path,engine)





if __name__=="__main__":
        if len(sys.argv) > 2:
            engine = load_data(sys.argv[1],sys.argv[2])
        else:
            print("Please provide arguments: csv file containing rental info and database file")
            sys.exit(1)





