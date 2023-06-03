from databaseUtils import load_data, queries

def load_all_files(): #specific example, we assume that rentals.db already exists
    load_data.load_data(f"data/historia_przejazdow_2021-01.csv", "rentals")
    load_data.load_data(f"data/historia_przejazdow_2021-02.csv", "rentals")
    load_data.load_data(f"data/historia_przejazdow_2021-03.csv", "rentals")
    load_data.load_data(f"data/historia_przejazdow_2021-04.csv", "rentals")
    load_data.load_data(f"data/historia_przejazdow_2021-05.csv", "rentals")
    load_data.load_data(f"data/historia_przejazdow_2021-06.csv", "rentals")
    load_data.load_data(f"data/historia_przejazdow_2021-07.csv", "rentals")
    load_data.load_data(f"data/historia_przejazdow_2021-08.csv", "rentals")
    load_data.load_data(f"data/historia_przejazdow_2021-09.csv", "rentals")
    load_data.load_data(f"data/historia_przejazdow_2021-10.csv", "rentals")
    load_data.load_data(f"data/historia_przejazdow_2021-11.csv", "rentals")
    load_data.load_data(f"data/historia_przejazdow_2021-12.csv", "rentals")


if __name__ == "__main__":
    #load_all_files()
    queries.interface("rentals")