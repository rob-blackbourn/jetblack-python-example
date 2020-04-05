"""The poller"""

import asyncio
from asyncio import Event
import logging

LOGGER = logging.getLogger(__name__)


async def start_polling(
    poll_seconds: float,
    cancellation_event: Event
) -> None:
    LOGGER.info('Started polling')

    while not cancellation_event.is_set():
        try:
            LOGGER.info('Waiting for %s seconds', poll_seconds)
            await asyncio.wait_for(
                cancellation_event.wait(),
                timeout=poll_seconds
            )
        except asyncio.TimeoutError:
            pass

    LOGGER.info('Stopped polling')
