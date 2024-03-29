import sys
import asyncio

async def counting():
    i=0
    while (True):
        print (i)
        i += 1
        await asyncio.sleep(1)
asyncio.run(counting())