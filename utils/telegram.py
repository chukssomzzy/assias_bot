from typing import Dict, Optional
from utils.core import logger
from pyrogram import Client
from data import config
import os

class Accounts:
    def __init__(self):
        self.workdir = config.WORKDIR
        self.api_id = config.API_ID
        self.api_hash = config.API_HASH

    def pars_sessions(self):
        sessions = []
        for file in os.listdir(self.workdir):
            if file.endswith(".session"):
                sessions.append(file.replace(".session", ""))

        logger.info(f"Session Found: {len(sessions)}!")
        return sessions

    async def check_valid_sessions(self, sessions: list):
        logger.info(f"Checking sessions for validity!")
        valid_sessions = []
        if config.USE_PROXY:
            proxy_dict = {}
            with open('proxy.txt','r') as file:
                proxy_dict = {
                    parts[1]: parts[0]
                    for i in file if len(parts := i.strip().split()) == 2
                }

            for session in sessions:
                try:
                    if session in proxy_dict:
                        proxy = proxy_dict[session]
                        proxy_client = {
                            "scheme": config.PROXY_TYPE,
                            "hostname": proxy.split(':')[0],
                            "port": int(proxy.split(':')[1]),
                            "username": proxy.split(':')[2],
                            "password": proxy.split(':')[3],
                        }

                        if await self.is_session_valid(session, proxy_client):
                            valid_sessions.append(session)
                    else:
                        if await self.is_session_valid(session):
                            valid_sessions.append(session)
                except:
                    logger.error(f"{session}.session is invalid")
            logger.success(f"Valid sessions: {len(valid_sessions)}; Invalid: {len(sessions)-len(valid_sessions)}")

        else:
            for session in sessions:
                try:
                    if await self.is_session_valid(session):
                        valid_sessions.append(session)
                except:
                    logger.error(f"{session}.session is invalid")
            logger.success(f"Valid Sessions: {len(valid_sessions)}; Invalid: {len(sessions) - len(valid_sessions)}")
        return valid_sessions

    async def get_accounts(self):
        sessions = self.pars_sessions()
        accounts = await self.check_valid_sessions(sessions)

        if not accounts:
            raise ValueError("No valid sessions")
        else:
            return accounts

    async def is_session_valid(self, session: str, proxy_client: Optional[Dict] = None) -> bool:
        """Check if a session is still valid"""
        client = Client(
            name=session,
            api_id=self.api_id,
            api_hash=self.api_hash,
            workdir=self.workdir,
            proxy=proxy_client
        )

        if await client.connect():
            return True
        else:
            logger.error(f"{session}.session is invalid")

        await client.disconnect()
        return False
