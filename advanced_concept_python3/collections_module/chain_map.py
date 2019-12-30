""" Talk about collections ChainMap

ChainMap is a class that provides the ability to link multiple mappings
together such that they end up being a single unit.

It accepts **map*, which means that a ChainMap will accept any number of
mappings or dictionaries and turn them into a single view that you can update.

This is especually useful if you want to set up defaults.
Let's pretend that we want to create an application that has some defaults.
The application will also be aware of the operatin systems envrironment,
the environment variable will override our default.
"""

from collections import ChainMap

car_parts = {'hood': 500, 'engine': 5000, 'front_door': 750}
car_options = {'A/C': 1000, 'Turbo': 2500, 'roolbar': 300}
car_accessories = {'cover': 100, 'hood_ornament': 150, 'seat_cover': 99}

car_pricing = ChainMap(car_accessories, car_options, car_parts)
print(car_pricing['hood'])

# Example
import argparse
import os

from collections import ChainMap


def main():
    app_defaults = {'username': 'admin', 'password': 'admin'}

    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username')
    parser.add_argument('-p', '--password')
    args = parser.parse_args()
    command_line_arguments = {key: value for key, value
                              in vars(args).items() if value}

    chain = ChainMap(command_line_arguments, os.environ,
                     app_defaults)
    print(chain['username'])


if __name__ == '__main__':
    main()
    os.environ['username'] = 'test'
    main()
