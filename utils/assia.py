#!/usr/bin/env python3
from typing import Optional, Tuple
from pyrogram.raw.functions.messages.request_web_view import RequestWebView
from urllib.parse import unquote
from utils.core import logger
from fake_useragent import UserAgent
from pyrogram.client import Client
from data import config
from datetime import datetime

import aiohttp
import asyncio
import random

class Assia:
    def __init__(
        self,
        thread: int,
        account: str,
        proxy : str
    ):
        """
        Initialize the class
        """
        self.thread = thread
        self.name = account

        if proxy:
            proxy_client = {
                "scheme": config.PROXY_TYPE,
                "hostname": proxy.split(':')[0],
                "port": int(proxy.split(':')[1]),
                "username": proxy.split(':')[2],
                "password": proxy.split(':')[3],
            }
            self.client = Client(
                name=account,
                api_id=config.API_ID,
                api_hash=config.API_HASH,
                workdir=config.WORKDIR,
                proxy=proxy_client
            )
        else:
            self.client = Client(
                name=account,
                api_id=config.API_ID,
                api_hash=config.API_HASH,
                workdir=config.WORKDIR
            )

        if proxy:
            self.proxy = f"{config.PROXY_TYPE}://{proxy.split(':')[2]}:{proxy.split(':')[3]}@{proxy.split(':')[0]}:{proxy.split(':')[1]}"
        else:
            self.proxy = None

        self.auth_token = ""
        self.ref_token = ""
        headers = {'User-Agent': UserAgent(os='android').random}
        self.session = aiohttp.ClientSession(
            headers=headers, trust_env=True,
            connector=aiohttp.TCPConnector(verify_ssl=False)
        )

    async def main(self):
        """Main function
        """
        await asyncio.sleep(random.randint(*config.ACC_DELAY))
        try:
            login = await self.login()
            if login == False:
                await self.session.close()
                return 0
            logger.info(
                f"main | Thread {self.thread} | {self.name} | Start! | PROXY : {self.proxy}")
        except Exception as err:
            logger.error(f"main | Thread {self.thread} | {self.name} | {err}")
            await self.session.close()
            return 0

        while True:
            try:
                valid = await self.is_token_valid()
                if not valid:
                    logger.warning(f"main | Thread {self.thread} | {self.name} | Token is invalid. Refreshing token...")
                    await self.safe_refresh()
                await asyncio.sleep(random.randint(*config.MINI_SLEEP))

                try:
                    time = await self.balance()

                    if not time:
                        logger.warning(f"main | Thread {self.thread} | {self.name} | No farming time found. Retrying...")
                        await asyncio.sleep(random.randint(*config.MINI_SLEEP))
                        raise
                    _, end_time = time
                except:
                    continue

                timestamp = int(datetime.utcnow().timestamp())
                add_sleep = random.randint(60, 150)  # added some extra seconds between 1 and 2 minutes.
                time_difference = end_time - timestamp + add_sleep
                if time_difference < 0:
                    time_difference = 0
                hours = time_difference // 3600
                minutes = (time_difference % 3600) // 60
                seconds = time_difference % 60
                logger.info(f"main | Thread {self.thread} | {self.name} | Sleep {hours} hours, {minutes} minutes, {seconds} seconds !")
                await asyncio.sleep(time_difference)
                await self.is_token_valid()
                balance = await self.claim()
                logger.info(f"main | Thread {self.thread} | {self.name} | Balance: {balance}")
                await asyncio.sleep(random.randint(*config.MINI_SLEEP))
            except Exception as err:
                logger.error(f"main | Thread {self.thread} | {self.name} | {err}")
                if err != "Server disconnected":
                    valid = await self.is_token_valid()
                    if not valid:
                        logger.warning(f"main | Thread {self.thread} | {self.name} | Token is invalid. Refreshing token...")
                        await self.safe_refresh()
                    await asyncio.sleep(random.randint(*config.MINI_SLEEP))
                else:
                    await asyncio.sleep(5*random.randint(*config.MINI_SLEEP))

    async def safe_refresh(self):
        """Refresh token"""
        try:
            await self.login()
        except Exception as err:
            logger.error(f"safe_refresh | Thread {self.thread} | {self.name} | {err}")
            await asyncio.sleep(5)

    async def claim(self) -> Optional[int]:
        """Claim reward"""
        try:
            resp = await self.session.post(
                "https://api.assai8.com/api/user/receive_airdrop_mining",
                proxy=self.proxy)
            resp_json = await resp.json()


            return resp_json.get("availableBalance")
        except:
            pass

    async def balance(
        self
    ) -> Optional[Tuple[int, int]]:
        """
        Get balance and farming start and end time

        Returns:
            Tuple[int, int, int]: timestamp, start_time, end_time
        """
        try:

            resp = await self.session.get(
                "https://api.assai8.com/api/user/mine", proxy=self.proxy)
            resp_json = (await resp.json())["data"]

            start_time = resp_json.get("mining_start_time")
            end_time = resp_json.get("mining_end_time")
            return int(start_time), int(end_time)
        except:
            return None


    async def login(self):
        """Login assias

        Returns:
            bool: true if login is success else false
        """
        max_retries = 20
        retry_delay = 2

        for _ in range(max_retries):
            try:
                tg_web_data = await self.get_tg_web_data()
                if tg_web_data == False:
                    return False

                json_data = {"init_data": tg_web_data}
                resp = await self.session.post(
                    "https://api.assai8.com/api/user/tg",
                    json=json_data,
                    proxy=self.proxy
                )

                if resp.headers.get('Content-Type', '').startswith('application/json'):
                    resp_data = (await resp.json())["data"]
                    self.session.headers['Authorization'] = "Bearer " + resp_data.get("token", "")
                    return True

                else:
                    raise ValueError("Response is not JSON - Retrying till the it works")

            except Exception as err:
                logger.error(f"login | Thread {self.thread} | {self.name} | {err}")
                if "Server disconnected" in str(err):
                    return True
                await asyncio.sleep(retry_delay)
        logger.error(f"login | Thread {self.thread} | {self.name} | Failed to get a valid response after {max_retries} attempts")
        return False

    async def get_tg_web_data(self):
        """Get telegram init data from web view

        Returns:
            str: tg web data
        """
        await self.client.connect()
        try:
            web_view = await self.client.invoke(RequestWebView(
                peer=await self.client.resolve_peer('ASSAI8Bot'),
                bot=await self.client.resolve_peer('ASSAI8Bot'),
                platform='android',
                from_bot_menu=False,
                url="https://api.assai8.com"
            ))

            auth_url = web_view.url
        except Exception as err:
            logger.error(f"main | Thread {self.thread} | {self.name} | {err}")
            if 'USER_DEACTIVATED_BAN' in str(err):
                logger.error(f"login | Thread {self.thread} | {self.name} | USER BANNED")
                await self.client.disconnect()
                return False
        await self.client.disconnect()
        return unquote(string=unquote(string=auth_url.split('tgWebAppData=')[1].split('&tgWebAppVersion')[0]))

    async def is_token_valid(self):
        """check if the token is valid
        """
        response = await self.session.get(
            "https://api.assai8.com/api/user/mine", proxy=self.proxy)

        if response.status == 200:
            return True
        else:
            return False
