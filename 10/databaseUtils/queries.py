from sqlalchemy import select
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from databaseUtils.tables import Stations, Rentals




def get_stations_rentals(database_path):
    engine = create_engine(f"sqlite:///{database_path}.db")
    Session = sessionmaker(bind=engine)  # creating session
    session = Session()  #
    stations = session.query(Stations).all()  # Stations
    rentals = session.query(Rentals).all()  # Rentals
    return [stations, session, rentals]



def print_list_stations(stations):
    for station in stations:
        print(station.UID, station.station_name)
    print()

def print_list_bikes(rentals):
    bikes = set()
    for rental in rentals:
        bikes.add(rental.bike_num)
    for bike_num in bikes:
        print(bike_num)
    print()



def get_avg_time_station_start(session, station_name):
    average_duration = session.query(func.avg(Rentals.duration)
                                    ).join(Stations, Rentals.rent_station == Stations.UID
                                    ).filter(Stations.station_name == station_name).scalar()
    return average_duration

def get_avg_time_station_end(session, station_name):
    average_duration = session.query(func.avg(Rentals.duration)
                                    ).join(Stations, Rentals.return_station == Stations.UID
                                    ).filter(Stations.station_name == station_name).scalar()
    return average_duration

def count_distinct_bikes(session, station_name):
    statement = select(func.count(func.distinct(Rentals.bike_num))
                ).join(Stations, Rentals.return_station == Stations.UID
                ).where(Stations.station_name == station_name)
    result = session.execute(statement).scalar()
    return result


def find_longest_rental_duration_for_bike(session, bike_num):
    query = session.query(func.max(Rentals.duration)).filter(Rentals.bike_num == bike_num).scalar()
    return query



def print_menu():
    print(f"\nMENU")
    print(f"choose an option:")
    print("1 : print all stations")
    print("2 : print all bikes")
    print("3 : average duration of rentals started at a give station")
    print("4 : average duration of rentals ended at a give station")
    print("5 : number of different bikes parked at a given station")
    print("6 : longest rental duration for a given bike number")
    print(f"exit : exit \n")



def interface(database_path):
    s = get_stations_rentals(database_path)
    stations = s[0]
    session = s[1]
    rentals = s[2]
    while True:
        print_menu()
        user_input = input("option: ")
        if user_input == "exit":
            break
        elif user_input == '1':
            print_list_stations(stations)
        elif user_input == '2':
            print_list_bikes(rentals)
        elif user_input == '3':
            station = input("input a station name: ")
            print(get_avg_time_station_start(session,station))
        elif user_input == '4':
            station = input("input a station name: ")
            print(get_avg_time_station_end(session, station))
            print()
        elif user_input == '5':
            station = input("input a station name: ")
            print(count_distinct_bikes(session, station))
            print()
        elif user_input == '6':
            user = input("input a station name: ")
            print(find_longest_rental_duration_for_bike(session, user))
            print()
        else:
            print("the option does not exist")



if __name__ == "__main__":
    interface("rentals.db")