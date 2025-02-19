import logging

import asyncio

import aiohttp
from bs4 import BeautifulSoup

from app.config.settings import REQUEST_URL
from app.db.session import get_session

logger = logging.getLogger(__name__)

async def main():
    limit: int = 25
    async for db_session in get_session():
        async with aiohttp.ClientSession() as aiohttp_session:
            async with aiohttp_session.get(REQUEST_URL) as response:
                logger.info("___response_content___")
                logger.info(response.content)
                res_page = await response.content.read()
                soup = BeautifulSoup(res_page, 'html.parser')
                soup.find_all('div')
            await asyncio.sleep(1)


if __name__ == '__main__':
    asyncio.run(main())
