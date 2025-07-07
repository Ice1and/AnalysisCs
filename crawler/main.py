import asyncio

from spiders import InventorySpider


async def main() -> None:
    inventory_spider = InventorySpider("76561199405541900")
    await inventory_spider.crawl_inventory_list()
    await inventory_spider.close()


if __name__ == '__main__':
    asyncio.run(main())