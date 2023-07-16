import asyncio
from asyncio import Queue
from random import randrange
from typing import List


class Product:
    def __init__(self, name: str, checkout_time: float):
        self.name = name
        self.checkout_time = checkout_time


class Customer:
    def __init__(self, customer_id: int, products: List[Product]):
        self.customer_id = customer_id
        self.products = products


async def checkout_customer(queue: Queue, cashier_number: int):
    while not queue.empty():
        # 队列中有顾客
        customer: Customer = queue.get_nowait()
        print(f'收营员 {cashier_number} ' f'结账客户 ' f'{customer.customer_id}')

        for product in customer.products:
            # 检查每位顾客的商品
            print(f"收营员 {cashier_number} " f"正在给" f"{customer.customer_id}'s 结算 {product.name}")
            await asyncio.sleep(product.checkout_time)

        print(f'收营员 {cashier_number} ' f'完成对' f'{customer.customer_id} 的结算')
        queue.task_done()


async def main():
    customer_queue = Queue()

    all_products = [
        Product('beer', 2),
        Product('bananas', .5),
        Product('sausage', .2),
        Product('diapers', .2)
    ]

    # 随机创建10位顾客及产品
    for i in range(10):
        products = [all_products[randrange(len(all_products))] for _ in range(randrange(10))]
        customer_queue.put_nowait(Customer(i, products))

    # 创建三个收银员来结账
    cashiers = [asyncio.create_task(checkout_customer(customer_queue, i)) for i in range(3)]
    # join 协程将阻塞，直到队列为空并且所有顾客都已结账。
    await asyncio.gather(customer_queue.join(), *cashiers)


asyncio.run(main())
