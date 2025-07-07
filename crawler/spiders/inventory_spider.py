# -*- coding: utf-8 -*-
from time import time, ctime
from base64 import b64encode
from random import uniform
from typing import Optional, Literal
from asyncio import Queue, create_task, gather, sleep, run

from parsel import Selector
from pymongo import AsyncMongoClient
from aiohttp import ClientSession, ClientResponse


class InventorySpider:
    def __init__(self, user_id: str):
        self.queue = Queue()
        self.inventory_id = user_id
        self.session = ClientSession(
            headers={
                "Accept": "text/javascript, text/html, application/xml, text/xml, */*",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
                "Referer": f"https://steamcommunity.com/profiles/{self.inventory_id}/inventory/",
                "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                # "Cookie": "timezoneOffset=28800,0; browserid=83994221101422839; strInventoryLastContext=730_2; sessionid=234dfadcb2938cf5881da205; steamLoginSecure=76561199548892760%7C%7CeyAidHlwIjogIkpXVCIsICJhbGciOiAiRWREU0EiIH0.eyAiaXNzIjogInI6MDAwRF8yNjg0Qzk0Q184OEY2MSIsICJzdWIiOiAiNzY1NjExOTk1NDg4OTI3NjAiLCAiYXVkIjogWyAid2ViOmNvbW11bml0eSIgXSwgImV4cCI6IDE3NTE4Njk0OTIsICJuYmYiOiAxNzQzMTQyMjQ4LCAiaWF0IjogMTc1MTc4MjI0OCwgImp0aSI6ICIwMDA4XzI2OTFFQzVFXzE5NEVFIiwgIm9hdCI6IDE3NTExOTY2OTIsICJydF9leHAiOiAxNzY5MTEwMzA0LCAicGVyIjogMCwgImlwX3N1YmplY3QiOiAiMTExLjI0My42NS4xNjgiLCAiaXBfY29uZmlybWVyIjogIjExMS4yNDMuNjUuMTY4IiB9.xEgQECW2V7Uz33_8M9mdmA1HFZCv405l5V-6tJcDRG-LXXgxM02RQu4sWHE5wcMbS9uIMuWvfE3UhGthBhllCA; steamCountry=HK%7Cea2372d8061403eefc34b1bad8f99fdf; recentlyVisitedAppHubs=730; rgTopicView_General_3381077=%7B%223780245614654210047%22%3A1751784513%7D; app_impressions=730@2_9_100006_100202; rgTopicView_General_4009259_7=%7B%223468361193658091414%22%3A1751784570%7D; webTradeEligibility=%7B%22allowed%22%3A0%2C%22reason%22%3A16424%2C%22allowed_at_time%22%3A1752389558%2C%22steamguard_required_days%22%3A15%2C%22new_device_cooldown_days%22%3A0%2C%22expiration%22%3A1751785059%2C%22time_checked%22%3A1751784759%7D"
            },
            proxy="http://127.0.0.1:7890"
        )
        self.mongo_client = AsyncMongoClient("mongodb://127.0.0.1:27017/")
        self.inventories_collection = self.mongo_client.get_database('analysisCs').get_collection('inventories')

    async def get_response(
        self,
        url: str,
        *,
        method: Literal['get', 'post'] = 'get',
        params: Optional[dict] = None
    ) -> ClientResponse:
        return await self.session.get(url, params=params)

    async def process_description(self, description: dict, batch_id: str):
        item_information = {
            'batch_id': batch_id,
            'class_id': description['classid'],
            'market_name': description['market_name'],
            'market_hash_name': description['market_hash_name'],
            'tags': description['tags']
        }

        picture_url = f'https://community.fastly.steamstatic.com/economy/image/{description["icon_url"]}/62fx62f'
        # price_url = f"https://steamcommunity.com/market/search"
        # parameter = {
        #     'appid': 'CN',
        #     'q': description['market_hash_name']
        # }
        price_url = 'https://steamcommunity.com/market/priceoverview'       # price 查询接口
        parameter = {
            'country': 'CN',
            'currency': 23,
            'appid': 730,
            'market_hash_name': description['market_hash_name']
        }
        tasks = [
            create_task(self.get_response(url=picture_url)),
            create_task(self.get_response(url=price_url, params=parameter))
        ]
        picture_resp, price_resp = await gather(*tasks, return_exceptions=True)
        async with price_resp:
            picture_resp = await picture_resp.read()
            # price_resp = Selector(await price_resp.text())
            price_resp = await price_resp.json()

        item_information['b64_str'] = b64encode(picture_resp).decode('utf-8')
        # item_information['price'] = {
        #     'lowest_price': price_resp.xpath('//span[@class="normal_price"][1]/text()').get(),
        #     'timestamp': time(),
        #     'datetime': ctime(time())
        # }
        item_information['market_price'] = price_resp
        print(item_information)

        await self.inventories_collection.insert_one(item_information)

    async def crawl_inventory_list(self):
        inventory_url = f"https://steamcommunity.com/inventory/{self.inventory_id}/730/2"
        parameter = {
            "count": 100
        }

        resp = await self.get_response(url=inventory_url, params=parameter)
        async with resp:
            data = await resp.json()

        batch_id = str(time())
        tasks = []
        for desc in data['descriptions']:
            tasks.append(
                create_task(self.process_description(desc, batch_id))
            )
            await sleep(uniform(4, 5))

        await gather(*tasks)

    async def close(self):
        await self.session.close()
        await self.mongo_client.close()


async def main() -> None:
    inventory_spider = InventorySpider("76561199405541900")
    await inventory_spider.crawl_inventory_list()
    await inventory_spider.close()


if __name__ == '__main__':
    run(main())
