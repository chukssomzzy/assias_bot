from loguru import logger
from data import config
from pyrogram.client import Client
from data.config import USE_PROXY


async def create_sessions():
    while True:
        session_name = input('Enter a name for the session (press Enter to exit):\n')
        if not session_name:
            return

        if USE_PROXY:
            proxy_dict = {}
            with open('proxy.txt','r') as file:
                proxy_dict = {
                    parts[1]: parts[0]
                    for i in file if len(parts := i.strip().split()) == 2
                }

            if session_name in proxy_dict:
                proxy = proxy_dict[session_name]

                proxy_client = {
                    "scheme": config.PROXY_TYPE,
                    "hostname": proxy.split(':')[0],
                    "port": int(proxy.split(':')[1]),
                    "username": proxy.split(':')[2],
                    "password": proxy.split(':')[3],
                }
                session = Client(
                    api_id=config.API_ID,
                    api_hash=config.API_HASH,
                    name=session_name,
                    workdir=config.WORKDIR,
                    proxy=proxy_client
                )

                async with session:
                    user_data = await session.get_me()
                    logger.success(f'Session created successfully +{user_data.phone_number} @{user_data.username} PROXY : NONE')
            else:
                session = Client(
                    api_id=config.API_ID,
                    api_hash=config.API_HASH,
                    name=session_name,
                    workdir=config.WORKDIR,
                )

                async with session:
                    user_data = await session.get_me()
                    logger.success(f'Session created successfully +{user_data.phone_number} @{user_data.username} PROXY : NONE')
        else:
            session = Client(
                api_id=config.API_ID,
                api_hash=config.API_HASH,
                name=session_name,
                workdir=config.WORKDIR,
            )

            async with session:
                user_data = await session.get_me()

                logger.success(f'Session created successfully +{user_data.phone_number} @{user_data.username} PROXY : NONE')
