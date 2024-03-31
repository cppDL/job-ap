from fastapi import FastAPI, Request
import asyncio
import robot

app = FastAPI()

counting_cancelled = asyncio.Event()

async def counting(startpoint):
    i = startpoint
    while not counting_cancelled.is_set():
        print(i)
        i += 1
        await asyncio.sleep(1)


@app.post("/startrobot")
async def startrobot(request: Request, startpoint: int):
    global task
    task = asyncio.create_task(counting(startpoint))
    start = asyncio.create_task(robot(startpoint))
    return {"message": "Robot has been started"}


@app.post("/stop_robot")
async def stop_robot(request: Request):
    global task
    task.cancel()
    return {"message": "Robot has been stopped"}


if __name__ == "__main__":
    print("Starting FastAPI server...")
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)