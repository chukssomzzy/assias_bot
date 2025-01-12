#!/usr/bin/env python3
from utils.core import create_sessions
from utils.telegram import Accounts
from utils.blum import Blum
from data.config import hello, USE_PROXY
import asyncio
import os
from utils.core import logger
import random

async def main():
    print(hello)
    action = int(input("Select action:\n1. Create sessions\n2. Start claimer\n\n> "))

    if not os.path.exists('sessions'):
        os.mkdir('sessions')

    if action == 1:
        await create_sessions()

    elif action == 2:
        while True:
            accounts = await Accounts().get_accounts()
            with open('proxy.txt', 'r', encoding='utf-8') as file:
                proxy = [i.strip() for i in file.readlines()]
            tasks = []

            if USE_PROXY:
                proxy_dict = {}
                with open('proxy.txt', 'r') as file:
                    proxy = [i.strip().split() for i in file.readlines() if len(i.strip().split()) == 2]
                    for prox, name in proxy:
                        proxy_dict[name] = prox

                for thread, account in enumerate(accounts):
                    if account in proxy_dict:
                        tasks.append(asyncio.create_task(Blum(account=account, thread=thread, proxy=proxy_dict[account]).main()))
                    else:
                        tasks.append(asyncio.create_task(Blum(account=account, thread=thread, proxy=None).main()))
            else:
                for thread, account in enumerate(accounts):
                    tasks.append(asyncio.create_task(Blum(account=account, thread=thread, proxy=None).main()))

            try:
                await asyncio.wait_for(asyncio.gather(*tasks), timeout=random.randint(2400,3600))
            except asyncio.TimeoutError:
                logger.info("Timeout reached. Closing Blum running Code...")

            for task in tasks:
                if not task.done():
                    task.cancel()
                    try:
                        await task
                    except asyncio.CancelledError:
                        logger.info(f"Running code is Closed")

            logger.info("Restarting Blum Code...")

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
