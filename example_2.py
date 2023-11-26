import time
import asyncio


async def do_work(s: str, delay_s: float = 1.0):
    print(f"{s} started")
    await asyncio.sleep(delay_s)
    print(f"{s} done")


async def main():
    start = time.perf_counter()

    todo = ["get package", "laundry", "bake cake"]

    coros = [do_work(item) for item in todo]
    results = await asyncio.gather(*coros)
    print(results)

    end = time.perf_counter()
    print(f"it took: {end - start: .2f}s")


if __name__ == "__main__":
    asyncio.run(main())
