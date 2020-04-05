"""Server"""

import argparse
import asyncio
from asyncio import AbstractEventLoop, Event
import logging
import logging.config
import os
import os.path
import signal
from typing import Any, List, Mapping

import pkg_resources
import yaml

from .constants import APP_NAME
from .poller import start_polling


LOGGER = logging.getLogger(__name__)


def _parse_args(argv: List[str]):
    parser = argparse.ArgumentParser(
        description=APP_NAME,
        add_help=False
    )

    parser.add_argument(
        '--help', help='Show usage',
        action='help'
    )

    parser.add_argument(
        '-f', '--config', help='Path to the configuration file',
        default=pkg_resources.resource_filename(__name__, 'config.yaml'),
        action='store', dest='CONFIG_FILE'
    )

    return parser.parse_args(argv)


def _load_config(filename: str) -> Mapping[str, Any]:
    with open(filename, 'rt') as file_ptr:
        return yaml.load(file_ptr, Loader=yaml.FullLoader)


def _initialise_logging(config: Mapping[str, Any]) -> None:
    python_env = os.environ.get('PYTHON_ENV')
    key = f'logging_{python_env}' if python_env else 'logging'
    if key in config:
        logging.config.dictConfig(config[key])


def _make_cancellation_event(loop: AbstractEventLoop) -> Event:
    cancellation_event = Event()

    def cancel(name, num):
        msg = f'Received signal {name}'
        if num == signal.SIGINT:
            LOGGER.info(msg)
        else:
            LOGGER.warning(msg)
        cancellation_event.set()

    for signame in ['SIGINT', 'SIGTERM']:
        signum = getattr(signal, signame)
        loop.add_signal_handler(signum, cancel, signame, signum)

    return cancellation_event


def start_server(argv: List[str]) -> None:
    args = _parse_args(argv[1:])
    config = _load_config(args.CONFIG_FILE)
    _initialise_logging(config)

    loop = asyncio.get_event_loop()
    cancellation_event = _make_cancellation_event(loop)

    poll_seconds: int = config['app']['poll_seconds']
    start_message: str = os.path.expandvars(config['app']['start_message'])
    stop_message: str = os.path.expandvars(config['app']['stop_message'])

    LOGGER.info('Start message: "%s"', start_message)

    loop.run_until_complete(
        start_polling(poll_seconds, cancellation_event)
    )

    LOGGER.info('Stop message: "%s"', stop_message)

    logging.shutdown()
