import asyncio
import time

start = time.perf_counter()
async def func_one(secs):
    await asyncio.sleep(secs)
    print(f"Runnning .... {secs}")
    
async def main():
    async with asyncio.TaskGroup() as tg:
        for i in range(6):
            tg.create_task(func_one(i))


asyncio.run(main())
finish = time.perf_counter()

print(f"Running in {round(finish-start,2)}")

    
    

# async def func1():
#     print("I am running ===>1")
    
# async def func2():
#     await asyncio.sleep(5)
#     print("I am running ===>2")
    
# async def func3():
#     await asyncio.sleep(3)
#     print("I am running ===>3")
    
# async def func4():
#     print("I am running ===>4")
    
# async def main():
#     task1 = asyncio.create_task(func1())
#     task2 = asyncio.create_task(func2())
#     task3 = asyncio.create_task(func3())
#     task4 = asyncio.create_task(func4())
    
#     await task1
#     await task2
#     await task3
#     await task4

# asyncio.run(main())