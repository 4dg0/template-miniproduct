from .models import PBParams


class Collection:
    def __init__(self, pb: "PBClient", collection_id: str):
        self.pb = pb
        self.collection_id = collection_id

    async def get_one(self, record_id: str, params: PBParams):
        url = f"/api/collections/{self.collection_id}/records/{record_id}"
        response = await self.pb._client.get(url, params=params.model_dump())
        response.raise_for_status()
        return response.json()

    async def get_full_list(self, params: PBParams):
        url = f"/api/collections/{self.collection_id}/records"
        response = await self.pb._client.get(url, params=params.model_dump())
        response.raise_for_status()
        return response.json()

    async def get_list(self, page: int, per_page: int, params: PBParams):
        url = f"/api/collections/{self.collection_id}/records"
        params_dict = params.model_dump()
        params_dict.update({"page": page, "perPage": per_page})
        response = await self.pb._client.get(url, params=params_dict)
        response.raise_for_status()
        return response.json()

    async def create(self, data: dict):
        url = f"/api/collections/{self.collection_id}/records"
        response = await self.pb._client.post(url, json=data)
        response.raise_for_status()
        return response.json()

    async def update(self, record_id: str, data: dict):
        url = f"/api/collections/{self.collection_id}/records/{record_id}"
        response = await self.pb._client.patch(url, json=data)
        response.raise_for_status()
        return response.json()

    async def delete(self, record_id: str):
        url = f"/api/collections/{self.collection_id}/records/{record_id}"
        response = await self.pb._client.delete(url)
        response.raise_for_status()
        return response.json()
