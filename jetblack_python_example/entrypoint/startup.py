"""The entry point for starting the server.
"""

import sys

from jetblack_python_example import start_server


def main():
    """Start the server with the command line args.
    """
    start_server(sys.argv)


if __name__ == "__main__":
    main()
