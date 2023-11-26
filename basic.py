import time
import asyncio


async def do_work(s: str, delay_s: float = 1.0):
    print(f"{s} started")
    await asyncio.sleep(delay_s)
    print(f"{s} done")


async def main():
    start = time.perf_counter()

    todo = ["get package", "laundry", "bake cake"]

    for item in todo:
        await do_work(item)

    end = time.perf_counter()
    print(f"it took: {end - start: .2f}s")


if __name__ == "__main__":
    asyncio.run(main())
