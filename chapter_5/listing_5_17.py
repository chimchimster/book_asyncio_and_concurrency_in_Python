import asyncpg
import asyncio


async def take(generator, to_take: int):
    item_count = 0

    async for item in generator:
        if item_count > to_take - 1:
            return
        item_count += 1
        yield item


async def main():
    connection = await asyncpg.connect(host='localhost',
                                       port=5432,
                                       user='postgres',
                                       database='products',
                                       password='password')

    async with connection.transaction():
        query = 'select product_id, product_name from product'
        product_generator = connection.cursor(query)

        async for product in take(product_generator, 5):
            print(product)

        print('Получаем первые пять товаров!')

    await connection.close()


asyncio.run(main())