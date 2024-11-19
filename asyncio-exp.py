import asyncio


#coroutine that increment counter and put it into the main queue
async def task_coro(queue):
    counter = 0
    while True:
        counter += 1
        await queue.put(counter)
        await asyncio.sleep(1)


#reading main queue to print task_coro value
async def print_value(queue):
    counter = await queue.get()
    print(f"value: {counter}")
    queue.task_done()


async def main():
    #creating queue
    queue = asyncio.Queue()

    #launching task that increment counter value
    task = asyncio.create_task(task_coro(queue))

    #interate as mush as the code need to
    while True:
        #uses task that print queue value
        await print_value(queue)

    await task

#running coroutine
asyncio.run(main())