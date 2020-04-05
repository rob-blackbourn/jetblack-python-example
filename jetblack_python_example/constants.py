"""Constants"""

import socket
import pkg_resources

HOST = socket.gethostname()
FQDN = socket.getfqdn()
APP_NAME = 'jetblack-python-example'
VERSION = pkg_resources.get_distribution(APP_NAME).version
