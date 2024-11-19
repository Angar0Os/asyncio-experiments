import asyncio

async def task_coro():
    value = "Hello From Coroutine !"


async def print_coro_value(value):
    print(value)

async def main():
    coro = task_coro()
    task = asyncio.create_task(coro)
    await task
    value = task.result()

    print_coro_value(value)
    task2 = asyncio.create_task(print_coro_value(value))
    await task2

asyncio.run(main())

#TODO : acceder aux info / variables d'une coroutine pendant son execution
