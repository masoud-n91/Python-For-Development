import asyncio
import time
import random


async def download():
    print("Downloading started")
    r = random.randint(0, 10)
    await asyncio.sleep(r)
    print(f"Downloading ended in {r} seconds")


async def ai():
    print("AI started")
    r = random.randint(0, 10)
    await asyncio.sleep(r)
    print(f"AI ended in {r} seconds")


async def printer():
    print("Printer started")
    r = random.randint(0, 10)
    await asyncio.sleep(r)
    print(f"Printer ended in {r} seconds")


async def main():
    await asyncio.gather(download(), printer(), ai())
    print("main ended")


if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main())
    print("--- %s seconds ---" % (time.time() - start_time))