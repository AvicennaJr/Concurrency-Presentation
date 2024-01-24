import multiprocessing
import asyncio
import time

async def cpu_bound_async(number):
    return sum(i * i for i in range(number))

async def find_sums_async(numbers):
    with multiprocessing.Pool() as pool:
        tasks = [loop.run_in_executor(None, cpu_bound_async, number) for number in numbers]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    numbers = [5_000_000 + x for x in range(20)]

    start_time = time.time()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(find_sums_async(numbers))

    duration = time.time() - start_time
    print(f"Duration {duration} seconds")

