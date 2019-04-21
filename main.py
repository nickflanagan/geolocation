#!/usr/bin/env python3

import network_utilities


def main():
    # get [latitude, longitude, accuracy]
    coordinates = network_utilities.return_coordinates()
    latitude = coordinates[0]
    longitude = coordinates[1]
    accuracy = coordinates[2]
    print(f"You are within {accuracy}m of {latitude}, {longitude}")
    print()
    print(f"https://www.google.com/maps/place/{latitude},{longitude}")

    address = network_utilities.get_address(latitude, longitude)

    print()
    print(address + '\n')


if __name__ == "__main__":
    main()
