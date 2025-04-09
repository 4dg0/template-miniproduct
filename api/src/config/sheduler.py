from apscheduler.schedulers.asyncio import AsyncIOScheduler

from src.pkg.pb import PBClient

from .pb import refresh_token


def init_sheduler(pb: PBClient):
    scheduler = AsyncIOScheduler()

    scheduler.add_job(lambda: refresh_token(pb), trigger="interval", hours=6)

    scheduler.start()
    return scheduler
