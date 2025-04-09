from fastapi import FastAPI
import stripe

from src.agent import init_agent
from src.config import *


async def startup(app: FastAPI):
    app.state.env = init_env()
    init_logging(app.state.env)

    app.state.pb = await init_pb(app.state.env)
    app.state.langfuse = init_langfuse(app.state.env)
    app.state.sheduler = init_sheduler(app.state.pb)

    stripe.api_key = app.state.env.stripe_api_key

    app.state.agent = init_agent(app.state.env)


async def shutdown(app: FastAPI):
    await app.state.pb.close()
    app.state.sheduler.shutdown()
