import asyncio
from asyncio import Queue
from random import randrange


class Product:
    def __init__(self, name: str, checkout_time: float):
        self.name = name
        self.checkout_time = checkout_time


class Customer:
    def __init__(self, customer_id, products):
        self.customer_id = customer_id
        self.products = products


async def checkout_customer(queue: Queue, cashier_number: int):
    while True:
        customer: Customer = await queue.get()
        print(f'收营员 {cashier_number} ' f'结账客户 ' f'{customer.customer_id}')

        for product in customer.products:
            print(f"收营员 {cashier_number} " f"正在给" f"{customer.customer_id}'s 结算 {product.name}")
            await asyncio.sleep(product.checkout_time)

        print(f'收营员 {cashier_number} ' f'完成对' f'{customer.customer_id} 的结算')
        queue.task_done()


# 生成一个随机的客户
def generate_customer(customer_id: int) -> Customer:
    all_products = [
        Product('beer', 2),
        Product('bananas', .5),
        Product('sausage', .2),
        Product('diapers', .2)
    ]
    products = [all_products[randrange(len(all_products))] for _ in range(randrange(10))]
    return Customer(customer_id, products)


# 没秒随机生成几个顾客
async def customer_generator(queue: Queue):
    customer_count = 0
    while True:
        customers = [generate_customer(i) for i in range(customer_count, customer_count + randrange(5))]
        for customer in customers:
            print('客户正在等待排队...')
            await queue.put(customer)
            print('客户已加入排队!')
        customer_count = customer_count + len(customers)
        await asyncio.sleep(1)


async def main():
    # 限制每个队列的大小
    customer_queue = Queue(5)

    customer_producer = asyncio.create_task(customer_generator(customer_queue))

    cashiers = [asyncio.create_task(checkout_customer(customer_queue, i)) for i in range(3)]

    await asyncio.gather(customer_producer, *cashiers)


asyncio.run(main())
