import asyncio
import asyncpg
from util import async_timed
from typing import List, Dict
from concurrent.futures.process import ProcessPoolExecutor

# 查询 SQL
product_query = \
    """
SELECT *
FROM product as p
JOIN sku as s on s.product_id = p.product_id
JOIN product_color as pc on pc.product_color_id = s.product_color_id
JOIN product_size as ps on ps.product_size_id = s.product_size_id
WHERE p.product_id = 100
"""


# 查询方法
async def query_product(pool):
    async with pool.acquire() as connection:
        return await connection.fetchrow(product_query)


@async_timed()
async def query_products_concurrently(pool, queries):
    """
    并发查询
    :param pool: 连接池
    :param queries: 并发次数
    :return:
    """
    queries = [query_product(pool) for _ in range(queries)]
    return await asyncio.gather(*queries)


def run_in_new_loop(num_queries: int) -> List[Dict]:
    """
    新的事件循环
    :param num_queries:
    :return:
    """
    async def run_queries():
        async with asyncpg.create_pool(
                host='127.0.0.1',
                port=5432,
                user='postgres',
                password='password',
                database='products',
                min_size=6,
                max_size=6) as pool:
            return await query_products_concurrently(pool, num_queries)

    # 在一个新的事件循环中运行查询
    results = [dict(result) for result in asyncio.run(run_queries())]
    return results


@async_timed()
async def main():
    loop = asyncio.get_running_loop()
    pool = ProcessPoolExecutor()
    # 创造五个各自拥有事件循环的进程。
    tasks = [loop.run_in_executor(pool, run_in_new_loop, 10000) for _ in range(5)]
    # 等待所有查询结果查询完成
    all_results = await asyncio.gather(*tasks)
    total_queries = sum([len(result) for result in all_results])
    print(f'Retrieved {total_queries} products the product database.')


if __name__ == "__main__":
    asyncio.run(main())
