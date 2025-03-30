import logfire

from src.pkg.pb import PBClient

from .env import env
from .sheduler import scheduler


pb = PBClient(env.pb_url, env.pb_id, env.pb_password)


@scheduler.scheduled_job("interval", hours=3)
async def refresh_token():
    await pb.refresh()
    logfire.info("PocketBase token refreshed")
