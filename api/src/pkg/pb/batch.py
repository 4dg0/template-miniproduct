# THIS PEACE OF CODE IS STRANGE AND NOT TESTED

# import httpx


# class BatchOperation:
#     def __init__(
#         self, collection: str, action: str, payload: dict, record_id: str | None = None
#     ):
#         self.collection = collection
#         self.action = action  # "create", "update", "delete", "upsert"
#         self.payload = payload
#         self.record_id = record_id


# class BatchCollectionProxy:
#     def __init__(self, batch, collection_id: str):
#         self.batch = batch
#         self.collection_id = collection_id

#     def create(self, data: dict):
#         self.batch._add(BatchOperation(self.collection_id, "create", data))

#     def update(self, record_id: str, data: dict):
#         self.batch._add(BatchOperation(self.collection_id, "update", data, record_id))

#     def delete(self, record_id: str):
#         self.batch._add(BatchOperation(self.collection_id, "delete", {}, record_id))

#     def upsert(self, data: dict):
#         self.batch._add(BatchOperation(self.collection_id, "upsert", data))


# class PBBatch:
#     def __init__(self, client: "PBClient"):
#         self.client = client
#         self.operations: list[BatchOperation] = []

#     def _add(self, op: BatchOperation):
#         self.operations.append(op)

#     def collection(self, name: str) -> BatchCollectionProxy:
#         return BatchCollectionProxy(self, name)

#     async def send(self):
#         results = []
#         for op in self.operations:
#             col = self.client.collection(op.collection)
#             try:
#                 match op.action:
#                     case "create":
#                         res = await col.create(op.payload)
#                     case "update":
#                         res = await col.update(op.record_id, op.payload)
#                     case "delete":
#                         res = await col.delete(op.record_id)
#                     case "upsert":
#                         id_ = op.payload.get("id")
#                         if id_:
#                             try:
#                                 res = await col.update(id_, op.payload)
#                             except httpx.HTTPStatusError as e:
#                                 if e.response.status_code == 404:
#                                     res = await col.create(op.payload)
#                                 else:
#                                     raise
#                         else:
#                             res = await col.create(op.payload)
#                     case _:
#                         raise ValueError(f"Unknown action: {op.action}")
#                 results.append(res)
#             except Exception as e:
#                 results.append({"error": str(e), "operation": op})
#         return results
