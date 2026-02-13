import asyncio

async def main():
    x = 5
    await asyncio.sleep(0.1)
    x += 10
    print(x)

asyncio.run(main())
