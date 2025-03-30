import logfire

from contextlib import asynccontextmanager
from fastapi import FastAPI

from src.config import env, scheduler, pb


@asynccontextmanager
async def lifespan(app: FastAPI):
    # STARTUP
    logfire.configure(token=env.logfire_token, environment=env.logfire_env)
    logfire.info("Starting the app")

    await pb.login()
    logfire.info("PocketBase login successful")
    scheduler.start()

    yield

    # SHUTDOWN
    await pb.close()
    scheduler.shutdown()


app = FastAPI(lifespan=lifespan)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=env.debug)
