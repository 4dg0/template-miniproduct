from fastapi import Request

from src.pkg.pb import PBClient

from .env import Env


def get_pb(request: Request) -> PBClient:
    return request.app.state.pb


async def init_pb(env: Env):
    pb = PBClient(env.pb_url, env.pb_id, env.pb_password)
    await pb.login()
    return pb


async def refresh_token(pb: PBClient):
    await pb.refresh()
