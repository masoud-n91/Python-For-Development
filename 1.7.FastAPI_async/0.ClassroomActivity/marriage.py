import asyncio
import time
import random


counter = 0


async def marraige(name):
    global counter

    r = random.randint(0, 10)
    await(asyncio.sleep(r))
    
    print(f"{name} is married after {r} years.")
    
    counter += 1


async def main():
    for child in ["Hazhir1", "Hazhir2", "Hazhir3", "Hazhir4"]:
        asyncio.create_task(marraige(child))

    while counter < 4:
        await asyncio.sleep(1)


if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main())
    print("--- %s seconds ---" % (time.time() - start_time))

