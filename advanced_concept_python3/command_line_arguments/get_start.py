""" Basic argparse concept

To process command line arguments in Python
Here we use built-in module call argparse
Another decorator wrap call click https://github.com/pallets/click
https://realpython.com/command-line-interfaces-python-argparse/
https://realpython.com/comparing-python-command-line-parsing-libraries-argparse-docopt-click/
"""
import argparse


def get_args():
    parser = argparse.ArgumentParser(
        description="A simple argument parse",
        epilog="This is where you might put exmaple usage"
    )

    # required argument
    # --long version to match -x
    parser.add_argument('-x', '--execute', action="store", required=True,
                        help='Help text for option X')

    # optional arguments
    parser.add_argument('-y', help='Help text for option Y', default=False)
    parser.add_argument('-z', help='Help text for option Z', type=int)

    # exclusive group
    # either A or B
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-a', help='Help text for option a')
    group.add_argument('-b', help='Help text for option b', default=False)

    print(parser.parse_args())


if __name__ == '__main__':
    get_args()
    # parser.print_help()
