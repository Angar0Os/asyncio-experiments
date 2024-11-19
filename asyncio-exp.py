import asyncio
from asyncio import TaskGroup

async def async_sayHello():
    while True:
        await asyncio.sleep(3)
        print("Hello World")
        await asyncio.sleep(5)
        print("Goodbye World")

async def async_main():
    task0 = asyncio.create_task(async_sayHello())

    count = 0
    loop = asyncio.get_event_loop()

    while True:
        print(count)
        count += 1
        await asyncio.sleep(1)

asyncio.run(async_main())

#faire communiquer les fonctions entre elle