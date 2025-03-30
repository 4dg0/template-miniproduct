from pydantic import BaseModel


class PBParams(BaseModel):
    filter: str
    expand: str
    sort: str
    fields: str
