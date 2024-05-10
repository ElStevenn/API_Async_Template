import asyncio, aiohttp
import os
from dotenv import load_dotenv
load_dotenv()

"""

"""

class ClientSend_Connection():
    def __init__(self):
        self.api_key = os.getcwd('API_KEY_DESTINATION')

        
    async def __aenter__(self):
        if self.session is None:
            self.session = aiohttp.ClientSession()
        return self

    async def __aexit__(self):
        if self.session:
            await self.session.close()
            self.session = None

    async def open_session(self):
        if self.session is None:
            self.session = aiohttp.ClientSession()

    async def close_session(self):
        if self.session:
            await self.session.close()
            self.session = None


if __name__ == "__main__":
    pass