import network_utilities


def main():
    # get [lattitude, longitude, accuracy]
    coordinates = network_utilities.return_coordinates()
    lattitude = coordinates[0]
    longitude = coordinates[1]
    accuracy = coordinates[2]
    print(f"Your are within {accuracy}m of {lattitude}, {longitude}")



if __name__ == "__main__":
    main()
