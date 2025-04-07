import httpx

from .collection import Collection


class PBClient:
    def __init__(self, pb_url: str, pb_id: str, pb_password: str):
        self._client = httpx.AsyncClient(
            base_url=pb_url,
            timeout=httpx.Timeout(10.0, connect=5.0),
            headers={"Content-Type": "application/json"},
        )
        self.id = pb_id
        self.password = pb_password

    async def login(self):
        response = await self._client.post(
            "/api/collections/_superusers/auth-with-password",
            json={"identity": self.id, "password": self.password},
        )
        response.raise_for_status()
        token = response.json().get("token")

        self._client.headers.update({"Authorization": f"Bearer {token}"})

    async def refresh(self):
        response = await self._client.post(
            "/api/collections/_superusers/auth-refresh",
        )
        response.raise_for_status()
        token = response.json().get("token")

        self._client.headers.update({"Authorization": f"Bearer {token}"})

    def collection(self, name: str):
        return Collection(self, name)

    async def close(self):
        await self._client.aclose()

    # @asynccontextmanager
    # async def batch(self):
    #     batch = PBBatch(self)
    #     try:
    #         yield batch
    #     finally:
    #         results = await batch.send()
    #         logfire.info("Batch operations executed", results=len(results))
